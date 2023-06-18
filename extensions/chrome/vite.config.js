import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    assetsInlineLimit: 0,
    rollupOptions: {
        input: {
            main: './src/main.js', // Update the entry point based on your extension's main script file
        },
        output: {
            entryFileNames: '[name].js',
        }
    },
  },
});
