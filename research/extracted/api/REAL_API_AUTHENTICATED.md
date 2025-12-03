# Pilar Homes - Real Authenticated API Documentation

**Status**: ✅ LIVE DATA - Captured from authenticated session (User: Bolivar Alencastro, ID: 692ebe1112ffb7eb6a4b08a4)  
**Date**: 2025-12-03  
**App Version**: eba7fe8a8c54d5f94e813abc7f5acfe6b6ccad05

---

## 🔐 Authentication System

### Cookie-Based Session (Iron v2 Encryption)

**Primary Cookie**: `nuxt-session`
- **Format**: Iron v2 sealed object (`Fe26.2**...`)
- **Security**: AES-256 encryption + HMAC verification
- **Attributes**: HttpOnly, Secure, SameSite=Lax
- **Expiry**: 7 days
- **Example**:
  ```
  Fe26.2**41b8a2019b3353d5a1d942c8384a91cb21457612cf13a7bd23ce7545e41ca7aa*zXihVD8ykH_Mxh_VobXcwA*RBR0BqaPM9eiPTnIYDMG76dJQtTPUTaHv8xVlKd7iiwkjRIeXF0Tf7GJxuyytZEplI2GCQdp9DZdXbupIWhOY761e1Gl8HdBedBcr0CpeWwt0qotCS2lLeHxCQScWYTkQFLC1KlWz85TySi4lytPjM2Z1fO18RWJ4zxTH1OpxBxpvpES_y6bTtpdxgGo1pTx...
  ```

**AWS Load Balancer Cookie**: `AWSALBAPP-0`
- **Purpose**: Session stickiness across ALB targets
- **Format**: Base64-encoded AWS session ID
- **Attributes**: Secure, SameSite=None
- **Expiry**: 7 days
- **Example**: `AAAAAAAAAAAWOZOBPQOtm6ofCrV4r2WjWOfBNT3cRt0GlE4c2lFbECy4+xvByfbllG00oE6MH/5j...`

**Anonymous Tracking**: `pilar_anon_id`
- **Purpose**: Track sessions before login, link to user after auth
- **Format**: UUID v4
- **Persistent**: Yes (survives logout)
- **Example**: `23ae0dad-6e99-42ec-98cd-2d06b981432a`

### Infrastructure Flow

```
Client Request
    ↓
CloudFront CDN (GRU1-P4 - São Paulo)
    ↓
AWS Application Load Balancer (ALB)
    ↓
Nuxt.js 3 SSR App
    ↓
Backend API (MongoDB)
```

**Headers to Include**:
```http
Cookie: nuxt-session={encrypted_session}; AWSALBAPP-0={aws_session}; pilar_anon_id={uuid}
Referer: https://pilarhomes.com.br/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
Accept: */*
```

---

## 📡 Discovered Endpoints

### ✅ Working Endpoints (200 OK)

#### `GET /api/_auth/session`
**Purpose**: Get current session information  
**Auth**: Required (nuxt-session cookie)  
**Cache**: `no-cache, must-revalidate`

**Request**:
```http
GET /api/_auth/session HTTP/1.1
Host: pilarhomes.com.br
Cookie: nuxt-session={encrypted_session}; AWSALBAPP-0={aws_session}
```

**Response** (200 OK):
```json
{
  "id": "8474b319-eaaa-44d6-9389-ec30c7231377"
}
```

**Response Headers**:
```http
Content-Type: application/json
Cache-Control: no-cache, must-revalidate
Set-Cookie: nuxt-session={new_encrypted_session}; Path=/; HttpOnly; Secure; SameSite=Lax
Set-Cookie: AWSALBAPP-0={aws_session}; Expires=Wed, 10 Dec 2025 05:29:35 GMT; Path=/; SameSite=None; Secure
X-Version: eba7fe8a8c54d5f94e813abc7f5acfe6b6ccad05
Via: 1.1 {cloudfront_id}.cloudfront.net (CloudFront)
X-Cache: Miss from cloudfront
```

---

#### `GET /api/wishlist`
**Purpose**: Get user's wishlist (favorited properties)  
**Auth**: Required (nuxt-session cookie)  
**Cache**: `no-cache, must-revalidate`

