<template>
  <div class="posts" v-if="posts.length">
    <ul class="post" v-for="post in posts">
        <div v-if="post.title">
            <li>
              <router-link :to="post.path">
                {{post.title}}
              </router-link>
            </li>
        </div>
    </ul>
  </div>
</template>

<script>
export default {
  props: ["page"],
  computed: {
    posts() {
      let currentPage = this.page ? this.page : this.$page.path;
      let posts = this.$site.pages
        .filter(x => {
          return x.path.match(new RegExp(`(${currentPage})`));
        })
        .sort((a, b) => {
          return new Date(b.frontmatter.date) - new Date(a.frontmatter.date);
        });
      return posts;
    }
  }
};
</script>
