import { defineStore } from 'pinia'

export type CompareItem = {
  id: string
  title: string
  price?: number
  area?: number
  bedrooms?: number
  bathrooms?: number
  city?: string
  region?: string
}

const MAX_ITEMS = 4

export const useCompareStore = defineStore('compare', {
  state: () => ({
    items: [] as CompareItem[],
    warning: '' as string
  }),
  getters: {
    count: (state) => state.items.length,
    isFull: (state) => state.items.length >= MAX_ITEMS,
    ids: (state) => state.items.map(i => i.id)
  },
  actions: {
    clearWarning() {
      this.warning = ''
    },
    add(item: CompareItem) {
      if (this.items.find(i => i.id === item.id)) return
      if (this.items.length >= MAX_ITEMS) {
        this.warning = `Você pode comparar até ${MAX_ITEMS} imóveis.`
        return
      }
      this.items.push(item)
    },
    remove(id: string) {
      this.items = this.items.filter(i => i.id !== id)
    },
    clear() {
      this.items = []
    }
  }
})