**Request**:
```http
GET /api/wishlist HTTP/1.1
Host: pilarhomes.com.br
Cookie: nuxt-session={encrypted_session}; AWSALBAPP-0={aws_session}
Accept: */*
```

**Response** (200 OK):
```json
[
  {
    "owner": {
      "_id": "692ebe1112ffb7eb6a4b08a4",
      "name": "Bolivar Alencastro",
      "updatedAt": "2025-12-02T20:21:59.324000"
    },
    "title": "Coleção de Bolivar",
    "description": "Coleção de Bolivar",
    "propertyCount": 2,
    "properties": [
      {
        "_id": "68702cf0e074c2d5e602c1d8",
        "commercialId": "YVA137671",
        "addedAt": "2025-12-02T20:21:59.329000",
        "addedBy": {
          "_id": "692ebe1112ffb7eb6a4b08a4",
          "name": "Bolivar Alencastro",
          "updatedAt": "2025-12-02T20:21:59.324000"
        },
        "likesCount": 0,
        "topComments": [],
        "commentsCount": 0
      },
      {
        "_id": "68c18827d2445315b270a08e",
        "commercialId": "LGE004",
        "addedAt": "2025-12-02T20:22:00.494000",
        "addedBy": {
          "_id": "692ebe1112ffb7eb6a4b08a4",
          "name": "Bolivar Alencastro",
          "updatedAt": "2025-12-02T20:21:59.324000"
        },
        "likesCount": 0,
        "topComments": [],
        "commentsCount": 0
      }
    ],
    "sharedWith": [
      {
        "_id": "692ebe1112ffb7eb6a4b08a4",
        "name": "Bolivar Alencastro",
        "updatedAt": "2025-12-02T20:21:59.324000"
      }
    ],
    "privacy": "public",
    "mainWishlist": true,
    "createdAt": "2025-12-02T20:21:59.324000",
    "updatedAt": "2025-12-02T20:22:00.494000",
    "deletedAt": null,
    "id": "692f4a67aa9cd04de8c860e8"
  }
]
```

**Schema Insights**:
- Wishlists are collections owned by users
- Each wishlist can contain multiple properties (referenced by `_id` and `commercialId`)
- Properties in wishlist show metadata: `likesCount`, `commentsCount`, `addedAt`
- Wishlists support sharing (`sharedWith` array of users)
- Privacy settings: `"public"` or likely `"private"`
- `mainWishlist: true` suggests users can have multiple wishlists
- Uses MongoDB ObjectIds (`_id` format: `692ebe1112ffb7eb6a4b08a4`)
- Dates in ISO 8601 format with microseconds: `2025-12-02T20:21:59.324000`
- Soft deletes supported (`deletedAt` field)

**TypeScript Type**:
```typescript
interface User {
  _id: string; // MongoDB ObjectId
  name: string;
  updatedAt: string; // ISO 8601 datetime
}

interface WishlistProperty {
  _id: string; // MongoDB ObjectId
  commercialId: string; // Human-readable ID (e.g., "YVA137671", "LGE004")
  addedAt: string; // ISO 8601 datetime
  addedBy: User;
  likesCount: number;
  topComments: any[]; // Need to investigate structure
  commentsCount: number;
}

interface Wishlist {
  id: string; // MongoDB ObjectId
  owner: User;
  title: string;
  description: string;
  propertyCount: number;
  properties: WishlistProperty[];
  sharedWith: User[];
  privacy: "public" | "private"; // Inferred
  mainWishlist: boolean;
  createdAt: string; // ISO 8601 datetime
  updatedAt: string; // ISO 8601 datetime
  deletedAt: string | null; // ISO 8601 datetime or null
}

type WishlistResponse = Wishlist[];
```

---

### ❌ Blocked Endpoints (403 Forbidden)

#### `POST /api/properties/search`
**Status**: 403 Forbidden  
**Issue**: Returns 403 even with valid `nuxt-session` cookie  
**Hypothesis**: 
- Requires CSRF token in headers (`x-csrf-token` or similar)
- Needs specific API key
- Rate limited (user made multiple requests)
- Endpoint may require elevated permissions

**Request** (failed):
```http
POST /api/properties/search HTTP/1.1
Host: pilarhomes.com.br
Cookie: nuxt-session={encrypted_session}
Content-Type: application/json

{
  // Unknown request body structure
}
```

