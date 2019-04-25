module.exports = {
    title: 'Mr.Blue\'s Blog',
    head: [
        ['link', {rel: 'icon', href: '/shuttlecock-transparent-small.png' }],
        ['link', {rel: 'stylesheet', href: '/css/bootstrap.min.css'}]
    ],
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
