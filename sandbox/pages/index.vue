<template>
  <div class="wrapper">
    <div class="container">
      <CodeExample :is-loading="isLoading" :is-summary.sync="isSummary" />
      <CodeMirror :code.sync="code" />
    </div>
    <div class="brand">vizio</div>
    <button class="button-generate" :disabled="isLoading" @click="generateDot">
      <div v-if="isLoading" class="loading-group">
        <div class="loading">🌀</div>
        <div class="loading">🌀</div>
        <div class="loading">🌀</div>
      </div>
      <div v-else>Generate</div>
    </button>
    <div class="container">
      <DownloadGroup :is-loading="isLoading" :is-failed="isFailed" :dot="dot" />
      <FlowChart :is-loading="isLoading" :is-failed="isFailed" :dot="dot" />
    </div>
  </div>
</template>

<script>
import { readFile } from '~/utils/file_hanlder.js'

export default {
  name: 'VizSandBox',

  data() {
    return {
      code: '',
      dot: '',
      isLoading: false,
      isSummary: false,
      isFailed: false,
    }
  },

  computed: {
    active() {
      return this.$store.state.examples.active
    },
    example() {
      return this.$store.state.examples.list[this.active]
    },
  },

  watch: {
    example: {
      handler() {
        this.loadExample()
      },
      immediate: true,
    },

    isSummary: {
      handler() {
        this.generateDot()
      },
      immediate: true,
    },
  },

  methods: {
    loadExample() {
      if (this.isLoading) return

      const filePath = `/data/examples/${this.example.file}`
      readFile(filePath).then((code) => {
        this.code = code
        this.generateDot()
      })
    },

    async generateDot() {
      if (this.isLoading || !this.code) return

      try {
        this.isLoading = true

        const res = await this.$axios.$post('/generate_viz_devs', {
          source_code: this.code,
          need_summary: this.isSummary,
        })
        this.dot = res.results
      } catch {
        this.isFailed = true
      } finally {
        this.isLoading = false
      }
    },
  },
}
</script>

<style>
body {
  margin: 0;
}

* {
  box-sizing: border-box;
}

.wrapper {
  position: relative;
  height: 100vh;
  width: 100vw;
  display: flex;
  gap: 10px;
  padding: 10px;
}

.container {
  width: 50vw;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.brand {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  font-family: fantasy;
  font-size: 28px;
  font-weight: bold;
  color: #3f87cc;
}

button {
  min-width: 30px;
  height: 30px;
  background-color: white;
  color: #1877f2;
  border: 1px solid #1877f2;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4px 8px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  z-index: 999;
}

button.active {
  background-color: #e6f4ff;
}

button:not(:disabled):hover {
  background-color: #bae0ff;
}

button:disabled:not(.button-generate) {
  opacity: 0.5;
  cursor: not-allowed;
}

.button-generate {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.loading-group {
  display: flex;
  gap: 2px;
}

.loading-group .loading {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>
