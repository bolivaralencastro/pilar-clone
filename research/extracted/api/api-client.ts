/**
 * PilarHomes API Client
 * Mock implementation for Vercel prototype based on real API structure
 * 
 * NOTE: This is a MOCK client for prototyping. Real API requires:
 * - Iron v2 encrypted session cookies
 * - AWS ALB session management
 * - Nuxt.js server proxy layer
 * 
 * For production, implement server-side API routes in Next.js that proxy
 * to pilarhomes.com.br/api/* with proper session handling.
 */

import type {
  SessionResponse,
  Wishlist,
  WishlistResponse,
  Property,
  PropertySearchFilters,
  PaginationParams,
  PaginatedResponse,
  APIResponse,
  User,
  ObjectId,
  CommercialId,
} from './api-types';

// ============================================================================
// CONFIGURATION
// ============================================================================

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'https://pilarhomes.com.br';

const DEFAULT_HEADERS = {
  'Accept': '*/*',
  'Content-Type': 'application/json',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
};

// ============================================================================
// API CLIENT CLASS
// ============================================================================

export class PilarAPI {
  private baseUrl: string;
  private sessionCookie?: string;
  
  constructor(baseUrl: string = API_BASE_URL) {
    this.baseUrl = baseUrl;
  }
  
  /**
   * Set session cookie for authenticated requests
   */
  setSession(sessionCookie: string): void {
    this.sessionCookie = sessionCookie;
  }
  
  /**
   * Clear session cookie
   */
  clearSession(): void {
    this.sessionCookie = undefined;
  }
  
  /**
   * Make authenticated request
   */
  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${this.baseUrl}${endpoint}`;
    
    const headers = new Headers(DEFAULT_HEADERS);
    
    // Add session cookie if available
    if (this.sessionCookie) {
      headers.set('Cookie', `nuxt-session=${this.sessionCookie}`);
    }
    
    // Merge custom headers
    if (options.headers) {
      Object.entries(options.headers).forEach(([key, value]) => {
        headers.set(key, value as string);
      });
    }
    
    const response = await fetch(url, {
      ...options,
      headers,
      credentials: 'include', // Include cookies
    });
    
    if (!response.ok) {
      throw new Error(`API Error: ${response.status} ${response.statusText}`);
    }
    
    return response.json();
  }
  
  // ==========================================================================
  // AUTHENTICATION
  // ==========================================================================
  
  /**
   * Get current session information
   * GET /api/_auth/session
   */
  async getSession(): Promise<SessionResponse> {
    return this.request<SessionResponse>('/api/_auth/session');
  }
  
  // ==========================================================================
  // WISHLIST
  // ==========================================================================
  
  /**
   * Get user's wishlists
   * GET /api/wishlist
   */
  async getWishlists(): Promise<WishlistResponse> {
    return this.request<WishlistResponse>('/api/wishlist');
  }
  
  /**
   * Get main wishlist
   */
  async getMainWishlist(): Promise<Wishlist | null> {
    const wishlists = await this.getWishlists();
    return wishlists.find(w => w.mainWishlist) || null;
  }
  
  /**
   * Create new wishlist
   * POST /api/wishlist (assumed endpoint)
   */
  async createWishlist(data: {
    title: string;
    description?: string;
    privacy?: 'public' | 'private';
  }): Promise<Wishlist> {
    return this.request<Wishlist>('/api/wishlist', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }
  
  /**
   * Update wishlist
   * PUT /api/wishlist/{id} (assumed endpoint)
   */
  async updateWishlist(
    id: ObjectId,
    data: Partial<{
      title: string;
      description: string;
      privacy: 'public' | 'private';
    }>
  ): Promise<Wishlist> {
    return this.request<Wishlist>(`/api/wishlist/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }
  
  /**
   * Delete wishlist
   * DELETE /api/wishlist/{id} (assumed endpoint)
   */
  async deleteWishlist(id: ObjectId): Promise<void> {
    await this.request<void>(`/api/wishlist/${id}`, {
      method: 'DELETE',
    });
  }
  
  /**
   * Add property to wishlist
   * POST /api/wishlist/{id}/properties (assumed endpoint)
   */
  async addPropertyToWishlist(
    wishlistId: ObjectId,
    propertyId: ObjectId
  ): Promise<Wishlist> {
    return this.request<Wishlist>(`/api/wishlist/${wishlistId}/properties`, {
      method: 'POST',
      body: JSON.stringify({ propertyId }),
    });
  }
  
  /**
   * Remove property from wishlist
   * DELETE /api/wishlist/{id}/properties/{propertyId} (assumed endpoint)
   */
  async removePropertyFromWishlist(
    wishlistId: ObjectId,
    propertyId: ObjectId
  ): Promise<Wishlist> {
    return this.request<Wishlist>(
      `/api/wishlist/${wishlistId}/properties/${propertyId}`,
      {
        method: 'DELETE',
      }
    );
  }
  
  // ==========================================================================
  // PROPERTIES (endpoints need investigation - currently return 403)
  // ==========================================================================
  
  /**
   * Search properties
   * POST /api/properties/search (currently returns 403)
   * 
   * NOTE: This endpoint requires additional authentication beyond session cookie
   * Possible: CSRF token, API key, or specific headers
   */
  async searchProperties(
    filters: PropertySearchFilters,
    pagination: PaginationParams = { page: 1, perPage: 50 }
  ): Promise<PaginatedResponse<Property>> {
    throw new Error('Endpoint returns 403 - needs investigation');
    
    // Theoretical implementation:
    // return this.request<PaginatedResponse<Property>>('/api/properties/search', {
    //   method: 'POST',
    //   body: JSON.stringify({ filters, ...pagination }),
    // });
  }
  
  /**
   * Get property by ID
   * GET /api/properties/{id} (assumed endpoint - needs testing)
   */
  async getProperty(id: ObjectId | CommercialId): Promise<Property> {
    return this.request<Property>(`/api/properties/${id}`);
  }
  
  /**
   * Get property by commercial ID
   * Alternative route that might work
   */
  async getPropertyByCommercialId(commercialId: CommercialId): Promise<Property> {
    return this.getProperty(commercialId);
  }
  
  // ==========================================================================
  // COMPANIES/BOUTIQUES (endpoints unknown)
  // ==========================================================================
  
  /**
   * Get all companies (endpoint unknown)
   */
  async getCompanies(): Promise<any[]> {
    throw new Error('Endpoint not yet discovered');
  }
  
  /**
   * Get company by ID (endpoint unknown)
   */
  async getCompany(id: ObjectId): Promise<any> {
    throw new Error('Endpoint not yet discovered');
  }
  
  // ==========================================================================
  // BROKERS/AGENTS (endpoints unknown)
  // ==========================================================================
  
  /**
   * Get all brokers (endpoint unknown)
   */
  async getBrokers(): Promise<any[]> {
    throw new Error('Endpoint not yet discovered');
  }
  
  /**
   * Get broker by ID (endpoint unknown)
   */
  async getBroker(id: ObjectId): Promise<any> {
    throw new Error('Endpoint not yet discovered');
  }
}

