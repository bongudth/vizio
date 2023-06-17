<template>
  <div class="group-list">
    <button @click="downloadSvg">Download SVG</button>
  </div>
</template>

<script>
export default {
  name: 'DownloadGroup',

  props: {
    dot: {
      type: String,
      default: '',
    },
  },

  methods: {
    downloadSvg() {
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
