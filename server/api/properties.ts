import { defineEventHandler, getQuery } from 'h3'

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  const query = getQuery(event)
  
  // Construir query string
  const params = new URLSearchParams()
  
  // Parâmetros de paginação
  params.append('page', String(query.page || 1))
  params.append('perPage', String(query.perPage || 12))
  
  // Tipo de transação
  if (query.transactionType) {
    params.append('transactionType', String(query.transactionType))
  }
  
  // Tipo de imóvel
  if (query.propertyType) {
    params.append('propertyType', String(query.propertyType))
  }
  
  // Filtros de preço
  if (query.minPrice) {
    params.append('minPrice', String(query.minPrice))
  }
  if (query.maxPrice) {
    params.append('maxPrice', String(query.maxPrice))
  }
  
  // Filtros de área
  if (query.minArea) {
    params.append('minArea', String(query.minArea))
  }
  if (query.maxArea) {
    params.append('maxArea', String(query.maxArea))
  }
  
  // Quartos, suítes, vagas
  if (query.bedrooms) {
    params.append('bedrooms', String(query.bedrooms))
  }
  if (query.suites) {
    params.append('suites', String(query.suites))
  }
  if (query.parkingSpots) {
    params.append('parkingSpots', String(query.parkingSpots))
  }
  
  // Localização
  if (query.city) {
    params.append('city', String(query.city))
  }
  if (query.region) {
    params.append('region', String(query.region))
  }
  
  const apiUrl = `${config.pilarApiUrl}/api/properties?${params.toString()}`
  
  try {
    const response = await fetch(apiUrl, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://pilarhomes.com.br/',
        'Origin': 'https://pilarhomes.com.br'
      }
    })
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`)
    }
    
    const data = await response.json()
    return data
    
  } catch (error: unknown) {
    const errorMessage = error instanceof Error ? error.message : 'Unknown error'
    console.error('Error fetching properties:', errorMessage)
    
    return {
      error: true,
      message: errorMessage,
      properties: [],
      pagination: {
        page: 1,
        perPage: 12,
        total: 0,
        totalPages: 0
      }
    }
  }
})
