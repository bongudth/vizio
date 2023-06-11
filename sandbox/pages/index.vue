<template>
  <div class="wrapper">
    <div class="container">
      <CodeExample />
      <CodeMirror :code="code" />
    </div>
    <button class="button" @click="onSubmit">Generate</button>
    <div class="container">
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

    onSubmit() {
      this.$axios
        .$post('/generate_viz_devs', { source_code: this.code })
        .then((res) => {
          console.log(res)
          this.dot = res
        })
        .catch((err) => {
          console.log(err)
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

.button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
