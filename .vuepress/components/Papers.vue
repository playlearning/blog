<template>
  <div :id="topic_id">
    <div class="topic_head">
      <p class="title is-4">
        <a class="has-text-black" :href="'#' + topic_id">Topic: {{ paper_list.topic }}</a>
      </p>
      <p>
        <span class="button is-light is-small" v-on:click="toggle_verbose">
          <span v-if="is_verbose" class="verbose-text">Hide</span>
          <span v-else class="verbose-text">Show</span>
          Detail
        </span>
        <a class="button is-small is-light btn-link" :href="src" target="_blank">
            YAML &nbsp;
            <i class="fas fa-cogs"></i>
        </a>
        <a class="button is-small is-light btn-link" href="https://github.com/playlearning/blog/tree/master/.vuepress/public/yaml/papers" target="_blank">
            Download Papers in List &nbsp;
            <i class="fas fa-download"></i>
        </a>
      </p>
      <p class="title is-5" v-if="Object.keys(tasks).length">Tasks</p>
      <div class="field is-grouped is-grouped-multiline">
        <div class="control" v-for="(c, t) in tasks">
          <div class="tags has-addons">
            <span class="tag">{{ t }}</span>
            <span class="tag has-background-grey-lighter">{{ c }}</span>
          </div>
        </div>
      </div>
      <p class="title is-5">Resources</p>
      <ol>
        <li v-for="(p, index) in papers">
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
          <div v-if="is_verbose && has_detail(p)" class="detail">
            <div>
              <div v-if="p.questions" class="media">
                <div class="media-left">
                  <i class="far fa-question-circle is-size-5"></i>
                </div>
                <div class="media-content">
                  <ol>
                    <li v-for="(q, index) in p.questions">
                      {{ q }}
                    </li>
                  </ol>
                </div>
              </div>
              <div v-if="p.tasks" class="media">
                <div class="media-left">
                  <i class="fas fa-crosshairs is-size-5"></i>
                </div>
                <div class="media-content">
                  <ol>
                    <li v-for="(t, index) in p.tasks">
                      {{ t.name }}
                    </li>
                  </ol>
                </div>
              </div>
            </div>
          </div>
        </li>
      </ol>
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
    },
    tasks: function() {
      var res = {}
      if (this.paper_list.papers) {
        for (const p of this.paper_list.papers) {
          if (p.tasks) {
            for (const t of p.tasks) {
              if (t.name in res) {
                res[t.name] += 1
              } else {
                res[t.name] = 1
              }
            }
          }
        }
      }
      return res
    }
  },
  methods: {
    toggle_verbose: function() {
      this.is_verbose = !this.is_verbose
    },
    has_detail: function(p) {
      return !!(p.questions || p.tasks);
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
  margin: 0 2.5em;
  padding: 0.5em;
  border-radius: 3px;
}
ol {
  list-style-type: none !important;
  counter-reset: elementcounter;
  margin-top: 0;
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
.media-content ol {
  margin-left: 0;
}
.media-content {
  border-left: 1px solid #eee;
}
.verbose-text {
    width: 2.8em;
}
</style>
