<template>
  <div class="posts" v-if="posts.length">
    <ul>
        <li v-if="post.title" class="post" v-for="post in posts">
          <router-link :to="post.path">
            {{post.title}}
          </router-link>
        </li>
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
          return b > a;
        });
      return posts;
    }
  }
};
</script>
