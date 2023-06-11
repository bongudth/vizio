<template>
  <div>
    {{ dot }}
  </div>
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
}
</script>
