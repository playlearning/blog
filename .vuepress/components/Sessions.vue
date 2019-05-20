<template>
    <table>
        <thead>
            <tr>
                <th>Event</th>
                <th>Date</th>
                <th>Description</th>
                <th>Session Materials</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="s in topic.sessions">
                <td>{{ s.event }}</td>
                <td>{{ s.date}}</td>
                <td>
                    {{ s.title }}
                </td>
                <td>
                    <ul style="margin-block-start: 0">
                        <li v-bind:class="{ stress: p.stress }" v-for="p in s.papers">
                            <span v-if="p.year || p.remark">[</span><span v-if="p.year">{{ p.year }}</span><span v-if="p.year && p.remark">, </span><span v-if="p.remark">{{ p.remark }}</span><span v-if="p.year || p.remark">]</span>
                            <a v-if="p.link" :href="p.link">{{ p.title }}</a>
                            <span v-else>{{ p.title }}</span>
                            <a v-if="p.pdf" :href="p.pdf" target="_blank"><i class="far fa-file-pdf is-size-7 has-text-black"></i></a>
                        </li>
                    </ul>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import axios from 'axios'
import yaml from 'js-yaml'

export default {
    data () {
        return {
            topic: '',
        }
    },
    props: ['src'],
    mounted () {
        axios.get(this.src)
            .then(response => (
                this.topic = yaml.safeLoad(response.data)
            ))
    }
}
</script>

<style scoped>
.stress {
    font-weight: bold;
}
</style>
