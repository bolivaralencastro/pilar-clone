# PilarHomes - Extracted Assets
## Design Tokens, API Endpoints e CSS para Protótipo Vercel

**Data de Extração**: 3 de Dezembro de 2025  
**Fonte**: https://pilarhomes.com.br  
**Método**: HTTP extraction + documentação manual

---

## 📁 Estrutura de Arquivos

```
extracted/
├── api/
│   ├── endpoints-map.json         # Endpoints básicos (JSON)
│   └── API_ENDPOINTS_MAP.md       # Documentação completa da API
├── css/
│   ├── style_1.css                # CSS extraído do site (parte 1)
│   ├── style_2.css                # CSS extraído do site (parte 2)
│   ├── style_3.css                # CSS extraído do site (parte 3)
│   └── combined.css               # Todos os CSS combinados
├── tokens/
│   ├── design-tokens.json         # Tokens básicos (auto-extraídos)
│   ├── design-tokens-complete.json # Tokens completos (curados)
│   ├── tokens.css                 # CSS Variables prontos para uso
│   └── tokens.ts                  # TypeScript module com tipos
└── index.html                     # HTML da homepage (referência)
```

---

## 🚀 Como Usar no Protótipo Vercel

### 1. Importar Design Tokens

#### Opção A: CSS Variables (Recomendado para Next.js)

```css
/* app/globals.css ou styles/globals.css */
@import url('./extracted/tokens/tokens.css');

/* Agora você pode usar: */
body {
  font-family: var(--font-family-primary);
  color: var(--color-text-primary);
  background: var(--color-background);
}

.button {
  background: var(--color-primary-black);
  color: var(--color-neutral-white);
  padding: var(--spacing-4) var(--spacing-6);
  border-radius: var(--radius-md);
  transition: var(--transition-fast);
}
```

#### Opção B: TypeScript/JavaScript Module

```typescript
// lib/tokens.ts ou utils/design-tokens.ts
import tokens from './extracted/tokens/tokens';

export const Button = styled.button`
  font-family: ${tokens.typography.fontFamily.primary};
  font-size: ${tokens.typography.fontSize.base};
  padding: ${tokens.spacing[4]} ${tokens.spacing[6]};
  background: ${tokens.colors.primary.black};
  color: ${tokens.colors.neutral.white};
  border-radius: ${tokens.borderRadius.md};
  transition: all ${tokens.transitions.duration.fast} ${tokens.transitions.timing.default};
`;
```

#### Opção C: Tailwind CSS Config

```javascript
// tailwind.config.js
const tokens = require('./extracted/tokens/design-tokens-complete.json');

module.exports = {
  theme: {
    extend: {
      colors: {
        primary: tokens.colors.primary.black.hex,
        beige: tokens.colors.accent.beige.hex,
        gray: {
          100: '#f0f0f0',
          200: '#e0e0e0',
          400: '#aaaaaa',
          600: '#6d6d6d',
        },
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      spacing: tokens.spacing.scale,
      borderRadius: tokens.borderRadius,
      boxShadow: tokens.shadows,
    },
  },
};
```

---

### 2. Configurar API Client

```typescript
// lib/api-client.ts
const API_BASE = 'https://api.pilarhomes.com.br';
const CDN_IMAGES = 'https://imagens.pilarhomes.com.br';
const CDN_STATIC = 'https://static.pilarhomes.com.br';

export const apiClient = {
  // Listar propriedades
  getProperties: async (params?: {
    page?: number;
    perPage?: number;
    city?: string;
    minPrice?: number;
    maxPrice?: number;
    isExclusive?: boolean;
  }) => {
    const query = new URLSearchParams(params as any).toString();
    const res = await fetch(`${API_BASE}/properties?${query}`);
    return res.json();
  },

  // Buscar propriedade por ID
  getProperty: async (id: string) => {
    const res = await fetch(`${API_BASE}/properties/${id}`);
    return res.json();
  },

  // Listar corretores
  getAgents: async (companyId?: string) => {
    const query = companyId ? `?companyId=${companyId}` : '';
    const res = await fetch(`${API_BASE}/agents${query}`);
    return res.json();
  },

  // Listar boutiques
  getCompanies: async () => {
    const res = await fetch(`${API_BASE}/companies`);
    return res.json();
  },

  // Helper para URLs de imagens
  getImageUrl: (path: string) => `${CDN_IMAGES}/${path}`,
};
```

---

### 3. Estrutura de Componentes Sugerida

