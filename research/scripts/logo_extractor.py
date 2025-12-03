"""
Logo Extractor - Extrai logos de sites da rede Pilar
"""
import os
import re
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
from datetime import datetime

class LogoExtractor:
    def __init__(self, output_dir="logos_whitelabel"):
        self.output_dir = output_dir
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        self.results = []
        os.makedirs(output_dir, exist_ok=True)
    
    def extract_logo(self, domain):
        """Extrai logo de um domínio"""
        url = f"https://{domain}" if not domain.startswith('http') else domain
        domain_name = urlparse(url).netloc or domain
        
        print(f"  🔍 Processando: {domain_name}...")
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10, allow_redirects=True)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            logos_found = []
            
            # Estratégia 1: Tags <img> com 'logo' no src, class, id ou alt
            for img in soup.find_all('img'):
                src = img.get('src', '')
                alt = img.get('alt', '')
                cls = ' '.join(img.get('class', []))
                img_id = img.get('id', '')
                
                if any('logo' in attr.lower() for attr in [src, alt, cls, img_id]):
                    if src:
                        logos_found.append(('img-logo', urljoin(url, src)))
            
            # Estratégia 2: Links/divs com classe logo contendo img
            for container in soup.find_all(['a', 'div', 'span', 'header'], class_=re.compile(r'logo', re.I)):
                img = container.find('img')
                if img and img.get('src'):
                    logos_found.append(('container-logo', urljoin(url, img['src'])))
            
            # Estratégia 3: SVGs inline com logo
            for svg in soup.find_all('svg'):
                parent = svg.parent
                if parent:
                    parent_class = ' '.join(parent.get('class', []))
                    parent_id = parent.get('id', '')
                    if any('logo' in attr.lower() for attr in [parent_class, parent_id]):
                        # Salvar SVG inline
                        svg_content = str(svg)
                        svg_filename = f"{domain_name.replace('.', '_')}_inline.svg"
                        svg_path = os.path.join(self.output_dir, svg_filename)
                        with open(svg_path, 'w', encoding='utf-8') as f:
                            f.write(svg_content)
                        logos_found.append(('svg-inline', svg_path))
            
            # Estratégia 4: Meta tags (og:image, favicon)
            for meta in soup.find_all('meta', property='og:image'):
                content = meta.get('content')
                if content:
                    logos_found.append(('og-image', urljoin(url, content)))
            
            # Estratégia 5: Favicon
            for link in soup.find_all('link', rel=re.compile(r'icon', re.I)):
                href = link.get('href')
                if href:
                    logos_found.append(('favicon', urljoin(url, href)))
            
            # Baixar logos únicos
            downloaded = []
            seen_urls = set()
            
            for logo_type, logo_url in logos_found:
                if logo_url in seen_urls or logo_url.startswith(self.output_dir):
                    continue
                seen_urls.add(logo_url)
                
                try:
                    if logo_url.startswith('data:'):
                        # Base64 encoded
                        continue
                    
                    logo_response = requests.get(logo_url, headers=self.headers, timeout=10)
                    if logo_response.status_code == 200:
                        # Determinar extensão
                        content_type = logo_response.headers.get('Content-Type', '')
                        if 'svg' in content_type or logo_url.endswith('.svg'):
                            ext = '.svg'
                        elif 'png' in content_type or logo_url.endswith('.png'):
                            ext = '.png'
                        elif 'webp' in content_type or logo_url.endswith('.webp'):
                            ext = '.webp'
                        elif 'ico' in content_type or logo_url.endswith('.ico'):
                            ext = '.ico'
                        else:
                            ext = '.jpg'
                        
                        filename = f"{domain_name.replace('.', '_')}_{logo_type}{ext}"
                        filepath = os.path.join(self.output_dir, filename)
                        
                        with open(filepath, 'wb') as f:
                            f.write(logo_response.content)
                        
                        downloaded.append({
                            'type': logo_type,
                            'url': logo_url,
                            'file': filepath
                        })
                        print(f"    ✅ {logo_type}: {filename}")
                except Exception as e:
                    pass
            
            result = {
                'domain': domain_name,
                'status': 'success' if downloaded else 'no_logo_found',
                'logos': downloaded
            }
            self.results.append(result)
            return result
            
        except requests.exceptions.Timeout:
            print(f"    ⏱️ Timeout")
            result = {'domain': domain_name, 'status': 'timeout', 'logos': []}
            self.results.append(result)
            return result
        except requests.exceptions.RequestException as e:
            print(f"    ❌ Erro: {str(e)[:50]}")
            result = {'domain': domain_name, 'status': 'error', 'error': str(e), 'logos': []}
            self.results.append(result)
            return result
    
    def extract_batch(self, domains, delay=1):
        """Extrai logos de múltiplos domínios"""
        print(f"\n🚀 Iniciando extração de {len(domains)} domínios...")
        print(f"📁 Salvando em: {self.output_dir}/\n")
        
        success = 0
        failed = 0
        
        for i, domain in enumerate(domains, 1):
            print(f"[{i}/{len(domains)}] ", end="")
            result = self.extract_logo(domain)
            
            if result['status'] == 'success':
                success += 1
            else:
                failed += 1
            
            if delay > 0 and i < len(domains):
                time.sleep(delay)
        
        # Salvar relatório
        report = {
            'timestamp': datetime.now().isoformat(),
            'total': len(domains),
            'success': success,
            'failed': failed,
            'results': self.results
        }
        
        report_path = os.path.join(self.output_dir, 'extraction_report.json')
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n" + "="*50)
        print(f"📊 RELATÓRIO FINAL")
        print(f"="*50)
        print(f"✅ Sucesso: {success}")
        print(f"❌ Falhas: {failed}")
        print(f"📁 Logos salvos em: {self.output_dir}/")
        print(f"📋 Relatório: {report_path}")
        
        return report


