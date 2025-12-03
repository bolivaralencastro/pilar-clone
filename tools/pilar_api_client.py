"""
🏠 Pilar Homes API Client
Cliente Python completo para recriar o sistema de busca da Pilar Homes

Uso:
    python pilar_api_client.py

Ou importe como módulo:
    from pilar_api_client import PilarHomesAPI
    api = PilarHomesAPI()
    results = api.search(property_type="apartment", max_price=2000000)
"""

import requests
from typing import Optional, Dict, List, Any
from dataclasses import dataclass
from datetime import datetime
import json

# ============================================================================
# CONFIGURAÇÃO
# ============================================================================

API_BASE_URL = "https://pilarhomes.com.br/api"
GOOGLE_MAPS_KEY = "AIzaSyB6TCbFAul6VL_VEWQ9-_pmOWhjas1ALGQ"

# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class Property:
    """Representa um imóvel"""
    id: str
    slug: str
    title: str
    description: str
    property_type: str
    transaction_type: str
    
    # Localização
    region: str
    city: str
    state: str
    condo_name: Optional[str]
    
    # Preços
    asking_price: Optional[int]
    rent_price: Optional[int]
    condo_fee: Optional[int]
    tax: Optional[float]
    
    # Características
    area: int
    total_area: Optional[int]
    bedrooms: int
    bathrooms: int
    suites: int
    parking_spots: int
    
    # Mídia
    images: List[str]
    videos: List[str]
    
    # Metadata
    commercial_id: str
    is_exclusive: bool
    company_name: str
    agent_name: str
    
    # Features
    features: Dict[str, List[str]]
    
    @classmethod
    def from_api(cls, data: Dict) -> 'Property':
        """Cria Property a partir do JSON da API"""
        return cls(
            id=data.get('id', ''),
            slug=data.get('slug', ''),
            title=data.get('ad', {}).get('title', ''),
            description=data.get('ad', {}).get('description', ''),
            property_type=data.get('propertyType', {}).get('name', ''),
            transaction_type=data.get('ad', {}).get('transactionType', ''),
            
            region=data.get('region', ''),
            city=data.get('city', ''),
            state=data.get('state', ''),
            condo_name=data.get('condoName'),
            
            asking_price=data.get('askingPrice'),
            rent_price=data.get('rentPrice'),
            condo_fee=data.get('condoFee'),
            tax=data.get('tax'),
            
            area=data.get('area', 0),
            total_area=data.get('totalArea'),
            bedrooms=data.get('bedrooms', 0),
            bathrooms=data.get('bathrooms', 0),
            suites=data.get('suites', 0),
            parking_spots=data.get('parkingSpots', 0),
            
            images=[img.get('watermarkUrl', '') for img in data.get('images', [])],
            videos=data.get('videos', []),
            
            commercial_id=data.get('commercialId', ''),
            is_exclusive=data.get('isExclusive', False),
            company_name=data.get('company', {}).get('name', ''),
            agent_name=data.get('agent', {}).get('name', ''),
            
            features={
                cat: [f.get('name', '') for f in features]
                for cat, features in data.get('featuresByCategory', {}).items()
            }
        )
    
    def format_price(self) -> str:
        """Formata o preço em R$"""
        price = self.asking_price or self.rent_price
        if not price:
            return "Sob consulta"
        return f"R$ {price:,.0f}".replace(",", ".")
    
    def __str__(self) -> str:
        return f"{self.property_type} em {self.region} - {self.format_price()}"


@dataclass
class SearchResult:
    """Resultado de uma busca"""
    properties: List[Property]
    page: int
    per_page: int
    total_pages: int
    total_count: int
    
    @classmethod
    def from_api(cls, data: Dict) -> 'SearchResult':
        pagination = data.get('pagination', {})
        # A API pode retornar 'data' ou 'properties' dependendo do endpoint
        properties_data = data.get('data') or data.get('properties', [])
        return cls(
            properties=[Property.from_api(p) for p in properties_data],
            page=pagination.get('page', 1),
            per_page=pagination.get('perPage', 12),
            total_pages=pagination.get('totalPages', 0),
            total_count=pagination.get('filteredCount', 0)
        )


# ============================================================================
# API CLIENT
# ============================================================================

