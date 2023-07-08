<template>
  <div class="example-list">
    <div v-for="(example, index) in examples" :key="index" class="example-item">
      <button
        :class="['example-button', { active: index === active }]"
        :disabled="isLoading"
        @click="changeExample(index)"
      >
        {{ example.id }}
      </button>
    </div>

    <!-- <div class="example-list">
      <label class="switch">
        <input v-model="isSummaryValue" type="checkbox" />
        <span class="slider round"></span>
      </label>
      <div>Summary code</div>
    </div> -->
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  name: 'CodeExample',

  props: {
    isLoading: {
      type: Boolean,
      default: true,
    },

    isSummary: {
      type: Boolean,
      default: false,
    },
  },

  computed: {
    examples() {
      return this.$store.state.examples.list
    },

    active() {
      return this.$store.state.examples.active
    },

    isSummaryValue: {
      get() {
        return this.isSummary
      },
      set(value) {
        this.$emit('update:isSummary', value)
      },
    },
  },

  methods: {
    ...mapMutations('examples', ['setActive']),

    changeExample(index) {
      if (this.isLoading) return

      this.setActive(index)
    },
  },
}
</script>

<style>
.example-list {
  display: flex;
  align-items: center;
  gap: 10px;
}

.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  min-width: 60px;
  height: 30px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: white;
  border: 1px solid #1877f2;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

.slider:before {
  position: absolute;
  content: '';
  height: 24px;
  width: 24px;
  left: 2px;
  bottom: 2px;
  background-color: #1877f2;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

input:checked + .slider {
  background-color: #1877f2;
}

input:focus + .slider {
  box-shadow: 0 0 1px #1877f2;
}

input:checked + .slider:before {
  background-color: white;
  -webkit-transform: translateX(30px);
  -ms-transform: translateX(30px);
  transform: translateX(30px);
}

.slider.round {
  border-radius: 30px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>
