/**
 * PilarHomes API TypeScript Types
 * Generated from real authenticated API responses
 * Date: 2025-12-03
 * Source: Live API data from pilarhomes.com.br
 */

// ============================================================================
// BASE TYPES
// ============================================================================

/**
 * MongoDB ObjectId as string (24-character hexadecimal)
 * Example: "692ebe1112ffb7eb6a4b08a4"
 */
export type ObjectId = string;

/**
 * ISO 8601 datetime string with microsecond precision
 * Example: "2025-12-02T20:21:59.324000"
 */
export type ISODateTime = string;

/**
 * Commercial property ID format
 * Pattern: 3 uppercase letters (company code) + 3-6 digits
 * Examples: "YVA137671", "LGE004"
 */
export type CommercialId = string;

/**
 * UUID v4 string for anonymous tracking
 * Example: "23ae0dad-6e99-42ec-98cd-2d06b981432a"
 */
export type UUID = string;

// ============================================================================
// USER TYPES
// ============================================================================

/**
 * User object (partial - appears in multiple contexts)
 */
export interface User {
  /** MongoDB ObjectId */
  _id: ObjectId;
  
  /** Full name */
  name: string;
  
  /** Last update timestamp */
  updatedAt: ISODateTime;
  
  /** Email (discovered in Mixpanel cookie, not in API response) */
  email?: string;
  
  /** Phone with country code (discovered in Mixpanel cookie) */
  phone?: string;
}

/**
 * User preferences stored in localStorage
 */
export interface UserPreferences {
  /** Brazilian states (e.g., ["SP", "RJ"]) */
  states?: string[];
  
  /** Cities (e.g., ["São Paulo", "Rio de Janeiro"]) */
  cities?: string[];
  
  /** Specific regions/neighborhoods (e.g., ["Jardim Guedala"]) */
  regions?: string[];
  
  /** Maximum asking price in BRL */
  askingPrice?: number;
  
  /** Property types (e.g., ["house", "apartment"]) */
  propertyTypes?: string[];
}

// ============================================================================
// AUTHENTICATION TYPES
// ============================================================================

/**
 * Session response from /api/_auth/session
 */
export interface SessionResponse {
  /** Session UUID */
  id: UUID;
}

/**
 * Authentication cookies
 */
export interface AuthCookies {
  /** Iron v2 encrypted session (Fe26.2** format) */
  'nuxt-session': string;
  
  /** AWS Application Load Balancer session */
  'AWSALBAPP-0': string;
  
  /** AWS Target Group cookie */
  AWSALBTG?: string;
  
  /** AWS Target Group CORS cookie */
  AWSALBTGCORS?: string;
  
  /** Anonymous tracking ID (persists after logout) */
  pilar_anon_id: UUID;
  
  /** Mixpanel analytics (contains user data) */
  mp_804b84f25add0baf52ffd23254f3b7bc_mixpanel?: string;
}

// ============================================================================
// PROPERTY TYPES
// ============================================================================

/**
 * Property reference in wishlist (minimal data)
 */
export interface WishlistProperty {
  /** MongoDB ObjectId */
  _id: ObjectId;
  
  /** Commercial property ID (e.g., "YVA137671") */
  commercialId: CommercialId;
  
  /** When property was added to wishlist */
  addedAt: ISODateTime;
  
  /** User who added the property */
  addedBy: User;
  
  /** Number of likes/favorites */
  likesCount: number;
  
  /** Top comments (structure unknown) */
  topComments: unknown[];
  
  /** Total number of comments */
  commentsCount: number;
}

/**
 * Full property object (structure incomplete - needs /api/properties/{id})
 */
export interface Property {
  /** MongoDB ObjectId */
  _id: ObjectId;
  
  /** Commercial property ID */
  commercialId: CommercialId;
  
  /** Property title */
  title?: string;
  
  /** Property description */
  description?: string;
  
  /** Asking price in BRL */
  askingPrice?: number;
  
  /** Property type (house, apartment, etc.) */
  propertyType?: string;
  
  /** Location data */
  location?: {
    state?: string;
    city?: string;
    region?: string;
    address?: string;
  };
  
  /** Property features */
  features?: {
    bedrooms?: number;
    suites?: number;
    bathrooms?: number;
    parkingSpaces?: number;
    builtArea?: number;
    landArea?: number;
  };
  
  /** Image URLs */
  images?: string[];
  
  /** Associated company/boutique */
  company?: {
    _id: ObjectId;
    name: string;
  };
  
  /** Associated broker/agent */
  broker?: {
    _id: ObjectId;
    name: string;
  };
  
  /** Whether property is exclusive to Pilar */
  isExclusive?: boolean;
  
  /** Timestamps */
  createdAt?: ISODateTime;
  updatedAt?: ISODateTime;
  deletedAt?: ISODateTime | null;
}

