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
        this.generatePanZoom()
      },
    },
  },

  methods: {
    generateSvg(dotString) {
      // eslint-disable-next-line no-undef
      const svg = Viz(dotString, { format: 'svg' })
      document.getElementById('flowchart').innerHTML = svg
    },

    generatePanZoom() {
      // eslint-disable-next-line no-undef
      svgPanZoom('#flowchart svg', {
        zoomEnabled: true,
        controlIconsEnabled: true,
        fit: true,
        center: true,
      })
    },
  },
}
</script>

<style>
#flowchart {
  border: 1px solid #1ca6e9;
  max-height: 100%;
  overflow-y: scroll;
}

#flowchart,
svg {
  width: 100%;
  height: 100%;
}
</style>
