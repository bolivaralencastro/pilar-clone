#!/usr/bin/env python3
"""
Social Media Data Extractor - Pilar Homes & Sou Pilar
Captura dados públicos das redes sociais das marcas Pilar.
"""

import requests
import json
import re
import time
from datetime import datetime
from urllib.parse import urljoin, urlparse
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from bs4 import BeautifulSoup

# Configuração de headers para simular navegador
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

@dataclass
class SocialProfile:
    """Representa um perfil de rede social."""
    platform: str
    username: str
    url: str
    display_name: Optional[str] = None
    bio: Optional[str] = None
    followers: Optional[str] = None
    following: Optional[str] = None
    posts_count: Optional[str] = None
    website: Optional[str] = None
    verified: bool = False
    profile_image: Optional[str] = None
    extra_data: Optional[Dict] = None
    status: str = "found"
    error: Optional[str] = None


class SocialMediaExtractor:
    """Extrator de dados de redes sociais."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.results: Dict[str, Dict[str, SocialProfile]] = {}
        
    def extract_from_website(self, url: str, brand_name: str) -> List[str]:
        """Extrai links de redes sociais de um website."""
        print(f"\n🌐 Analisando website: {url}")
        social_links = []
        
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Padrões de redes sociais
            social_patterns = {
                'instagram': r'instagram\.com/([^/?\s"\']+)',
                'facebook': r'facebook\.com/([^/?\s"\']+)',
                'linkedin': r'linkedin\.com/(company|in)/([^/?\s"\']+)',
                'youtube': r'youtube\.com/(@?[^/?\s"\']+|channel/[^/?\s"\']+)',
                'twitter': r'(twitter|x)\.com/([^/?\s"\']+)',
                'tiktok': r'tiktok\.com/@([^/?\s"\']+)',
                'pinterest': r'pinterest\.com/([^/?\s"\']+)',
                'whatsapp': r'wa\.me/(\d+)|whatsapp.*?(\d{10,})',
            }
            
            # Busca em links
            for link in soup.find_all('a', href=True):
                href = link['href'].lower()
                for platform, pattern in social_patterns.items():
                    if platform in href or (platform == 'twitter' and 'x.com' in href):
                        social_links.append(link['href'])
                        
            # Busca no HTML completo
            html_text = response.text
            for platform, pattern in social_patterns.items():
                matches = re.findall(pattern, html_text, re.IGNORECASE)
                for match in matches:
                    if isinstance(match, tuple):
                        match = '/'.join(filter(None, match))
                    if match and match not in ['share', 'sharer', 'intent', 'dialog']:
                        if platform == 'instagram':
                            social_links.append(f'https://instagram.com/{match}')
                        elif platform == 'facebook':
                            social_links.append(f'https://facebook.com/{match}')
                        elif platform == 'linkedin':
                            social_links.append(f'https://linkedin.com/{match}')
                        elif platform == 'youtube':
                            social_links.append(f'https://youtube.com/{match}')
                        elif platform in ['twitter', 'x']:
                            social_links.append(f'https://x.com/{match}')
                        elif platform == 'tiktok':
                            social_links.append(f'https://tiktok.com/@{match}')
                            
            # Remove duplicatas mantendo ordem
            seen = set()
            unique_links = []
            for link in social_links:
                normalized = link.lower().rstrip('/')
                if normalized not in seen:
                    seen.add(normalized)
                    unique_links.append(link)
                    
            print(f"   ✅ Encontrados {len(unique_links)} links de redes sociais")
            return unique_links
            
        except Exception as e:
            print(f"   ❌ Erro ao analisar website: {e}")
            return []
    
    def get_instagram_data(self, username: str) -> SocialProfile:
        """Extrai dados públicos do Instagram."""
        print(f"   📸 Instagram: @{username}")
        url = f"https://www.instagram.com/{username}/"
        
        profile = SocialProfile(
            platform="instagram",
            username=username,
            url=url
        )
        
        try:
            response = self.session.get(url, timeout=15)
            
            if response.status_code == 404:
                profile.status = "not_found"
                profile.error = "Perfil não encontrado"
                return profile
                
            if response.status_code != 200:
                profile.status = "error"
                profile.error = f"Status code: {response.status_code}"
                return profile
            
            html = response.text
            
            # Tenta extrair dados do meta tags
            soup = BeautifulSoup(html, 'html.parser')
            
            # Título geralmente contém nome e username
            title = soup.find('title')
            if title:
                title_text = title.get_text()
                # Padrão: "Nome (@username) • Instagram photos and videos"
                name_match = re.search(r'^([^(]+)\s*\(@', title_text)
                if name_match:
                    profile.display_name = name_match.group(1).strip()
            
            # Meta description contém bio e contagens
            meta_desc = soup.find('meta', {'name': 'description'}) or soup.find('meta', {'property': 'og:description'})
            if meta_desc and meta_desc.get('content'):
                desc = meta_desc['content']
                profile.bio = desc
                
                # Extrai números (seguidores, seguindo, posts)
                numbers = re.findall(r'([\d,.]+[KMB]?)\s*(Followers|Following|Posts|Seguidores|Seguindo|Publicações)', desc, re.IGNORECASE)
                for num, label in numbers:
                    label_lower = label.lower()
                    if 'follower' in label_lower or 'seguidor' in label_lower:
                        profile.followers = num
                    elif 'following' in label_lower or 'seguindo' in label_lower:
                        profile.following = num
                    elif 'post' in label_lower or 'publicaç' in label_lower:
                        profile.posts_count = num
            
            # Imagem de perfil
            og_image = soup.find('meta', {'property': 'og:image'})
            if og_image:
                profile.profile_image = og_image.get('content')
            
            # Verifica selo de verificado
            if 'verified' in html.lower() or '✓' in html:
                profile.verified = True
                
            profile.status = "success"
            print(f"      ✅ Dados extraídos: {profile.followers or '?'} seguidores")
            
        except requests.exceptions.Timeout:
            profile.status = "timeout"
            profile.error = "Timeout na requisição"
        except Exception as e:
            profile.status = "error"
            profile.error = str(e)
            print(f"      ⚠️ Erro: {e}")
            
        return profile
    
    def get_facebook_data(self, page_name: str) -> SocialProfile:
        """Extrai dados públicos do Facebook."""
        print(f"   📘 Facebook: {page_name}")
        url = f"https://www.facebook.com/{page_name}"
        
        profile = SocialProfile(
            platform="facebook",
            username=page_name,
            url=url
        )
        
        try:
            response = self.session.get(url, timeout=15)
            
            if response.status_code != 200:
                profile.status = "error" if response.status_code != 404 else "not_found"
                profile.error = f"Status code: {response.status_code}"
                return profile
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Título da página
            title = soup.find('title')
            if title:
                profile.display_name = title.get_text().replace(' | Facebook', '').strip()
            
            # Meta description
            meta_desc = soup.find('meta', {'name': 'description'}) or soup.find('meta', {'property': 'og:description'})
            if meta_desc:
                profile.bio = meta_desc.get('content')
                
            # Imagem
            og_image = soup.find('meta', {'property': 'og:image'})
            if og_image:
                profile.profile_image = og_image.get('content')
                
            profile.status = "success"
            print(f"      ✅ Página encontrada: {profile.display_name or page_name}")
            
        except Exception as e:
            profile.status = "error"
            profile.error = str(e)
            print(f"      ⚠️ Erro: {e}")
            
        return profile
    
    def get_linkedin_data(self, company_slug: str, is_company: bool = True) -> SocialProfile:
        """Extrai dados públicos do LinkedIn."""
        print(f"   💼 LinkedIn: {company_slug}")
        
        if is_company:
            url = f"https://www.linkedin.com/company/{company_slug}"
        else:
            url = f"https://www.linkedin.com/in/{company_slug}"
        
        profile = SocialProfile(
            platform="linkedin",
            username=company_slug,
            url=url
        )
        
        try:
            response = self.session.get(url, timeout=15, allow_redirects=True)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = soup.find('title')
            if title:
                profile.display_name = title.get_text().replace(' | LinkedIn', '').strip()
            
            meta_desc = soup.find('meta', {'name': 'description'})
            if meta_desc:
                profile.bio = meta_desc.get('content')
                
            og_image = soup.find('meta', {'property': 'og:image'})
            if og_image:
                profile.profile_image = og_image.get('content')
                
            profile.status = "success"
            print(f"      ✅ Empresa encontrada: {profile.display_name or company_slug}")
            
        except Exception as e:
            profile.status = "error"
            profile.error = str(e)
            print(f"      ⚠️ Erro: {e}")
            
        return profile
    
    def get_youtube_data(self, channel: str) -> SocialProfile:
        """Extrai dados públicos do YouTube."""
        print(f"   📺 YouTube: {channel}")
        
        if channel.startswith('@'):
            url = f"https://www.youtube.com/{channel}"
        elif channel.startswith('channel/'):
            url = f"https://www.youtube.com/{channel}"
        else:
            url = f"https://www.youtube.com/@{channel}"
        
        profile = SocialProfile(
            platform="youtube",
            username=channel,
            url=url
        )
        
        try:
            response = self.session.get(url, timeout=15)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = soup.find('title')
            if title:
                profile.display_name = title.get_text().replace(' - YouTube', '').strip()
            
            meta_desc = soup.find('meta', {'name': 'description'})
            if meta_desc:
                profile.bio = meta_desc.get('content')
            
            # Tenta extrair contagem de inscritos do HTML
            html = response.text
            subs_match = re.search(r'"subscriberCountText":\s*{\s*"simpleText":\s*"([^"]+)"', html)
            if subs_match:
                profile.followers = subs_match.group(1)
                
            profile.status = "success"
            print(f"      ✅ Canal encontrado: {profile.display_name or channel}")
            
        except Exception as e:
            profile.status = "error"
            profile.error = str(e)
            print(f"      ⚠️ Erro: {e}")
            
        return profile
    
    def get_twitter_data(self, username: str) -> SocialProfile:
        """Extrai dados públicos do Twitter/X."""
        print(f"   🐦 Twitter/X: @{username}")
        url = f"https://x.com/{username}"
        
        profile = SocialProfile(
            platform="twitter",
            username=username,
            url=url
        )
        
        try:
            response = self.session.get(url, timeout=15)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = soup.find('title')
            if title:
                title_text = title.get_text()
                name_match = re.search(r'^([^(]+)\s*\(@', title_text)
                if name_match:
                    profile.display_name = name_match.group(1).strip()
            
            meta_desc = soup.find('meta', {'name': 'description'})
            if meta_desc:
                profile.bio = meta_desc.get('content')
                
            profile.status = "success"
            print(f"      ✅ Perfil encontrado")
            
        except Exception as e:
            profile.status = "error"
            profile.error = str(e)
            print(f"      ⚠️ Erro: {e}")
            
        return profile
    
    def get_tiktok_data(self, username: str) -> SocialProfile:
        """Extrai dados públicos do TikTok."""
        print(f"   🎵 TikTok: @{username}")
        url = f"https://www.tiktok.com/@{username}"
        
        profile = SocialProfile(
            platform="tiktok",
            username=username,
            url=url
        )
        
        try:
            response = self.session.get(url, timeout=15)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = soup.find('title')
            if title:
                profile.display_name = title.get_text().replace(' | TikTok', '').strip()
            
            meta_desc = soup.find('meta', {'name': 'description'})
            if meta_desc:
                profile.bio = meta_desc.get('content')
                
            profile.status = "success"
            print(f"      ✅ Perfil encontrado: {profile.display_name or username}")
            
        except Exception as e:
            profile.status = "error"
            profile.error = str(e)
            print(f"      ⚠️ Erro: {e}")
            
        return profile


def extract_pilar_social_media():
    """Extrai dados de redes sociais das marcas Pilar."""
    
    print("="*60)
    print("🏠 EXTRATOR DE REDES SOCIAIS - PILAR HOMES & SOU PILAR")
    print("="*60)
    print(f"📅 Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    extractor = SocialMediaExtractor()
    
    # Definição das marcas e suas redes sociais conhecidas/suspeitas
    brands = {
        "Pilar Homes": {
            "website": "https://pilarhomes.com.br",
            "known_socials": {
                "instagram": ["pilarhomes_", "pilarhomes", "pilar.homes"],
                "facebook": ["pilarhomes", "pilarhomesbr"],
                "linkedin": ["pilar-homes", "pilarhomes"],
                "youtube": ["pilarhomes", "@pilarhomes"],
                "tiktok": ["pilarhomes", "pilarhomes_"],
            }
        },
        "Sou Pilar": {
            "website": "https://soupilar.com.br",
            "known_socials": {
                "instagram": ["soupilar", "sou.pilar", "soupilar_"],
                "facebook": ["soupilar", "soupilarbr"],
                "linkedin": ["sou-pilar", "soupilar"],
                "youtube": ["soupilar", "@soupilar"],
                "tiktok": ["soupilar"],
            }
        }
    }
    
    results = {}
    
    for brand_name, brand_data in brands.items():
        print(f"\n{'='*60}")
        print(f"🏢 MARCA: {brand_name}")
        print(f"{'='*60}")
        
        results[brand_name] = {
            "website": brand_data["website"],
            "extracted_at": datetime.now().isoformat(),
            "social_links_from_website": [],
            "profiles": {}
        }
        
        # 1. Extrai links do website
        website_links = extractor.extract_from_website(
            brand_data["website"], 
            brand_name
        )
        results[brand_name]["social_links_from_website"] = website_links
        
        # 2. Testa perfis conhecidos/suspeitos
        print(f"\n🔍 Verificando perfis nas redes sociais...")
        
        for platform, usernames in brand_data["known_socials"].items():
            for username in usernames:
                time.sleep(0.5)  # Rate limiting
                
                if platform == "instagram":
                    profile = extractor.get_instagram_data(username)
                elif platform == "facebook":
                    profile = extractor.get_facebook_data(username)
                elif platform == "linkedin":
                    profile = extractor.get_linkedin_data(username)
                elif platform == "youtube":
                    profile = extractor.get_youtube_data(username)
                elif platform == "twitter":
                    profile = extractor.get_twitter_data(username)
                elif platform == "tiktok":
                    profile = extractor.get_tiktok_data(username)
                else:
                    continue
                
                # Guarda apenas perfis encontrados ou o primeiro testado
                key = f"{platform}_{username}"
                if profile.status == "success":
                    results[brand_name]["profiles"][key] = asdict(profile)
                    break  # Encontrou, não precisa testar outros usernames
    
    return results


def generate_markdown_report(results: Dict) -> str:
    """Gera relatório em Markdown."""
    
    md = []
    md.append("# 📱 Relatório de Redes Sociais - Grupo Pilar")
    md.append(f"\n**Data de Extração:** {datetime.now().strftime('%d/%m/%Y às %H:%M')}")
    md.append("\n---\n")
    
    for brand_name, brand_data in results.items():
        md.append(f"## 🏢 {brand_name}")
        md.append(f"\n**Website:** [{brand_data['website']}]({brand_data['website']})")
        
        # Links encontrados no website
        if brand_data.get("social_links_from_website"):
            md.append("\n### 🔗 Links de Redes Sociais no Website")
            for link in brand_data["social_links_from_website"]:
                md.append(f"- {link}")
        
        # Perfis verificados
        if brand_data.get("profiles"):
            md.append("\n### 📊 Perfis Verificados")
            md.append("")
            
            # Agrupa por plataforma
            platforms = {}
            for key, profile in brand_data["profiles"].items():
                plat = profile["platform"]
                if plat not in platforms:
                    platforms[plat] = []
                platforms[plat].append(profile)
            
            # Ícones por plataforma
            icons = {
                "instagram": "📸",
                "facebook": "📘",
                "linkedin": "💼",
                "youtube": "📺",
                "twitter": "🐦",
                "tiktok": "🎵",
            }
            
            for platform, profiles in platforms.items():
                icon = icons.get(platform, "🔗")
                md.append(f"\n#### {icon} {platform.title()}")
                
                for profile in profiles:
                    md.append(f"\n**Perfil:** [@{profile['username']}]({profile['url']})")
                    
                    if profile.get("display_name"):
                        md.append(f"- **Nome:** {profile['display_name']}")
                    if profile.get("followers"):
                        md.append(f"- **Seguidores:** {profile['followers']}")
                    if profile.get("following"):
                        md.append(f"- **Seguindo:** {profile['following']}")
                    if profile.get("posts_count"):
                        md.append(f"- **Posts:** {profile['posts_count']}")
                    if profile.get("bio"):
                        bio = profile['bio'][:200] + "..." if len(profile['bio']) > 200 else profile['bio']
                        md.append(f"- **Bio:** {bio}")
                    if profile.get("verified"):
                        md.append(f"- **Verificado:** ✅ Sim")
                    if profile.get("website"):
                        md.append(f"- **Website:** {profile['website']}")
                    md.append("")
        
        md.append("\n---\n")
    
    # Resumo
    md.append("## 📈 Resumo Geral")
    md.append("")
    md.append("| Marca | Plataforma | Username | Seguidores | Status |")
    md.append("|-------|------------|----------|------------|--------|")
    
    for brand_name, brand_data in results.items():
        for key, profile in brand_data.get("profiles", {}).items():
            status = "✅" if profile["status"] == "success" else "❌"
            followers = profile.get("followers", "N/A")
            md.append(f"| {brand_name} | {profile['platform'].title()} | @{profile['username']} | {followers} | {status} |")
    
    md.append("\n---\n")
    md.append("## 🔍 Metodologia")
    md.append("""