// ============================================================================
// WISHLIST TYPES
// ============================================================================

/**
 * Privacy setting for wishlist
 */
export type WishlistPrivacy = 'public' | 'private';

/**
 * Complete wishlist object from /api/wishlist
 */
export interface Wishlist {
  /** MongoDB ObjectId */
  id: ObjectId;
  
  /** Wishlist owner */
  owner: User;
  
  /** Wishlist title */
  title: string;
  
  /** Wishlist description */
  description: string;
  
  /** Number of properties in wishlist */
  propertyCount: number;
  
  /** Array of properties (minimal data) */
  properties: WishlistProperty[];
  
  /** Users with whom wishlist is shared */
  sharedWith: User[];
  
  /** Privacy setting */
  privacy: WishlistPrivacy;
  
  /** Whether this is the user's main/default wishlist */
  mainWishlist: boolean;
  
  /** Creation timestamp */
  createdAt: ISODateTime;
  
  /** Last update timestamp */
  updatedAt: ISODateTime;
  
  /** Soft delete timestamp (null if not deleted) */
  deletedAt: ISODateTime | null;
}

/**
 * Response from GET /api/wishlist
 */
export type WishlistResponse = Wishlist[];

// ============================================================================
// SEARCH/FILTER TYPES
// ============================================================================

/**
 * Property search filters (structure inferred from localStorage preferences)
 */
export interface PropertySearchFilters {
  /** Brazilian states */
  states?: string[];
  
  /** Cities */
  cities?: string[];
  
  /** Regions/neighborhoods */
  regions?: string[];
  
  /** Minimum asking price in BRL */
  minPrice?: number;
  
  /** Maximum asking price in BRL */
  maxPrice?: number;
  
  /** Property types */
  propertyTypes?: string[];
  
  /** Minimum bedrooms */
  minBedrooms?: number;
  
  /** Minimum parking spaces */
  minParkingSpaces?: number;
  
  /** Only exclusive properties */
  isExclusive?: boolean;
}

/**
 * Pagination parameters
 */
export interface PaginationParams {
  /** Page number (1-indexed) */
  page: number;
  
  /** Items per page */
  perPage: number;
}

/**
 * Paginated response wrapper (structure assumed)
 */
export interface PaginatedResponse<T> {
  /** Array of items */
  data: T[];
  
  /** Pagination metadata */
  meta: {
    /** Current page */
    currentPage: number;
    
    /** Total number of pages */
    totalPages: number;
    
    /** Total number of items */
    totalItems: number;
    
    /** Items per page */
    perPage: number;
  };
}

// ============================================================================
// API CLIENT TYPES
// ============================================================================

/**
 * API error response (structure assumed)
 */
export interface APIError {
  /** Error message */
  message: string;
  
  /** Error code */
  code?: string;
  
  /** HTTP status code */
  statusCode?: number;
  
  /** Additional error details */
  details?: unknown;
}

/**
 * API response wrapper (structure assumed)
 */
export type APIResponse<T> = 
  | { success: true; data: T }
  | { success: false; error: APIError };

// ============================================================================
// COMPANY/BOUTIQUE TYPES (structure unknown - needs investigation)
// ============================================================================

/**
 * Company/Boutique (structure incomplete)
 */
export interface Company {
  _id: ObjectId;
  name: string;
  code?: string; // 3-letter code (e.g., "YVA", "LGE")
  // ... other fields unknown
}

// ============================================================================
// BROKER/AGENT TYPES (structure unknown - needs investigation)
// ============================================================================

/**
 * Broker/Agent (structure incomplete)
 */
export interface Broker {
  _id: ObjectId;
  name: string;
  // ... other fields unknown
}

// ============================================================================
// ANALYTICS TYPES
// ============================================================================

/**
 * Mixpanel user data (from cookie)
 */
export interface MixpanelUserData {
  distinct_id: string;
  $device_id: string;
  $anon_id: UUID;
  $user_id?: string;
  __alias?: string;
  version: string;
}

// ============================================================================
// UTILITY TYPES
// ============================================================================

/**
 * Extract company code from commercial ID
 * @example "YVA137671" -> "YVA"
 */
export function extractCompanyCode(commercialId: CommercialId): string {
  return commercialId.substring(0, 3);
}

/**
 * Extract property number from commercial ID
 * @example "YVA137671" -> "137671"
 */
export function extractPropertyNumber(commercialId: CommercialId): string {
  return commercialId.substring(3);
}

/**
 * Type guard for checking if ObjectId is valid MongoDB format
 */
export function isValidObjectId(id: string): id is ObjectId {
  return /^[0-9a-f]{24}$/i.test(id);
}

/**
 * Type guard for checking if string is valid commercial ID
 */
export function isValidCommercialId(id: string): id is CommercialId {
  return /^[A-Z]{3}\d{3,6}$/.test(id);
}
