module.exports = {
    title: 'Mr.Blue\'s Blog',
    head: [
        ['link', {rel: 'icon', href: '/imgs/shuttlecock-transparent-small.png' }],
        ['link', {rel: 'stylesheet', href: '/css/bulma.min.css'}],
        ['link', {rel: 'stylesheet', href: '/css/bulma-tooltip.min.css'}],
        ['link', {rel: 'stylesheet', href: '/css/all.min.css'}]
    ],
    themeConfig: {
        sidebar: false
    },
    markdown: {
        linkify: true
    },
    plugins: [
        [
            '@vuepress/google-analytics',
            {
                'ga': 'UA-138694157-1'
            }
        ]
    ]
}
