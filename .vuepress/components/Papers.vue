<template>
  <div class="paper">
    <div class="topic_head">
      <p>
        <strong>
          <a class="topic" :id="topic_id" :href="'#' + topic_id">Topic: {{ paper_list.topic }}</a>
        </strong>
      </p>
      <span class="btn_verbose" v-on:click="toggle_verbose">
        <span v-if="is_verbose">Hide</span>
        <span v-else>Show</span>
        Detail
      </span>
      <a class="link" :href="src" target="_blank">YAML</a>
      <a class="link" href="https://github.com/playlearning/blog/tree/master/.vuepress/public/yaml/papers" target="_blank">Download Papers in List</a>
    </div>
    <div class="topic_body">
      <p>
        <strong><span class="section">Resources</span></strong>
      </p>
      <ul>
        <li v-for="(p, index) in papers">
          <span class="index">
            {{index+1}}.
          </span>
          <span class="title" v-bind:class="{ stress: p.stress }">
            <span v-if="p.date">[{{ new Date(String(p.date)).getFullYear() }}]</span>
            <a v-if="p.link" :href="p.link" target="_blank">{{ p.title }}</a>
            <span v-else-if="p.pdf" >
              <a :href="p.pdf" target="_blank">{{ p.title }}</a>
              <span class="pdf">pdf</span>
            </span>
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
      <div v-if="paper_list.tasks && paper_list.tasks.length">
        <p>
          <strong><span class="section">Tasks</span></strong>
        </p>
        <ul class="references">
          <li v-for="(t, index) in paper_list.tasks">
            <span class="index">
              {{index+1}}.
            </span>
            <span>{{ t.name }}</span>
            <div v-if="t.datasets && t.datasets.length" >
              <ul>
                <li v-for="(d, index) in t.datasets">
                  <a :href="d.link">
                    <span v-if="d.abbr">{{ d.abbr}}</span>
                    <span v-else>{{ d.name }}</span>
                  </a>
                </li>
              </ul>
            </div>
          </li>
        </ul>
      </div>
      <div v-if="references.length">
        <p>
          <strong><span class="section">References</span></strong>
        </p>
        <ul class="references">
          <li v-for="(r, index) in references">
            <span class="index">
              [{{index+1}}]
            </span>
            <a v-if="r.link" :href="r.link" target="_blank" >{{ r.title }}</a>
            <span v-else>{{ r.title }}</span>
            </span>
          </li>
        </ul>
      </div>
    </div>
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
    },
    references: function() {
      if (this.paper_list.references) {
        return this.paper_list.references
      } else {
        return []
      }
    },
    topic_id: function() {
      if (this.paper_list.topic) {
        return this.paper_list.topic.toLowerCase().split(' ').join('-')
      } else {
        return ''
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
  color: inherit;
  padding-top: 4.6rem;
}
.btn_verbose, .link{
  width: fit-content;
  text-align: center;
  padding: 2px;
  margin-right: 1.5em;
  cursor: pointer;
}
.btn_verbose {
  border-bottom: 1px dotted #333;
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
  font-weight: bold;
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
.references {
  font-size: 0.95em;
}
.section {
  font-size: 1.2em;
}
.topic_body {
  padding-left: 1em;
}
.pdf {
  font-size: 0.7em;
  color: #aaa;
  font-style: italic;
  font-weight: 700;
}
</style>
