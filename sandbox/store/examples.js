import data from '~/static/data/examples.json'

export const state = () => ({
  list: data,
  active: 0
})

export const mutations = {
  setActive(state, index) {
    state.active = index
  },
}