**Response** (403):
```
Forbidden
```

**Action Needed**: Investigate successful property list calls to see what headers/params are included.

---

#### `GET https://api.pilarhomes.com.br/properties`
**Status**: 403 Forbidden (all requests)  
**Issue**: Direct API subdomain access blocked even with session cookies  
**Hypothesis**:
- API requires requests to come through Nuxt.js proxy (`/api/*` not `api.pilarhomes.com.br`)
- CORS policy blocks browser requests
- API key required in headers
- Requests must originate from verified CloudFront distribution

**Failed Patterns**:
```http
GET https://api.pilarhomes.com.br/properties?page=1&perPage=50
GET https://api.pilarhomes.com.br/properties?page=2&perPage=50
GET https://api.pilarhomes.com.br/properties?isExclusive=true&page=1&perPage=50
GET https://api.pilarhomes.com.br/properties?isExclusive=true&page=2&perPage=50
```

**All returned**: 403 Forbidden

**Discovery**: Pilar uses **Nuxt.js server middleware as API proxy**. Direct API access is intentionally blocked to:
1. Protect backend API endpoints from public exposure
2. Add server-side authorization layer
3. Transform/validate requests before hitting backend
4. Rate limit and abuse protection

**Correct Pattern**: Use `/api/*` endpoints on main domain, not `api.pilarhomes.com.br`

---

## 🔍 Endpoint Discovery Patterns

### Working Pattern
```
✅ https://pilarhomes.com.br/api/{endpoint}
   → Goes through Nuxt.js SSR server
   → Server validates session
   → Proxies to api.pilarhomes.com.br
   → Returns response
```

### Blocked Pattern
```
❌ https://api.pilarhomes.com.br/{endpoint}
   → Direct to API backend
   → No Nuxt.js proxy layer
   → 403 Forbidden (CORS, missing auth, etc.)
```

---

## 📊 Data Model Insights

### MongoDB Usage Confirmed
- All IDs follow MongoDB ObjectId format: 24-character hex string
- Example: `692ebe1112ffb7eb6a4b08a4`
- Timestamps with microsecond precision suggest MongoDB's ISODate format
- Soft delete pattern (`deletedAt` field) is MongoDB best practice

### User Model (Partial)
```javascript
{
  _id: "692ebe1112ffb7eb6a4b08a4",
  name: "Bolivar Alencastro",
  email: "bolivar@alencastro.com.br", // From Mixpanel cookie
  phone: "+5548984138601", // From Mixpanel cookie
  updatedAt: "2025-12-02T20:21:59.324000"
  // ... other fields not yet discovered
}
```

### Property Model (Partial - from wishlist)
```javascript
{
  _id: "68702cf0e074c2d5e602c1d8",
  commercialId: "YVA137671", // Human-readable reference
  // ... full structure needs /api/properties/{id} endpoint
}
```

### Commercial ID Patterns Observed
- `YVA137671` - Format: 3 uppercase letters + 6 digits
- `LGE004` - Format: 3 uppercase letters + 3 digits

**Hypothesis**: First 3 letters = Company/Boutique code
- `YVA` = Yara Valente Advogados (from previous docs)
- `LGE` = Unknown boutique (need to cross-reference)

---

## 🎯 Next Investigation Steps

### High Priority
1. ✅ **Examine Wishlist Endpoint** - COMPLETE
2. 🔄 **Navigate Site to Trigger More API Calls**
   - Click property cards → Discover `/api/properties/{id}` endpoint
   - Use search filters → Find working search endpoint pattern
   - View agent profiles → Map `/api/agents/{id}` or `/api/brokers/{id}`
   - Browse boutiques → Map `/api/companies/{id}`

3. 🔄 **Resolve 403 on Search Endpoint**
   - Compare headers between `/api/wishlist` (200) and `/api/properties/search` (403)
   - Look for CSRF token in page source
   - Check for rate limiting headers
   - Investigate if search requires specific user roles

### Medium Priority
4. ⏳ **Document Property Full Schema**
   - Get complete property object from detail view
   - Map all fields (title, price, images, location, features, etc.)
   - Create TypeScript interfaces

