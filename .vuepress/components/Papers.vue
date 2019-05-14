<template>
  <div class="paper">
    <p>
      <strong><span class="topic">Topic: {{ paper_list.topic }}</span></strong>
    </p>
    <span class="btn_verbose" v-on:click="toggle_verbose">
      <span v-if="is_verbose">Hide</span>
      <span v-else>Show</span>
      Detail
    </span>
    <a class="yaml" :href="src" target="_blank">YAML</a>
    <a class="yaml" href="https://github.com/playlearning/blog/tree/master/.vuepress/public/yaml/papers" target="_blank">Download Papers</a>
    <ul>
      <li v-for="(p, index) in papers">
        <span class="index">
          {{index+1}}.
        </span>
        <span class="title" v-bind:class="{ stress: p.stress }">
          [{{ new Date(String(p.date)).getFullYear() }}]
          <a v-if="p.link" :href="p.link" target="_blank" alt="List is rendered from this YAML file.">{{ p.title }}</a>
          <span v-else>{{ p.title }}</span>
        </span>
        <span v-if="p.proceeding" class="proceeding">{{ p.proceeding }}</span>
        <div v-if="is_verbose" class="detail">
          <span v-if="p.code">
            <a :href="p.code" target="_blank">[Code]</a>
          </span>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import yaml from 'js-yaml'

export default {
  data () {
    return {
      paper_list: {},
      is_verbose: false
    }
  },
  props: {
    src: String,
    verbose: Boolean
  },
  mounted () {
    axios.get(this.src)
      .then(response => (
        this.paper_list = yaml.safeLoad(response.data)
      )
    )
    this.is_verbose = this.verbose
  },
  computed: {
    papers: function() {
      if (this.paper_list.papers) {
        return this.paper_list.papers.sort(
          (a, b) => new Date(String(a.date)) - new Date(String(b.date)))
      } else {
        return []
      }
    }
  },
  methods: {
    toggle_verbose: function() {
      this.is_verbose = !this.is_verbose
    }
  }
}
</script>

<style scoped>
.topic {
  font-size: 1.2em;
}
.btn_verbose, .yaml {
  width: fit-content;
  text-align: center;
  padding: 2px;
  margin-right: 1.5em;
  border-bottom: 1px dotted #333;
  cursor: pointer;
}
.stress {
  font-weight: bold;
}
ul li {
  list-style: none;
}
.index {
  float: left;
  width: 2em;
}
.icon {
  width: 24px;
}
.proceeding {
  color: #777;
  font-style: italic;
  font-size: 0.8em;
  font-weight: 600;
  margin-left: 0.5em;
}
.detail {
  padding: 0em 2em;
  background: #f8f8f8;
  border-radius: 3px;
}
</style>
