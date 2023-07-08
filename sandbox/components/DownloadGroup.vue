<template>
  <div class="group-list">
    <button :disabled="isLoading || isFailed || !dot" @click="downloadSvg">
      Download SVG
    </button>
  </div>
</template>

<script>
export default {
  name: 'DownloadGroup',

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

  methods: {
    downloadSvg() {
      if (this.isLoading || this.isFailed || this.dot === '') return

      // eslint-disable-next-line no-undef
      const svg = Viz(this.dot, { format: 'svg' })
      const svgBlob = new Blob([svg], { type: 'image/svg+xml;charset=utf-8' })
      const svgUrl = URL.createObjectURL(svgBlob)
      const downloadLink = document.createElement('a')
      downloadLink.href = svgUrl
      downloadLink.download = 'flowchart.svg'
      document.body.appendChild(downloadLink)
      downloadLink.click()
      document.body.removeChild(downloadLink)
    },
  },
}
</script>

<style>
.group-list {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
</style>