5. ⏳ **Test Wishlist Mutations**
   - `POST /api/wishlist` - Create new wishlist
   - `PUT /api/wishlist/{id}` - Update wishlist
   - `DELETE /api/wishlist/{id}` - Delete wishlist
   - `POST /api/wishlist/{id}/properties` - Add property to wishlist
   - `DELETE /api/wishlist/{id}/properties/{propertyId}` - Remove property

### Low Priority
6. ⏳ **Document Analytics Tracking**
   - Mixpanel event schema
   - Datadog RUM metrics
   - GA4 event structure
   - Hotjar session replay triggers

---

## 🔒 Security Observations

### Strengths
- ✅ Iron v2 encryption for sessions (industry-standard, used by npm, GitHub)
- ✅ HttpOnly cookies (XSS protection)
- ✅ Secure flag (HTTPS-only)
- ✅ SameSite=Lax (CSRF protection)
- ✅ 7-day session expiry (reasonable balance)
- ✅ AWS ALB session stickiness (performance + reliability)
- ✅ CloudFront CDN (DDoS protection, speed)
- ✅ API subdomain blocked from direct access (defense in depth)

### Potential Concerns
- ⚠️ No visible CSRF token for POST requests (may be in session payload)
- ⚠️ User data exposed in Mixpanel cookie (name, email, phone visible in browser)
- ⚠️ Anonymous ID persists after logout (tracking concern)
- ⚠️ Session cookies sent to third-party domains (AWS, CloudFront headers visible)

---

## 💡 Vercel Prototype Implications

### API Client Strategy
Since direct `api.pilarhomes.com.br` access is blocked, Vercel prototype should:

1. **Mock the `/api/*` endpoints** with sample data from this document
2. **Create Nuxt-style API routes** in `pages/api/` that return realistic JSON
3. **Use Next.js API Routes** as proxy (same pattern as Nuxt middleware)
4. **Implement Iron session encryption** for authenticity (optional, use JWT for simpler auth)

### Sample Implementation
```typescript
// app/api/wishlist/route.ts
import { NextResponse } from 'next/server';
import { cookies } from 'next/headers';

export async function GET() {
  const sessionCookie = cookies().get('session');
  
  if (!sessionCookie) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  // Mock data based on real structure
  return NextResponse.json([
    {
      id: "692f4a67aa9cd04de8c860e8",
      owner: {
        _id: "692ebe1112ffb7eb6a4b08a4",
        name: "Demo User",
        updatedAt: new Date().toISOString()
      },
      title: "Minha Coleção",
      description: "Imóveis favoritos",
      propertyCount: 2,
      properties: [
        // ... sample properties
      ],
      sharedWith: [],
      privacy: "public",
      mainWishlist: true,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      deletedAt: null
    }
  ]);
}
```

---

## 📝 File Updates Needed

- [x] **This file** (`REAL_API_AUTHENTICATED.md`) - Created with live data
- [ ] `API_ENDPOINTS_MAP.md` - Update with real endpoints (replace hypothetical)
- [ ] `tokens.ts` - Add TypeScript types for API responses
- [ ] `api-client.ts` - Create with session management + wishlist methods
- [ ] `README.md` - Update with authentication flow explanation

---

## 🎓 Key Learnings

1. **Nuxt.js Proxy Pattern**: Modern SSR frameworks use server middleware to proxy API calls, protecting backend from direct access

2. **Iron Sessions**: More secure than JWT for server-side sessions (encryption + HMAC vs just signing)

3. **AWS Infrastructure**: ALB cookies (`AWSALBAPP-*`) required for session stickiness across multiple backend servers

4. **MongoDB Design**: 
   - Soft deletes (`deletedAt`)
   - Embedded documents (user objects in wishlist)
   - Human-readable IDs alongside ObjectIds (`commercialId`)

5. **Analytics Heavy**: Multiple tracking systems (Mixpanel, GA4, Datadog, Hotjar, TikTok, Facebook) suggest strong focus on user behavior analysis

6. **Commercial ID Pattern**: Three-letter boutique codes embedded in property IDs enable instant company identification

---

**Next Action**: Navigate the site to trigger property detail view and capture full property schema from `/api/properties/{id}` endpoint.
