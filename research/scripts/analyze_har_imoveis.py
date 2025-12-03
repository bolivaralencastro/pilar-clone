#!/usr/bin/env python3
"""
Análise HAR - Página de Imóveis pilarhomes.com.br/venda/imoveis/
"""

import json
from collections import defaultdict
from urllib.parse import urlparse, parse_qs

def analyze_imoveis_har():
    with open('pilarhomes_imoveis.har', 'r', encoding='utf-8') as f:
        har = json.load(f)

    entries = har.get('log', {}).get('entries', [])
    print(f"📊 ANÁLISE HAR - /venda/imoveis/")
    print(f"{'='*60}")
    print(f"Total de requisições: {len(entries)}")

    domains = defaultdict(lambda: {'count': 0, 'size': 0, 'urls': []})
    apis = []
    images = []
    tracking = []
    
    tracking_services = {
        'google-analytics': 'Google Analytics',
        'googletagmanager': 'GTM',
        'facebook': 'Facebook',
        'tiktok': 'TikTok',
        'hotjar': 'Hotjar',
        'datadoghq': 'Datadog',
        'clickcease': 'ClickCease',
        'stape': 'Stape (Server GTM)',
    }

    for entry in entries:
        request = entry.get('request', {})
        response = entry.get('response', {})
        url = request.get('url', '')
        domain = urlparse(url).netloc
        path = urlparse(url).path
        size = response.get('content', {}).get('size', 0) or 0
        content_type = response.get('content', {}).get('mimeType', '')
        method = request.get('method', '')
        status = response.get('status', '')
        
        domains[domain]['count'] += 1
        domains[domain]['size'] += size
        
        # APIs
        if '/api/' in url or 'api.' in domain or 'graphql' in url.lower():
            # Tenta extrair body da request
            post_data = request.get('postData', {})
            body_preview = ''
            if post_data:
                text = post_data.get('text', '')[:200]
                body_preview = text
            
            apis.append({
                'url': url,
                'method': method,
                'status': status,
                'size': size,
                'body': body_preview
            })
        
        # Imagens
        if 'image' in content_type or path.endswith(('.jpg', '.png', '.webp', '.svg')):
            images.append({
                'url': url,
                'size': size,
                'type': content_type
            })
        
        # Tracking
        for pattern, name in tracking_services.items():
            if pattern in url.lower():
                tracking.append({'service': name, 'url': url[:80]})
                break

    # Relatório
    print("\n" + "="*60)
    print("🌐 TOP DOMÍNIOS POR REQUISIÇÕES")
    print("="*60)
    print(f"{'Reqs':>5} {'Size':>10} {'Domínio':<45}")
    print("-"*65)
    for d, data in sorted(domains.items(), key=lambda x: x[1]['count'], reverse=True)[:20]:
        print(f"{data['count']:>5} {data['size']/1024:>8.1f}KB  {d[:45]}")

    print("\n" + "="*60)
    print("🔌 APIs IDENTIFICADAS")
    print("="*60)
    seen_apis = set()
    for api in apis:
        parsed = urlparse(api['url'])
        key = f"{api['method']} {parsed.netloc}{parsed.path.split('?')[0]}"
        if key not in seen_apis:
            seen_apis.add(key)
            print(f"\n{api['method']:>6} [{api['status']}] {parsed.netloc}{parsed.path[:60]}")
            if api['body']:
                # Tenta parsear JSON para ver estrutura
                try:
                    body_json = json.loads(api['body'])
                    if 'query' in str(body_json).lower()[:50]:
                        print(f"       → GraphQL Query detectada")
                    if 'operationName' in body_json:
                        print(f"       → Operation: {body_json.get('operationName')}")
                except:
                    print(f"       → Body: {api['body'][:80]}...")

    print("\n" + "="*60)
    print("🖼️ ANÁLISE DE IMAGENS")
    print("="*60)
    total_images = len(images)
    total_size = sum(i['size'] for i in images) / 1024 / 1024
    
    # Agrupa por domínio
    img_domains = defaultdict(lambda: {'count': 0, 'size': 0})
    for img in images:
        domain = urlparse(img['url']).netloc
        img_domains[domain]['count'] += 1
        img_domains[domain]['size'] += img['size']
    
    print(f"Total de imagens: {total_images}")
    print(f"Tamanho total: {total_size:.2f} MB")
    print("\nPor domínio:")
    for d, data in sorted(img_domains.items(), key=lambda x: x[1]['count'], reverse=True):
        print(f"  {data['count']:>4}x  {data['size']/1024:>8.1f}KB  {d}")

    print("\n" + "="*60)
    print("📊 TRACKING SERVICES")
    print("="*60)
    tracking_count = defaultdict(int)
    for t in tracking:
        tracking_count[t['service']] += 1
    for service, count in sorted(tracking_count.items(), key=lambda x: x[1], reverse=True):
        print(f"  {count:>3}x  {service}")

    # Comparação com homepage
    print("\n" + "="*60)
    print("📈 COMPARAÇÃO COM HOMEPAGE")
    print("="*60)
    print(f"Homepage:     287 requisições")
    print(f"Página imóveis: {len(entries)} requisições")
    print(f"Diferença:    {len(entries) - 287:+d} requisições")

    # Salva resumo
    summary = {
        'page': '/venda/imoveis/',
        'total_requests': len(entries),
        'total_images': total_images,
        'total_image_size_mb': round(total_size, 2),
        'top_domains': {d: data for d, data in sorted(domains.items(), key=lambda x: x[1]['count'], reverse=True)[:10]},
        'apis_found': list(seen_apis),
        'tracking_services': dict(tracking_count)
    }
    
    with open('har_imoveis_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2, default=str)
    
    print(f"\n💾 Resumo salvo em: har_imoveis_summary.json")


if __name__ == "__main__":
    analyze_imoveis_har()