class PilarHomesAPI:
    """Cliente para a API da Pilar Homes"""
    
    # Tipos de imóveis válidos
    PROPERTY_TYPES = {
        'apartment': 'Apartamento',
        'house': 'Casa',
        'penthouse': 'Cobertura',
        'land': 'Terreno',
        'commercial': 'Comercial',
        'studio': 'Studio',
        'flat': 'Flat'
    }
    
    # Tipos de transação
    TRANSACTION_TYPES = ['sell', 'rent']
    
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        # Headers necessários para passar pelo WAF/proteção
        self.session.headers.update({
            'Accept': 'application/json',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://pilarhomes.com.br/',
            'Origin': 'https://pilarhomes.com.br'
        })
    
    def search(
        self,
        transaction_type: str = "sell",
        page: int = 1,
        per_page: int = 12,
        property_type: Optional[str] = None,
        min_price: Optional[int] = None,
        max_price: Optional[int] = None,
        min_area: Optional[int] = None,
        max_area: Optional[int] = None,
        bedrooms: Optional[int] = None,
        suites: Optional[int] = None,
        parking_spots: Optional[int] = None,
        city: Optional[str] = None,
        region: Optional[str] = None,
        is_exclusive: Optional[bool] = None
    ) -> SearchResult:
        """
        Busca imóveis com filtros
        
        Args:
            transaction_type: 'sell' para venda, 'rent' para aluguel
            page: Número da página (1-indexed)
            per_page: Itens por página (máx 50)
            property_type: apartment, house, penthouse, land, commercial
            min_price: Preço mínimo
            max_price: Preço máximo
            min_area: Área mínima em m²
            max_area: Área máxima em m²
            bedrooms: Número mínimo de quartos
            suites: Número mínimo de suítes
            parking_spots: Número mínimo de vagas
            city: Nome da cidade
            region: Nome do bairro
            is_exclusive: Apenas imóveis exclusivos
        
        Returns:
            SearchResult com lista de Property
        """
        params = {
            'transactionType': transaction_type,
            'page': page,
            'perPage': min(per_page, 50)  # API limita em 50
        }
        
        # Adicionar filtros opcionais
        optional_params = {
            'propertyType': property_type,
            'minPrice': min_price,
            'maxPrice': max_price,
            'minArea': min_area,
            'maxArea': max_area,
            'bedrooms': bedrooms,
            'suites': suites,
            'parkingSpots': parking_spots,
            'city': city,
            'region': region,
            'isExclusive': is_exclusive
        }
        
        for key, value in optional_params.items():
            if value is not None:
                params[key] = value
        
        response = self.session.get(f"{self.base_url}/properties", params=params)
        response.raise_for_status()
        
        return SearchResult.from_api(response.json())
    
    def get_by_slug(self, slug: str) -> Optional[Property]:
        """Busca um imóvel específico pelo slug"""
        try:
            response = self.session.get(f"{self.base_url}/properties/{slug}")
            response.raise_for_status()
            return Property.from_api(response.json())
        except requests.exceptions.HTTPError:
            return None
    
    def get_clusters(self, transaction_type: str = "sell") -> Dict:
        """
        Busca clusters de imóveis para o mapa
        Retorna dados agregados por região
        """
        response = self.session.get(
            f"{self.base_url}/properties/clusters",
            params={'transactionType': transaction_type}
        )
        response.raise_for_status()
        return response.json()
    
    def search_all(
        self,
        max_results: int = 100,
        **filters
    ) -> List[Property]:
        """
        Busca todos os imóveis com paginação automática
        
        Args:
            max_results: Número máximo de resultados
            **filters: Mesmos filtros do método search()
        
        Returns:
            Lista de Property
        """
        all_properties = []
        page = 1
        per_page = 50  # Máximo permitido
        
        while len(all_properties) < max_results:
            result = self.search(page=page, per_page=per_page, **filters)
            
            if not result.properties:
                break
            
            all_properties.extend(result.properties)
            
            if page >= result.total_pages:
                break
            
            page += 1
        
        return all_properties[:max_results]
    
    def get_regions(self, city: str = "São Paulo") -> List[str]:
        """
        Busca todos os bairros disponíveis em uma cidade
        (Inferido dos resultados)
        """
        result = self.search(city=city, per_page=50)
        regions = set()
        
        for prop in result.properties:
            if prop.region:
                regions.add(prop.region)
        
        return sorted(regions)


# ============================================================================
# FUNÇÕES DE CONVENIÊNCIA
# ============================================================================

def format_property_card(prop: Property) -> str:
    """Formata um imóvel como card de texto"""
    lines = [
        "━" * 50,
        f"📍 {prop.region}, {prop.city} - {prop.state}",
        f"🏠 {prop.property_type} | {prop.area}m²",
        f"💰 {prop.format_price()}",
        f"",
        f"🛏️ {prop.bedrooms} quartos | 🛁 {prop.bathrooms} banheiros | 🚗 {prop.parking_spots} vagas",
    ]
    
    if prop.suites:
        lines[4] = f"   ({prop.suites} suítes)"
    
    if prop.condo_fee:
        lines.append(f"📋 Condomínio: R$ {prop.condo_fee:,.0f}".replace(",", "."))
    
    if prop.is_exclusive:
        lines.append("⭐ EXCLUSIVO")
    
    lines.append(f"")
    lines.append(f"🔗 https://pilarhomes.com.br/imovel/{prop.slug}")
    lines.append(f"📝 Cód: {prop.commercial_id} | {prop.company_name}")
    
    return "\n".join(lines)


