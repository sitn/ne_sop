import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { quasar, transformAssetUrls } from '@quasar/vite-plugin'
import { resolve } from 'path'

const projectRootDir = resolve(__dirname)

// https://vitejs.dev/config/
export default defineConfig({
  base: '/web/sop/', // /front/
  publicDir: 'public',
  plugins: [
    /* vue(),
    quasar({
      lang: 'fr',
    }),
    */
    vue({
      template: { transformAssetUrls }
    }),
    quasar({
      config: {
        lang: 'fr'
      }
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      '@assets/*': fileURLToPath(new URL('./src/assets/', import.meta.url)),
      '@public/*': fileURLToPath(new URL('./public/', import.meta.url)),
    }
  }
})
