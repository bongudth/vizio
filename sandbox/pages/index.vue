<template>
  <div class="wrapper">
    <div class="container">
      <CodeExample />
      <CodeMirror :code="code" />
    </div>
    <div class="container">
      <FlowChart />
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
      })
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
</style>
