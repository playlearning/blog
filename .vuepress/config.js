module.exports = {
    title: 'Mr.Blue\'s Blog',
    head: [
        ['link', {rel: 'icon', href: '/imgs/shuttlecock-transparent-small.png' }],
        ['link', {rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.min.css'}],
        ['link', {rel: 'stylesheet', href: 'https://use.fontawesome.com/releases/v5.8.2/css/all.css', integrity: 'sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay', crossorigin: 'anonymous'}]
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
