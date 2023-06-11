<template>
  <div id="flowchart"></div>
</template>

<script>
export default {
  name: 'FlowChart',

  props: {
    dot: {
      type: String,
      default: '',
    },
  },

  watch: {
    dot: {
      immediate: true,
      handler(dotString) {
        if (dotString === '') return

        this.generateSvg(dotString)
      },
    },
  },

  methods: {
    generateSvg(dotString) {
      // eslint-disable-next-line no-undef
      const svg = Viz(dotString, { format: 'svg' })
      document.getElementById('flowchart').innerHTML = svg
    },
  },
}
</script>

<style>
#flowchart,
svg {
  width: 100%;
  height: 100%;
}
</style>
