<template>
  <div class="wrapper">
    <div class="container">
      <CodeExample />
      <CodeMirror :code.sync="code" />
    </div>
    <div class="brand">vizio</div>
    <button class="button-generate" :disabled="isLoading" @click="generateDot">
      <div v-if="isLoading">🌀🌀🌀</div>
      <div v-else>Generate</div>
    </button>
    <div class="container">
      <DownloadGroup :dot="dot" />
      <FlowChart :dot="dot" />
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
  },

  methods: {
    loadExample() {
      const filePath = `/data/examples/${this.example.file}`
      readFile(filePath).then((code) => {
        this.code = code
        this.generateDot()
      })
    },

    async generateDot() {
      if (this.isLoading) return

      try {
        this.isLoading = true

        const res = await this.$axios.$post('/generate_viz_devs', {
          source_code: this.code,
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
  font-size: 24px;
  font-weight: bold;
  color: #3f87cc;
}

button {
  background-color: white;
  color: #1877f2;
  border: 1px solid #1877f2;
  border-radius: 4px;
  padding: 4px 8px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

button.active {
  background-color: #e6f4ff;
}

button:hover {
  background-color: #bae0ff;
}

button:disabled {
  background-color: #e6f4ff;
}

.button-generate {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
