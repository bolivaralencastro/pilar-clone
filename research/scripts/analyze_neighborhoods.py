#!/usr/bin/env python3
"""
Análise de distribuição de imóveis por bairro - PilarHomes
Extrai dados da API e gera estatísticas
"""

import requests
import json
from collections import Counter
import re

def extract_neighborhood_from_slug(slug):
    """Extrai bairro do slug do imóvel"""
    # Padrão: tipo-quartos-BAIRRO-cidade
    # Ex: casa-3-quartos-jardim-europa-sao-paulo
    parts = slug.split('-')
    
    # Remover tipo (casa, apartamento, cobertura, etc)
    tipos = ['casa', 'apartamento', 'cobertura', 'duplex', 'studio', 'flat', 'terreno', 'loft', 'sobrado', 'kitnet', 'imovel']
    
    # Remover cidade do final (geralmente últimas 2-3 palavras)
    cidades = ['sao-paulo', 'rio-janeiro', 'curitiba', 'belo-horizonte', 'brasilia', 
               'porto-alegre', 'salvador', 'fortaleza', 'recife', 'goiania',
               'sp', 'rj', 'pr', 'mg', 'df', 'rs', 'ba', 'ce', 'pe', 'go',
               'guaruja', 'santos', 'campinas', 'ribeirao-preto', 'uberlandia',
               'florianopolis', 'joinville', 'londrina', 'maringa']
    
    # Encontrar onde começa a cidade (do final)
    end_idx = len(parts)
    for i in range(len(parts) - 1, -1, -1):
        if parts[i] in cidades or (i > 0 and f"{parts[i-1]}-{parts[i]}" in [c.replace('-', ' ').replace(' ', '-') for c in cidades]):
            end_idx = i
            if i > 0 and f"{parts[i-1]}-{parts[i]}" in cidades:
                end_idx = i - 1
            break
    
    # Encontrar onde termina o tipo (do início)
    start_idx = 0
    for i, part in enumerate(parts):
        if part in tipos:
            start_idx = i + 1
        elif part.isdigit() or part == 'quartos' or part == 'quarto':
            start_idx = i + 1
    
    # Extrair bairro
    if start_idx < end_idx:
        bairro = '-'.join(parts[start_idx:end_idx])
        # Limpar
        bairro = re.sub(r'-+', '-', bairro)
        bairro = bairro.strip('-')
        return bairro if bairro else None
    
    return None

def format_neighborhood(bairro):
    """Formata nome do bairro para título"""
    if not bairro:
        return "Outros"
    
    # Substituir hífens por espaços e capitalizar
    formatted = bairro.replace('-', ' ').title()
    
    # Correções específicas
    corrections = {
        'Sao Paulo': 'São Paulo',
        'Sao': 'São',
        'Itaim': 'Itaim Bibi',
        'Alto De Pinheiros': 'Alto de Pinheiros',
        'Jardim Paulista': 'Jardim Paulista',
        'Vila Nova Conceicao': 'Vila Nova Conceição',
        'Cidade Jardim': 'Cidade Jardim',
        'Moema': 'Moema',
    }
    
    for old, new in corrections.items():
        if formatted == old:
            formatted = new
            break
    
    return formatted

def fetch_all_properties():
    """Busca todos os imóveis da API (paginado)"""
    all_properties = []
    offset = 0
    limit = 100
    total = None
    
    print("Buscando imóveis da API PilarHomes...")
    
    while True:
        url = f"https://pilarhomes.com.br/api/properties?limit={limit}&offset={offset}"
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            if total is None:
                total = data.get('total', 0)
                print(f"Total de imóveis: {total}")
            
            properties = data.get('properties', [])
            if not properties:
                break
            
            all_properties.extend(properties)
            offset += limit
            
            print(f"  Carregados: {len(all_properties)}/{total} ({100*len(all_properties)//total}%)")
            
            if len(all_properties) >= total:
                break
                
        except Exception as e:
            print(f"Erro ao buscar offset {offset}: {e}")
            break
    
    return all_properties, total

def analyze_neighborhoods(properties):
    """Analisa distribuição por bairro"""
    bairros = []
    cidades = []
    
    for prop in properties:
        slug = prop.get('slug', '')
        city = prop.get('city', 'Desconhecida')
        
        bairro = extract_neighborhood_from_slug(slug)
        if bairro:
            bairros.append(format_neighborhood(bairro))
        
        cidades.append(city)
    
    return Counter(bairros), Counter(cidades)

def main():
    # Buscar todos os imóveis
    properties, total = fetch_all_properties()
    
    print(f"\n{'='*60}")
    print(f"ANÁLISE DE DISTRIBUIÇÃO - PILARHOMES")
    print(f"{'='*60}")
    print(f"Total de imóveis analisados: {len(properties)}")
    
    # Analisar
    bairros_count, cidades_count = analyze_neighborhoods(properties)
    
    # Top 30 bairros
    print(f"\n📍 TOP 30 BAIRROS (de {len(bairros_count)} bairros únicos)")
    print("-" * 50)
    
    top_bairros = bairros_count.most_common(30)
    total_imoveis = sum(bairros_count.values())
    
    results = []
    for i, (bairro, count) in enumerate(top_bairros, 1):
        pct = (count / total_imoveis) * 100
        bar = "█" * int(pct)
        print(f"{i:2}. {bairro:<30} {count:4} ({pct:5.2f}%) {bar}")
        results.append({
            "rank": i,
            "bairro": bairro,
            "count": count,
            "percentage": round(pct, 2)
        })
    
    # Top 10 cidades
    print(f"\n🏙️ TOP 10 CIDADES")
    print("-" * 50)
    
    for i, (cidade, count) in enumerate(cidades_count.most_common(10), 1):
        pct = (count / len(properties)) * 100
        print(f"{i:2}. {cidade:<25} {count:4} ({pct:5.2f}%)")
    
    # Salvar resultados
    output = {
        "total_properties": len(properties),
        "total_unique_neighborhoods": len(bairros_count),
        "total_unique_cities": len(cidades_count),
        "top_30_neighborhoods": results,
        "all_neighborhoods": dict(bairros_count.most_common()),
        "cities": dict(cidades_count.most_common())
    }
    
    with open("research/data/neighborhood_analysis.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Resultados salvos em: research/data/neighborhood_analysis.json")
    
    return output

if __name__ == "__main__":
    main()
