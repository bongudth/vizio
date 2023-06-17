<template>
  <div class="example-list">
    <div v-for="(example, index) in examples" :key="index" class="example-item">
      <button
        :class="['example-button', { active: index === active }]"
        @click="setActive(index)"
      >
        {{ example.id }}
      </button>
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  name: 'CodeExample',

  computed: {
    examples() {
      return this.$store.state.examples.list
    },

    active() {
      return this.$store.state.examples.active
    },
  },

  methods: {
    ...mapMutations('examples', ['setActive']),
  },
}
</script>

<style>
.example-list {
  display: flex;
  gap: 10px;
}
</style>
