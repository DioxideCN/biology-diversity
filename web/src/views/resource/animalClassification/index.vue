<template>
  <ScrollContainer>
    <div ref="wrapperRef" :class="prefixCls">
      <Tabs tab-position="left" :tabBarStyle="tabBarStyle" >
        <TabPane key="1" tab="界" > <kingdom></kingdom> </TabPane>
        <TabPane key="2" tab="门" > <phylum></phylum> </TabPane>
        <TabPane key="3" tab="亚门" > <subphylum></subphylum> </TabPane>
        <TabPane key="4" tab="纲" > <classes></classes> </TabPane>
        <TabPane key="5" tab="亚纲" > <subclass></subclass> </TabPane>
        <TabPane key="6" tab="目" > <order></order> </TabPane>
        <TabPane key="7" tab="亚目" > <suborder></suborder> </TabPane>
        <TabPane key="8" tab="科" > <family></family> </TabPane>
        <TabPane key="9" tab="亚科" > <subfamily></subfamily> </TabPane>
        <TabPane key="10" tab="种" > <species></species> </TabPane>
        <TabPane key="11" tab="亚种" > <subspecies></subspecies> </TabPane>
        <TabPane key="12" tab="族" > <tribr></tribr> </TabPane>
      </Tabs>
    </div>
  </ScrollContainer>
</template>

<script lang="ts">
  import { defineComponent } from 'vue';
  import { Tabs } from 'ant-design-vue';
  import { ScrollContainer } from '/@/components/Container';
  import { settingList } from './data';
  

  import kingdom from './type/kingdom/kingdom.vue';
  import phylum from './type/phylum/phylum.vue';
  import subphylum from './type/subphylum/subphylum.vue';
  import classes from './type/class/class.vue';
  import subclass from './type/subclass/subclass.vue';
  import order from './type/order/order.vue';
  import suborder from './type/suborder/suborder.vue';
  import subfamily from './type/subfamily/subfamily.vue';
  import subspecies from './type/subspecies/subspecies.vue';
  import family from './type/family/family.vue';
  import tribr from './type/tribr/tribr.vue';
  import species from './type/species/species.vue';


  

  export default defineComponent({
    name: 'animal',
    components: {
      ScrollContainer,
      Tabs,
      TabPane: Tabs.TabPane,
      kingdom,
      phylum,
      subphylum,
      classes,
      subclass,
      order,
      suborder,
      family,
      subfamily,
      species,
      subspecies,
      tribr,
      
    },
    setup() {
      // function search(){
      //   getList().then((res)=>{
      //     console.log(res)
      //   })
      // }
      

      return {
        prefixCls: 'account-setting',
        settingList,
        tabBarStyle: {
          width: '220px',
        },
      };
    },
  });
</script>
<style lang="less">
  .account-setting {
    margin: 12px;
    background-color: @component-background;

    .base-title {
      padding-left: 0;
    }

    .ant-tabs-tab-active {
      background-color: @item-active-bg;
    }
  }
</style>