def export_to_json(properties: List[Property], filename: str):
    """Exporta imóveis para JSON"""
    data = []
    for prop in properties:
        data.append({
            'id': prop.id,
            'title': prop.title,
            'type': prop.property_type,
            'location': f"{prop.region}, {prop.city}",
            'price': prop.asking_price or prop.rent_price,
            'area': prop.area,
            'bedrooms': prop.bedrooms,
            'suites': prop.suites,
            'parking': prop.parking_spots,
            'url': f"https://pilarhomes.com.br/imovel/{prop.slug}",
            'images': prop.images[:3],  # Primeiras 3 imagens
            'exclusive': prop.is_exclusive
        })
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Exportado {len(data)} imóveis para {filename}")


def export_to_csv(properties: List[Property], filename: str):
    """Exporta imóveis para CSV"""
    import csv
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'ID', 'Tipo', 'Bairro', 'Cidade', 'Preço', 'Área m²',
            'Quartos', 'Suítes', 'Vagas', 'Condomínio', 'Exclusivo', 'URL'
        ])
        
        for prop in properties:
            writer.writerow([
                prop.commercial_id,
                prop.property_type,
                prop.region,
                prop.city,
                prop.asking_price or prop.rent_price or '',
                prop.area,
                prop.bedrooms,
                prop.suites,
                prop.parking_spots,
                prop.condo_fee or '',
                'Sim' if prop.is_exclusive else 'Não',
                f"https://pilarhomes.com.br/imovel/{prop.slug}"
            ])
    
    print(f"✅ Exportado {len(properties)} imóveis para {filename}")


# ============================================================================
# DEMO INTERATIVA
# ============================================================================

def demo():
    """Demonstração interativa do cliente"""
    print("=" * 60)
    print("🏠 PILAR HOMES API CLIENT - DEMO")
    print("=" * 60)
    
    api = PilarHomesAPI()
    
    # 1. Busca básica
    print("\n📌 1. Busca básica (primeiros 5 à venda)")
    print("-" * 40)
    
    result = api.search(transaction_type="sell", per_page=5)
    print(f"Total disponível: {result.total_count:,} imóveis")
    print(f"Mostrando página {result.page} de {result.total_pages}")
    
    for prop in result.properties:
        print(f"\n{format_property_card(prop)}")
    
    # 2. Busca com filtros
    print("\n" + "=" * 60)
    print("📌 2. Apartamentos até R$ 3M em São Paulo")
    print("-" * 40)
    
    result = api.search(
        transaction_type="sell",
        property_type="apartment",
        max_price=3000000,
        city="São Paulo",
        per_page=3
    )
    
    print(f"Encontrados: {result.total_count} apartamentos")
    for prop in result.properties:
        print(f"  • {prop.region}: {prop.format_price()} - {prop.area}m² - {prop.bedrooms}q")
    
    # 3. Casas
    print("\n" + "=" * 60)
    print("📌 3. Casas à venda")
    print("-" * 40)
    
    result = api.search(
        transaction_type="sell",
        property_type="house",
        per_page=3
    )
    
    print(f"Encontradas: {result.total_count} casas")
    for prop in result.properties:
        print(f"  • {prop.region}: {prop.format_price()} - {prop.area}m² - {prop.bedrooms}q")
    
    # 4. Aluguel
    print("\n" + "=" * 60)
    print("📌 4. Imóveis para aluguel")
    print("-" * 40)
    
    result = api.search(transaction_type="rent", per_page=3)
    print(f"Encontrados: {result.total_count} para alugar")
    for prop in result.properties:
        price = prop.rent_price or 0
        print(f"  • {prop.region}: R$ {price:,.0f}/mês - {prop.property_type}".replace(",", "."))
    
    # 5. Estatísticas
    print("\n" + "=" * 60)
    print("📊 ESTATÍSTICAS GERAIS")
    print("-" * 40)
    
    venda = api.search(transaction_type="sell", per_page=1)
    aluguel = api.search(transaction_type="rent", per_page=1)
    
    print(f"  📈 Total à venda:  {venda.total_count:,} imóveis")
    print(f"  📈 Total aluguel:  {aluguel.total_count:,} imóveis")
    print(f"  📈 Total geral:    {venda.total_count + aluguel.total_count:,} imóveis")
    
    # 6. Google Maps Key
    print("\n" + "=" * 60)
    print("🗺️ GOOGLE MAPS API")
    print("-" * 40)
    print(f"  Chave: {GOOGLE_MAPS_KEY}")
    print("  Uso: Incluir no HTML para renderizar mapas")
    
    print("\n" + "=" * 60)
    print("✅ Demo concluída!")
    print("=" * 60)


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    demo()
