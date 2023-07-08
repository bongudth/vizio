<template>
  <div class="flowchart-container">
    <div id="flowchart" :class="{ hidden: isLoading || isFailed }"></div>
    <div v-if="isLoading && !isFailed" class="loading-text">Loading...</div>
    <div v-if="isFailed && !isLoading" class="fail-text">Something went wrong!</div>
  </div>
</template>

<script>
export default {
  name: 'FlowChart',

  props: {
    isLoading: {
      type: Boolean,
      default: false,
    },

    isFailed: {
      type: Boolean,
      default: false,
    },

    dot: {
      type: String,
      default: '',
    },
  },

  watch: {
    dot: {
      immediate: true,
      handler(dotString) {
        if (this.isLoading || dotString === '') return

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
.flowchart-container {
  border: 1px solid #1ca6e9;
  position: relative;
}

.flowchart-container,
#flowchart {
  height: 100%;
  max-height: 100%;
  overflow-y: scroll;
}

#flowchart,
svg {
  width: 100%;
  height: 100%;
}

#flowchart.hidden {
  visibility: hidden;
}

.loading-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.fail-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: red;
}
</style>
