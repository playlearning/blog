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
            <tr v-for="s in items">
                <td scope="row">{{ s.event }}</td>
                <td>{{ s.date}}</td>
                <td>
                    <strong>{{ s.description }}</strong>
                </td>
                <td>
                    <ul style="margin-block-start: 0">
                        <li v-for="p in s.readings">
                            <span v-if="p.year || p.remark">[</span><span v-if="p.year">{{ p.year }}</span><span v-if="p.year && p.remark">,</span>
                            <span v-if="p.remark">{{ p.remark }}</span><span v-if="p.year || p.remark">]</span>
                            <a :href="p.link">{{ p.title }}</a>
                        </li>
                    </ul>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import sessions from './json/sessions.json'

export default {
    data () {
        return {
            items: sessions
        }
    }
}
</script>
