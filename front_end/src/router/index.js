import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import vueDet from '@/components/vue_det'
import About from '@/components/about'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/vue_det',
      name: 'vue_det',
      component: vueDet
    },
    {
      path: '/about',
      name: 'about',
      component: About
    }
  ]
})
