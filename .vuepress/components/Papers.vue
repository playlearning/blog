<template>
  <div :id="topic_id">
    <div class="topic_head">
      <p class="title is-4">
        <a class="has-text-black" :href="'#' + topic_id">Topic: {{ paper_list.topic }}</a>
      </p>
      <p>
        <span class="button is-small" v-on:click="toggle_verbose">
          <span v-if="is_verbose">Hide</span>
          <span v-else>Show</span>
          Detail
        </span>
        <a class="button is-small btn-link" :href="src" target="_blank">YAML</a>
        <a class="button is-small btn-link" href="https://github.com/playlearning/blog/tree/master/.vuepress/public/yaml/papers" target="_blank">Download Papers in List</a>
      </p>
      <p class="title is-5">Resources</p>
      <ol>
        <li v-for="(p, index) in papers">
          <!--<span class="index">-->
            <!--{{index+1}}.-->
          <!--</span>-->
          <span v-bind:class="{ stress: p.stress }">
            <span v-if="p.date">[{{ new Date(String(p.date)).getFullYear() }}]</span>
            <a v-if="p.link" :href="p.link" target="_blank">{{ p.title }}</a>
            <span v-else>{{ p.title }}</span>
            <a v-if="p.pdf" :href="p.pdf" target="_blank"><i class="far fa-file-pdf is-size-7 has-text-black"></i></a>
          </span>
          <span v-if="p.code">
              <a :href="p.code" target="_blank"><i class="far fa-file-code has-text-black is-size-7"></i></a>
          </span>
          <span v-if="p.proceeding" class="has-text-grey is-size-7 is-italic has-text-weight-semibold">{{ p.proceeding }}</span>
          <div v-if="is_verbose" class="has-background-light">
            <div v-if="p.questions">
              <p class="title is-6">Questions:</p>
              <ol>
                <li v-for="(q, index) in p.questions">
                  <!--<strong>{{ index+1 }}.</strong>-->
                  {{ q }}
                </li>
              </ol>
            </div>
          </div>
        </li>
      </ol>
      <div v-if="paper_list.tasks && paper_list.tasks.length">
        <p>
          <strong><span class="title is-5">Tasks</span></strong>
        </p>
        <ol>
          <li v-for="(t, index) in paper_list.tasks">
            <!--<span class="index">-->
              <!--{{index+1}}.-->
            <!--</span>-->
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
        </ol>
      </div>
      <div v-if="references.length">
        <p class="title is-5">References</p>
        <ol class="ref-list">
          <li v-for="(r, index) in references">
            <a v-if="r.link" :href="r.link" target="_blank" >{{ r.title }}</a>
            <span v-else>{{ r.title }}</span>
            </span>
          </li>
        </ol>
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
.btn-link {
  text-decoration: none !important;
}
.stress {
  font-weight: bold;
}
.index {
  float: left;
  width: 2em;
  font-weight: bold;
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
ol {
  list-style-type: none !important;
  counter-reset: elementcounter;
}
ol > li:before {
  display: inline-block;
  min-width: 2em;
  content: counter(elementcounter) ".";
  counter-increment:elementcounter;
  font-weight: 600;
  text-align: right;
  margin-right: 0.5em;
}
.ref-list li:before {
  content: "["counter(elementcounter) "] ";
}
.topic_head {
  margin-top: 1em;
}
</style>
