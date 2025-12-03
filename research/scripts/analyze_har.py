#!/usr/bin/env python3
"""
HAR File Analyzer - Extrai informações de marketing e infraestrutura
"""

import json
from collections import defaultdict
from urllib.parse import urlparse
import re

def analyze_har(filepath):
    """Analisa arquivo HAR e extrai informações relevantes."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        har = json.load(f)
    
    entries = har.get('log', {}).get('entries', [])
    
    print(f"📊 ANÁLISE DO ARQUIVO HAR - pilarhomes.com.br")
    print(f"{'='*60}")
    print(f"Total de requisições: {len(entries)}")
    print()
    
    # Categorias de análise
    domains = defaultdict(lambda: {'count': 0, 'size': 0, 'types': set()})
    apis = []
    tracking_pixels = []
    third_party_services = []
    cookies_all = []
    headers_security = {}
    content_types = defaultdict(int)
    
    # Padrões para identificar serviços
    tracking_patterns = {
        'google-analytics': 'Google Analytics',
        'googletagmanager': 'Google Tag Manager',
        'facebook.com/tr': 'Facebook Pixel',
        'facebook.net': 'Facebook SDK',
        'connect.facebook': 'Facebook Connect',
        'hotjar': 'Hotjar',
        'clarity.ms': 'Microsoft Clarity',
        'tiktok': 'TikTok Pixel',
        'taboola': 'Taboola',
        'doubleclick': 'DoubleClick',
        'googlesyndication': 'Google Ads',
        'googleadservices': 'Google Ads Conversion',
        'datadoghq': 'Datadog',
        'clickcease': 'ClickCease',
        'amplitude': 'Amplitude',
        'segment': 'Segment',
        'mixpanel': 'Mixpanel',
        'intercom': 'Intercom',
        'zendesk': 'Zendesk',
        'hubspot': 'HubSpot',
        'linkedin': 'LinkedIn',
        'twitter': 'Twitter/X',
        'pinterest': 'Pinterest',
        'snapchat': 'Snapchat',
    }
    
    cdn_patterns = {
        'cloudfront': 'Amazon CloudFront',
        'amazonaws': 'AWS',
        'cloudflare': 'Cloudflare',
        'akamai': 'Akamai',
        'fastly': 'Fastly',
        'gstatic': 'Google Static',
        'googleapis': 'Google APIs',
    }
    
    for entry in entries:
        request = entry.get('request', {})
        response = entry.get('response', {})
        
        url = request.get('url', '')
        parsed = urlparse(url)
        domain = parsed.netloc
        
        # Tamanho da resposta
        size = response.get('content', {}).get('size', 0) or 0
        
        # Content type
        content_type = response.get('content', {}).get('mimeType', 'unknown')
        content_types[content_type.split(';')[0]] += 1
        
        # Agrupa por domínio
        domains[domain]['count'] += 1
        domains[domain]['size'] += size
        domains[domain]['types'].add(content_type.split(';')[0])
        
        # Identifica APIs
        if '/api/' in url or 'api.' in domain:
            apis.append({
                'url': url[:150],
                'method': request.get('method'),
                'status': response.get('status'),
            })
        
        # Identifica tracking/pixels
        url_lower = url.lower()
        for pattern, name in tracking_patterns.items():
            if pattern in url_lower:
                tracking_pixels.append({
                    'service': name,
                    'url': url[:100],
                    'domain': domain
                })
                break
        
        # Identifica CDNs
        for pattern, name in cdn_patterns.items():
            if pattern in domain.lower():
                third_party_services.append({
                    'service': name,
                    'domain': domain,
                    'type': 'CDN/Cloud'
                })
                break
        
        # Cookies
        for cookie in response.get('cookies', []):
            cookies_all.append({
                'name': cookie.get('name'),
                'domain': cookie.get('domain', domain),
                'httpOnly': cookie.get('httpOnly', False),
                'secure': cookie.get('secure', False),
            })
        
        # Headers de segurança (apenas do domínio principal)
        if 'pilarhomes.com.br' in domain and not headers_security:
            for header in response.get('headers', []):
                name = header.get('name', '').lower()
                if name in ['content-security-policy', 'x-frame-options', 
                           'x-content-type-options', 'strict-transport-security',
                           'x-xss-protection', 'referrer-policy', 'permissions-policy']:
                    headers_security[name] = header.get('value', '')[:100]
    
    # ===== RELATÓRIO =====
    
    print("\n" + "="*60)
    print("🌐 TOP 20 DOMÍNIOS POR NÚMERO DE REQUISIÇÕES")
    print("="*60)
    sorted_domains = sorted(domains.items(), key=lambda x: x[1]['count'], reverse=True)[:20]
    print(f"{'Domínio':<45} {'Reqs':>6} {'Size':>10}")
    print("-"*65)
    for domain, data in sorted_domains:
        size_kb = data['size'] / 1024
        print(f"{domain[:44]:<45} {data['count']:>6} {size_kb:>8.1f}KB")
    
    print("\n" + "="*60)
    print("📊 SERVIÇOS DE TRACKING/ANALYTICS IDENTIFICADOS")
    print("="*60)
    tracking_unique = {}
    for t in tracking_pixels:
        if t['service'] not in tracking_unique:
            tracking_unique[t['service']] = {'count': 0, 'domains': set()}
        tracking_unique[t['service']]['count'] += 1
        tracking_unique[t['service']]['domains'].add(t['domain'])
    
    for service, data in sorted(tracking_unique.items(), key=lambda x: x[1]['count'], reverse=True):
        print(f"✅ {service}: {data['count']} requisições")
        for d in list(data['domains'])[:2]:
            print(f"   └─ {d}")
    
    print("\n" + "="*60)
    print("🔌 APIs IDENTIFICADAS")
    print("="*60)
    api_domains = set()
    for api in apis[:30]:
        domain = urlparse(api['url']).netloc
        if domain not in api_domains:
            api_domains.add(domain)
            print(f"• {domain}")
            print(f"  {api['method']} {api['url'][:80]}...")
            print(f"  Status: {api['status']}")
    
    print("\n" + "="*60)
    print("🍪 COOKIES IDENTIFICADOS")
    print("="*60)
    cookie_names = set()
    for c in cookies_all:
        if c['name'] and c['name'] not in cookie_names:
            cookie_names.add(c['name'])
            secure = "🔒" if c['secure'] else "⚠️"
            http = "HTTP" if c['httpOnly'] else "JS"
            print(f"{secure} {c['name'][:30]:<32} ({c['domain']}) [{http}]")
    
    print("\n" + "="*60)
    print("🔒 HEADERS DE SEGURANÇA")
    print("="*60)
    security_headers_expected = [
        'content-security-policy',
        'x-frame-options', 
        'x-content-type-options',
        'strict-transport-security',
        'x-xss-protection',
        'referrer-policy',
        'permissions-policy'
    ]
    for header in security_headers_expected:
        if header in headers_security:
            print(f"✅ {header}: {headers_security[header][:60]}...")
        else:
            print(f"❌ {header}: NÃO CONFIGURADO")
    
    print("\n" + "="*60)
    print("📦 TIPOS DE CONTEÚDO")
    print("="*60)
    for ctype, count in sorted(content_types.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"{count:>4}x  {ctype}")
    
    # Salva resumo em JSON
    summary = {
        'total_requests': len(entries),
        'domains': {k: {'count': v['count'], 'size_kb': v['size']/1024} 
                   for k, v in sorted_domains},
        'tracking_services': list(tracking_unique.keys()),
        'api_domains': list(api_domains),
        'cookies': list(cookie_names),
        'security_headers': headers_security,
        'content_types': dict(content_types),
    }
    
    with open('har_analysis_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print("\n" + "="*60)
    print("💾 Resumo salvo em: har_analysis_summary.json")
    print("="*60)
    
    return summary


if __name__ == "__main__":
    analyze_har("pilarhomes_radar.har")