# Lista dos 125 domínios da rede Pilar
DOMAINS = [
    # Sites Demo Pilar (3)
    "pilardemo1.com.br",
    "pilardemo2.com.br",
    "pilardemo3.com.br",
    
    # Whitelabels *homes.com.br (10)
    "avahomes.com.br",
    "eclathomes.com.br",
    "homesphere.com.br",
    "cmolarihomes.com.br",
    "mosaichomes.com.br",
    "pandorahomes.com.br",
    "iconhomes.com.br",
    "biafrancohomes.com.br",
    "augustahomes.com.br",
    "home2uimoveis.com.br",
    
    # Imobiliárias *imoveis.com.br (43)
    "zeroonzeimoveis.com.br",
    "casacarambolaimoveis.com.br",
    "vistaprimeimoveis.com.br",
    "cgimoveisespeciais.com.br",
    "casalomaimoveis.com.br",
    "pecanimoveis.com.br",
    "openimoveissp.com.br",
    "rximoveis.com.br",
    "area2imoveis.com.br",
    "zarahimoveis.com.br",
    "globalbrokersimoveis.com.br",
    "ccoliimoveis.com.br",
    "lilaximoveis.com.br",
    "casapessoaimoveis.com.br",
    "casalyraimoveis.com.br",
    "maisonclassiqueimoveis.com.br",
    "imoveismistral.com.br",
    "orosimoveis.com.br",
    "imoveslaper.com.br",
    "coimoveis.com.br",
    "emperiaimoveis.com.br",
    "axsimoveis.com.br",
    "fikaimoveis.com.br",
    "suagaleriadeimoveis.com.br",
    "lhimoveisdeluxo.com.br",
    "imoveisemfamilia.com.br",
    "zaraimoveis.com.br",
    "kasa7imoveis.com.br",
    "investemimoveis.com.br",
    "vizimoveis.com.br",
    "eduardocaderaimoveis.com.br",
    "gardeimoveis.com.br",
    "escorsinimoveis.com.br",
    "luferreiraimoveis.com.br",
    "imoveisavenidapaulista.com.br",
    "namaiimoveis.com.br",
    "sabiaimoveis.com.br",
    "imoveisbs.com.br",
    "urbanclassimoveis.com.br",
    "olhardecorretora.com.br",
    "mg2imov.com.br",
    "goinhome.com.br",
    "pitayaimoveis.com.br",
    
    # Brokers/Realty (35)
    "arzbrokers.com.br",
    "hausbrokers.com.br",
    "morobrokers.com.br",
    "enterbroker.com.br",
    "biafrancobrokers.com.br",
    "sampabrokers.com.br",
    "virtualrealty.com.br",
    "behomerealty.com.br",
    "rmproperties.com.br",
    "brandrealestate.com.br",
    "maximumre.com.br",
    "thelistproperties.com.br",
    "bestkey.com.br",
    "thekeyluxury.com.br",
    "batellisting.com",
    "tfcuradoria.com",
    "emmegroup.com.br",
    "valmendonca.com.br",
    "levav.com.br",
    "renatafarhud.com.br",
    "vilamoema.com.br",
    "linsnegociosimobiliarios.com.br",
    "andarx.com.br",
    "imobilliare.com.br",
    "triximob.com.br",
    "fjdhelomme.com.br",
    "barakgroup.com.br",
    "tatuapevip.com.br",
    "idurbana.com.br",
    "brossuacasa.com.br",
    "boutiquecaza.com.br",
    "aurasignatures.com.br",
    "casavalente.com.br",
    "casasbacanas.com.br",
    "morarsp.life",
    
    # Premium/Especializados (23)
    "acervoexclusivo.com.br",
    "galleriadeimoveis.com.br",
    "costacesarsp.com.br",
    "valsahomes.com.br",
    "yvahomes.com.br",
    "denisenojardins.com.br",
    "luxuryhome.com.br",
    "amenities.com.br",
    "laperconsultoria.com.br",
    "areadois.com.br",
    "mwconsultoria.com.br",
    # Principais sites
    "pilarhomes.com.br",
    "soupilar.com.br",
]

if __name__ == "__main__":
    print("="*60)
    print("🏠 LOGO EXTRACTOR - Rede Pilar Whitelabel")
    print("="*60)
    
    extractor = LogoExtractor("logos_whitelabel")
    extractor.extract_batch(DOMAINS, delay=0.5)
