import Vue from 'vue';

import AppComponent from './components/app-component/app-component';


var app = new Vue({
  el: '#app',
  components: {
    'app-component': AppComponent
  }
});
