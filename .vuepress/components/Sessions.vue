<template>
    <table class="table">
        <thead>
            <tr class='active'>
                <th class="col">Event</th>
                <th class="col">Date</th>
                <th class="col">Description</th>
                <th class="col">Session Materials</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="s in topic.sessions">
                <td scope="row">{{ s.event }}</td>
                <td>{{ s.date}}</td>
                <td>
                    {{ s.title }}
                </td>
                <td>
                    <ul style="margin-block-start: 0">
                        <li v-bind:class="{ stress: p.stress }" v-for="p in s.papers">
                            <span v-if="p.year || p.remark">[</span><span v-if="p.year">{{ p.year }}</span><span v-if="p.year && p.remark">, </span><span v-if="p.remark">{{ p.remark }}</span><span v-if="p.year || p.remark">]</span>
                            <a :href="p.link">{{ p.title }}</a>
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

<style>
.stress {
    font-weight: bold;
}
</style>