// ============================================================================
// SINGLETON INSTANCE
// ============================================================================

export const apiClient = new PilarAPI();

// ============================================================================
// MOCK DATA FOR PROTOTYPING
// ============================================================================

/**
 * Mock wishlist response (based on real API data from 2025-12-03)
 */
export const MOCK_WISHLIST: WishlistResponse = [
  {
    id: "692f4a67aa9cd04de8c860e8",
    owner: {
      _id: "692ebe1112ffb7eb6a4b08a4",
      name: "Demo User",
      updatedAt: "2025-12-02T20:21:59.324000"
    },
    title: "Minha Coleção",
    description: "Imóveis favoritos",
    propertyCount: 2,
    properties: [
      {
        _id: "68702cf0e074c2d5e602c1d8",
        commercialId: "YVA137671",
        addedAt: "2025-12-02T20:21:59.329000",
        addedBy: {
          _id: "692ebe1112ffb7eb6a4b08a4",
          name: "Demo User",
          updatedAt: "2025-12-02T20:21:59.324000"
        },
        likesCount: 0,
        topComments: [],
        commentsCount: 0
      },
      {
        _id: "68c18827d2445315b270a08e",
        commercialId: "LGE004",
        addedAt: "2025-12-02T20:22:00.494000",
        addedBy: {
          _id: "692ebe1112ffb7eb6a4b08a4",
          name: "Demo User",
          updatedAt: "2025-12-02T20:21:59.324000"
        },
        likesCount: 0,
        topComments: [],
        commentsCount: 0
      }
    ],
    sharedWith: [],
    privacy: "public",
    mainWishlist: true,
    createdAt: "2025-12-02T20:21:59.324000",
    updatedAt: "2025-12-02T20:22:00.494000",
    deletedAt: null
  }
];

/**
 * Mock session response
 */
export const MOCK_SESSION: SessionResponse = {
  id: "8474b319-eaaa-44d6-9389-ec30c7231377"
};

// ============================================================================
// REACT HOOKS (for Next.js App Router)
// ============================================================================

/**
 * Example usage in Next.js Server Component
 */
export async function getServerSideWishlists(sessionCookie?: string): Promise<WishlistResponse> {
  const api = new PilarAPI();
  
  if (sessionCookie) {
    api.setSession(sessionCookie);
  }
  
  try {
    return await api.getWishlists();
  } catch (error) {
    console.error('Failed to fetch wishlists:', error);
    // Return mock data as fallback
    return MOCK_WISHLIST;
  }
}

/**
 * Example usage in Next.js API Route
 */
export async function handleWishlistRequest(
  request: Request
): Promise<Response> {
  const sessionCookie = request.headers.get('cookie')
    ?.split(';')
    .find(c => c.trim().startsWith('nuxt-session='))
    ?.split('=')[1];
  
  const api = new PilarAPI();
  
  if (sessionCookie) {
    api.setSession(sessionCookie);
  }
  
  try {
    const wishlists = await api.getWishlists();
    return Response.json(wishlists);
  } catch (error) {
    return Response.json(
      { error: 'Failed to fetch wishlists' },
      { status: 500 }
    );
  }
}
