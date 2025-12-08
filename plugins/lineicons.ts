import { h } from 'vue'

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.component('Icon', {
    props: {
      name: {
        type: String,
        required: true
      }
    },
    setup(props) {
      return () => {
        let className = props.name
        // Ensure 'lni' base class is present if not already
        // LineIcons usually requires 'lni' + 'lni-icon-name'
        if (!className.includes('lni ')) {
           className = `lni ${className}`
        }
        return h('i', { class: className })
      }
    }
  })
})