```
components/
├── ui/
│   ├── Button.tsx          # Usa tokens.colors, tokens.spacing
│   ├── Card.tsx            # Usa tokens.shadows, tokens.borderRadius
│   ├── Input.tsx           # Usa tokens.colors, tokens.typography
│   └── Badge.tsx           # Para "Exclusivo PilarHomes"
├── property/
│   ├── PropertyCard.tsx    # Card de imóvel
│   ├── PropertyGrid.tsx    # Grid de imóveis
│   ├── PropertyDetail.tsx  # Página de detalhes
│   └── PropertyFilters.tsx # Filtros de busca
├── agent/
│   ├── AgentCard.tsx       # Card de corretor
│   └── AgentProfile.tsx    # Perfil completo
└── layout/
    ├── Header.tsx          # Logo PilarHomes + menu
    ├── Footer.tsx          # Links + contatos
    └── Layout.tsx          # Wrapper geral
```

---

### 4. Exemplo de Componente PropertyCard

```typescript
// components/property/PropertyCard.tsx
import tokens from '@/lib/tokens';
import Image from 'next/image';

interface PropertyCardProps {
  property: {
    id: string;
    title: string;
    type: string;
    price: number;
    area: number;
    rooms: number;
    suites: number;
    parkingSpaces: number;
    isExclusive: boolean;
    images: string[];
    address: {
      neighborhood: string;
      city: string;
      state: string;
    };
    agent: {
      name: string;
      profilePicture: string;
    };
    company: {
      name: string;
      logo: string;
    };
  };
}

export const PropertyCard = ({ property }: PropertyCardProps) => {
  return (
    <div
      style={{
        borderRadius: tokens.borderRadius.md,
        boxShadow: tokens.shadows.base,
        overflow: 'hidden',
        transition: `all ${tokens.transitions.duration.fast} ${tokens.transitions.timing.default}`,
      }}
      className="hover:shadow-lg"
    >
      {/* Imagem */}
      <div className="relative h-64">
        <Image
          src={property.images[0]}
          alt={property.title}
          fill
          className="object-cover"
        />
        {property.isExclusive && (
          <div
            style={{
              position: 'absolute',
              top: tokens.spacing[4],
              left: tokens.spacing[4],
              background: tokens.colors.accent.beige,
              color: tokens.colors.primary.black,
              padding: `${tokens.spacing[2]} ${tokens.spacing[4]}`,
              borderRadius: tokens.borderRadius.pill,
              fontSize: tokens.typography.fontSize.sm,
              fontWeight: tokens.typography.fontWeight.semibold,
            }}
          >
            Exclusivo PilarHomes
          </div>
        )}
      </div>

      {/* Conteúdo */}
      <div style={{ padding: tokens.spacing[6] }}>
        <h3
          style={{
            fontSize: tokens.typography.fontSize.xl,
            fontWeight: tokens.typography.fontWeight.semibold,
            color: tokens.colors.semantic.textPrimary,
            marginBottom: tokens.spacing[2],
          }}
        >
          {property.type} {property.rooms} quartos
        </h3>

        <p
          style={{
            fontSize: tokens.typography.fontSize.sm,
            color: tokens.colors.semantic.textSecondary,
            marginBottom: tokens.spacing[4],
          }}
        >
          {property.address.neighborhood}, {property.address.city} - {property.address.state}
        </p>

        <div style={{ marginBottom: tokens.spacing[4] }}>
          <span
            style={{
              fontSize: tokens.typography.fontSize['2xl'],
              fontWeight: tokens.typography.fontWeight.bold,
              color: tokens.colors.primary.black,
            }}
          >
            R$ {(property.price / 1000000).toFixed(2)}M
          </span>
        </div>

        <div
          style={{
            display: 'flex',
            gap: tokens.spacing[4],
            fontSize: tokens.typography.fontSize.sm,
            color: tokens.colors.semantic.textMuted,
          }}
        >
          <span>{property.area}m²</span>
          <span>•</span>
          <span>{property.rooms} quartos</span>
          <span>•</span>
          <span>{property.suites} suítes</span>
          <span>•</span>
          <span>{property.parkingSpaces} vagas</span>
        </div>

        {/* Corretor */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: tokens.spacing[3],
            marginTop: tokens.spacing[6],
            paddingTop: tokens.spacing[6],
            borderTop: `1px solid ${tokens.colors.semantic.border}`,
          }}
        >
          <Image
            src={property.agent.profilePicture}
            alt={property.agent.name}
            width={32}
            height={32}
            className="rounded-full"
          />
          <div>
            <p
              style={{
                fontSize: tokens.typography.fontSize.sm,
                fontWeight: tokens.typography.fontWeight.medium,
              }}
            >
              {property.agent.name}
            </p>
            <p
              style={{
                fontSize: tokens.typography.fontSize.xs,
                color: tokens.colors.semantic.textMuted,
              }}
            >
              {property.company.name}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
```

