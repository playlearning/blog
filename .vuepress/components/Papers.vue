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
            <span class="tag button is-light">{{ t }}</span>
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
              <div v-if="p.description">
                <div class="column">
                  <i class="far fa-comment-dots"></i>
                  &nbsp;
                  {{ sentence(p.description) }}
                </div>
              </div>
              <div class="columns">
                <div class="column" v-if="p.tasks">
                    <div class="media-content">
                        <div v-for="(t, index) in p.tasks">
                          <div class="tag">
                            <i class="fas fa-crosshairs"></i>
                            &nbsp;
                            {{ t.name }}
                          </div>
                          <div class="tags" v-if="t.datasets">
                            <span v-for="d in t.datasets" class="is-size-7 tag is-white">
                              <a :href="d.link" :class="['has-text-grey', 'btn-link', 'is-tooltip-right', d.target ? ' tooltip' : '']" :data-tooltip="d.target" target="_blank">
                                <i class="fas fa-database"></i>
                                &nbsp;
                                <span v-if="d.abbr">{{ d.abbr }}</span>
                                <span v-else="d.abbr">{{ d.name }}</span>
                              </a>
                            </span>
                          </div>
                        </div>
                    </div>
                </div>
                <div class="column" v-if="p.questions">
                    <div class="media-content">
                      <div v-for="(q, index) in p.questions">
                        <div class="tag">
                          <i class="far fa-question-circle"></i>
                          &nbsp;
                          {{ q }}
                        </div>
                        <div></div>
                      </div>
                    </div>
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
      is_verbose: false,
      active_tasks : []
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
        var res = this.active_tasks.length ? this.active_papers : this.paper_list.papers;
        return res.sort(
          (b, a) => new Date(String(a.date)) - new Date(String(b.date)))
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
    },
    sentence: function(raw) {
      raw = raw.trim()
      var res = raw.charAt(0).toUpperCase() + raw.slice(1)
      if (![',', '.', '!', '?'].includes(res.charAt(res.length-1))) {
        console.log(res)
        console.log(res.charAt(res.length-1))
        res += '.'
      }
      return res
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
  font-size: 0.9em;
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
  border-left: 1px solid #ccc;
}
.verbose-text {
  width: 2.8em;
}
</style>
