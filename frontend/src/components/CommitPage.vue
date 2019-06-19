<template>
  <div class="container">
    <h1>Commits</h1>
    
    <button v-on:click="syncCommits(true)">Sync</button>
    <input v-model="author" placeholder="Filter by author">

    <h2>Github (pytest-dev/pytest)</h2>
    <table>
      <thead><tr>
        <th v-for="key in cols.github" v-bind:key="key">
          {{ key }}
        </th>
      </tr></thead>
      <tbody>
        <tr v-for="commit in commits.github" v-bind:key="commit.sha">
          <td v-for="key in cols.github" v-bind:key="key">
            {{commit[key]}}
          </td>
        </tr>
      </tbody>
    </table>

    <h2>Bitbucket (biobakery/halla/commits)</h2>
    <table>
      <thead><tr>
        <th v-for="key in cols.bitbucket" v-bind:key="key">
          {{ key }}
        </th>
      </tr></thead>
      <tbody>
        <tr v-for="commit in commits.bitbucket" v-bind:key="commit.sha">
          <td v-for="key in cols.bitbucket" v-bind:key="key">
            {{commit[key]}}
          </td>
        </tr>
      </tbody>
    </table>
  
  </div>
</template>

<script lang="ts">

// calling the backend directly from a vue component is a bad example, 
// this is here just to demonstrate the backend loading data
import axios from 'axios';

export default {
  name: 'CommitPage',
  data: function() {
    return  {
      response: [],
      commits: {bitbucket: [], github: []},
      cols:    {bitbucket: [], github: []},
      author:  '',
    }
  },
  created: function(){
    this.syncCommits();
    this.syncCommits(true);
  },
  methods: {
    syncCommits(reload=false) {
      const params = {};
      if (reload) {
        params.reload = '';
      }
      if (this.author !== '') {
        params.author = this.author;
      }
      axios.get('http://0.0.0.0:8000/api/commits/bitbucket', { params }).then(response => {
        const data = response.data;
        this.commits.bitbucket = data;
        if (data.length) {
          this.cols.bitbucket = Object.keys(data[0]);
        }
      });
      axios.get('http://0.0.0.0:8000/api/commits/github', { params }).then(response => {
        const data = response.data;
        this.commits.github = data;
        if (data.length) {
          this.cols.github = Object.keys(data[0]);
        }
      });
    }
  }
}
</script>

<style lang="scss" scoped>
  h1 {
    text-align: center;
  }
</style>