Este relatório foi gerado através de:
1. Análise do HTML dos websites oficiais para identificar links de redes sociais
2. Verificação de usernames prováveis em cada plataforma
3. Extração de metadados públicos (título, descrição, contagens)

**Nota:** Os dados de seguidores e métricas são aproximados e baseados em informações públicas disponíveis.
""")
    
    return "\n".join(md)


def main():
    """Função principal."""
    
    # Extrai dados
    results = extract_pilar_social_media()
    
    # Salva JSON
    json_file = "social_media_pilar.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n💾 Dados salvos em: {json_file}")
    
    # Gera relatório Markdown
    md_report = generate_markdown_report(results)
    md_file = "SOCIAL_MEDIA_PILAR.md"
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_report)
    print(f"📄 Relatório salvo em: {md_file}")
    
    # Exibe resumo
    print("\n" + "="*60)
    print("✅ EXTRAÇÃO CONCLUÍDA!")
    print("="*60)
    
    total_profiles = sum(
        len(brand.get("profiles", {})) 
        for brand in results.values()
    )
    print(f"📊 Total de perfis encontrados: {total_profiles}")
    print(f"📁 Arquivos gerados:")
    print(f"   - {json_file} (dados estruturados)")
    print(f"   - {md_file} (relatório formatado)")


if __name__ == "__main__":
    main()
