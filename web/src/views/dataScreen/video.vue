<template>
  <div>
    <div class="stream" v-for="(item,index) in videos" :key="index" @click="showModal2(item.living_url)">
      <div class="zhibo1"  style="margin-bottom: 8px;" >
      <div>
        <iframe
        v-if="update"
        :class="video[index]"
        :src= "item.living_url"
        width="195"
        height="120"
        allow="autoplay"
      ></iframe>
      </div>
       <div :class="videoText[index]" >
        {{item.name}}
      </div> 
    </div>
    
  </div>
  <pointModal v-model:visible="visible6" title="视频直播" style="width: 900px" @cancel="handelCancel" >
        <iframe
        v-if="reFresh"
        id="video"
        :src= "card.living_url"
        width="800px"
        height="450px"
        style="margin:10px auto"
        allow="autoplay"
      ></iframe>
    </pointModal>
  </div>
</template>

<script setup lang="ts">
import { inject, ref, onMounted, onDeactivated, reactive ,nextTick, watchEffect} from 'vue';
import {GetStream} from './api';
import pointModal from './pointModal.vue'
const timer = ref(0);
const index = ref(0);
const reFresh = ref<boolean>(true);
const card = ref({living_url:'',});
const handelCancel = (e: MouseEvent) => {
  visible6.value = false;
  // console.log('90',visible6,e);
};
const visible6 = ref<boolean>(false);
const update = ref<boolean>(true);
let videos = ref([]);

function showModal2(living_url){
  card.value.living_url=living_url;
  visible6.value = true;
  // console.log('66',card.value.living_url);
  document.getElementById('video').contentWindow.location.reload(true);
};

// const living_url2 = ref();
const videoText = reactive(['videoText','videoText02']);
const video = reactive(['video','video02']);
GetStream().then((res) => {
    videos.value = res.qs;
    
    // console.log('11',res);
    
    
  });
  watchEffect(()=>{
    // console.log('00',card.value.living_url);
      reFresh.value = false;
      nextTick(() => {
                reFresh.value = true
            })
  })

timer.value = window.setInterval(function logname() {
  // 其他定时执行的方法
    function reload() {
            // 移除组件
            update.value = false,
            // console.log('更新了');
            // 在组件移除后，重新渲染组件
            // this.$nextTick可实现在DOM 状态更新后，执行传入的方法。
            nextTick(() => {
                update.value = true
            })
        }
  return reload();
 
}, 20000);
onMounted(() => {
  GetStream();
  
});
onDeactivated(() => {
  //离开当前组件的生命周期执行的方法
  window.clearInterval(timer.value);
});
</script>

<style >
* {
  margin: 0;
  padding: 0;
}
.video{
  float: left;
}
.video02 {
  float: right;
  background-color: rgb(30, 97, 50);
}
.zhibo1 {
  width: 320px;
  height: 120px;
  background-color: rgb(30, 97, 50);
}
.videoText{
   color: white;
   padding-top: 12%;
   text-align: center;
   font-size: 15px; 
   float: right;
   width: 105px;
   margin: 0 10px;
}

.videoText02{
  color: white;
  text-align: center;
  padding-top: 12%;
  font-size: 15px;
  width: 105px;
  margin: 0 10px;
}
</style>