---

## 📊 Dados de Exemplo (Mock)

Use os dados extraídos em `DADOS_COMPLETOS_PILARHOMES.md` para criar mocks:

```typescript
// lib/mock-data.ts
export const mockProperties = [
  {
    id: 'HS27071',
    title: 'Apartamento de luxo no Itaim Bibi',
    type: 'Apartamento',
    price: 43980000,
    area: 554,
    rooms: 3,
    suites: 3,
    parkingSpaces: 6,
    isExclusive: true,
    images: ['https://placehold.co/800x600/ddc79f/000000?text=Apartamento+Luxo'],
    address: {
      neighborhood: 'Itaim Bibi',
      city: 'São Paulo',
      state: 'SP',
    },
    agent: {
      name: 'Thiago Granato',
      profilePicture: 'https://placehold.co/100x100/000000/ffffff?text=TG',
    },
    company: {
      name: 'Homesphere',
      logo: 'https://placehold.co/200x50/000000/ffffff?text=Homesphere',
    },
  },
  // ... adicionar mais 30 propriedades dos dados extraídos
];
```

---

## 🎨 Checklist de Design System

- [ ] Importar `tokens.css` no projeto
- [ ] Configurar Tailwind com tokens (se usar)
- [ ] Criar componentes UI básicos (Button, Card, Input)
- [ ] Garantir tipografia Inter (importar do Google Fonts)
- [ ] Implementar cores (#000 primary, #ddc79f beige)
- [ ] Aplicar border-radius corretos (8px cards, 9999px pills)
- [ ] Usar transições de 0.15s
- [ ] Não usar emojis (marca de luxo)
- [ ] Implementar responsive breakpoints
- [ ] Testar acessibilidade (contraste de cores)

---

## 🔗 Links Importantes

- **Site Original**: https://pilarhomes.com.br
- **Exemplo White-Label**: https://costacesarsp.com.br
- **API Base**: https://api.pilarhomes.com.br
- **CDN Imagens**: https://imagens.pilarhomes.com.br
- **Documentação Completa**: Ver `DESIGN_SYSTEM_PILARHOMES.md`

---

## 📝 Próximos Passos

### Setup Inicial (Vercel)
```bash
# Criar projeto Next.js
npx create-next-app@latest pilarhomes-prototype --typescript --tailwind --app

# Copiar arquivos extraídos
cp -r extracted/ pilarhomes-prototype/public/
cp extracted/tokens/tokens.ts pilarhomes-prototype/lib/
cp extracted/tokens/tokens.css pilarhomes-prototype/styles/

# Instalar dependências adicionais
cd pilarhomes-prototype
npm install lucide-react # Para ícones
```

### Estrutura Sugerida
```
pilarhomes-prototype/
├── app/
│   ├── page.tsx                 # Homepage
│   ├── imoveis/
│   │   ├── page.tsx            # Listagem
│   │   └── [id]/page.tsx       # Detalhes
│   ├── corretores/
│   │   └── page.tsx            # Diretório de corretores
│   └── boutiques/
│       └── page.tsx            # Boutiques parceiras
├── components/
│   ├── ui/                     # Componentes base
│   ├── property/               # Componentes de imóveis
│   └── layout/                 # Header, Footer
├── lib/
│   ├── tokens.ts               # Design tokens
│   ├── api-client.ts           # API client
│   └── mock-data.ts            # Dados de exemplo
└── styles/
    └── globals.css             # Imports tokens.css
```

### Deploy
```bash
# Conectar ao Vercel
vercel

# Ou via Git
git init
git add .
git commit -m "Initial commit"
git remote add origin <seu-repo>
git push -u origin main

# Deploy automático via Vercel dashboard
```

---

## ✅ Validação

Use este checklist para garantir fidelidade ao design original:

- [ ] Cores corretas (#000 primary, #ddc79f beige)
- [ ] Tipografia Inter em todo o site
- [ ] Espaçamento em múltiplos de 4px
- [ ] Border-radius: 8px para cards, 9999px para pills
- [ ] Transições suaves (0.15s ease-in-out)
- [ ] Badges "Exclusivo PilarHomes" corretos
- [ ] Cards de propriedade com sombras sutis
- [ ] Hover states funcionando
- [ ] Imagens lazy loading
- [ ] Responsive em todas as breakpoints
- [ ] Sem emojis (posicionamento luxury)

---

**Status**: Pronto para uso no protótipo ✅  
**Última Atualização**: 2025-12-03
