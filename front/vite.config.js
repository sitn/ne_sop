import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

const projectRootDir = resolve(__dirname)

// https://vitejs.dev/config/
export default defineConfig({
  base: '/',
  publicDir: 'public',
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  /*
  rollup: {
    external: ['pdfmake/build/pdfmake', 'pdfmake/build/vfs_fonts'],
  },
  */
  /*
  optimizeDeps: {
    include: ['pdfmake/build/vfs_fonts'],
  },
  */
  // optimizeDeps: { include: ['pdfmake/build/pdfmake', 'pdfmake/build/vfs_fonts'] },
  // commonjsOptions: { exclude: ['pdfmake/build/pdfmake', 'pdfmake/build/vfs_fonts'] },
  // commonjsOptions: { }, // Edit: 

})
