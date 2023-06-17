<template>
  <codemirror
    :model-value="code"
    placeholder="Code goes here..."
    :style="{ height: '100%' }"
    :autofocus="true"
    :extensions="extensions"
    @change="formValue = $event"
  />
</template>

<script>
import { Codemirror } from 'vue-codemirror'
import { python } from '@codemirror/lang-python'

export default {
  name: 'CodeMirror',

  components: {
    Codemirror,
  },

  props: {
    code: {
      type: String,
      default: '',
    },
  },

  data() {
    return {
      extensions: [python()],
    }
  },

  computed: {
    formValue: {
      get() {
        return this.code
      },
      set(value) {
        this.$emit('update:code', value)
      },
    },
  },
}
</script>

<style>
.cm-editor {
  background-color: white;
  border: 1px solid #1ca6e9;
  height: 100%;
}

.ͼ1.cm-focused {
  outline: none;
}

.ͼ2 .cm-gutters {
  background-color: #e6f4ff;
}
</style>
