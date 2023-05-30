<template>
 <div class="wrap">  
 <div style="height:20px;"></div>
      <div style="display: flex;">
        <div style="width: 30px;"></div>
        <div style="background-color: white;width: 800px;height: 300px;">
              <div style="height:60px;"></div>
            <div style="display: flex;">  <div style="width: 20px;"></div>  <div>设备名称:</div>  <div style="width: 20px;"></div>  <el-input style="width: 200px;height: 28px;"/> 
                                           <div style="width: 40px;"></div>
                                          <div style="width: 20px;"></div>  <div>所属组别:</div>  <div style="width: 20px;"></div>  <el-input style="width: 200px;height: 28px;"/>
             </div>
             <div style="height:60px;"></div>
            <div style="display: flex;">  <div style="width: 20px;"></div>  <div>&nbsp&nbsp&nbsp&nbsp型号:&nbsp&nbsp&nbsp</div>  <div style="width: 20px;"></div>  <el-input style="width: 200px;height: 28px;"/> 
                                          <div style="width: 40px;"></div>
                                          <div style="width: 20px;"></div>  <div>监控范围:</div>  <div style="width: 20px;"></div>  <el-input style="width: 200px;height: 28px;"/>
             </div>
            
          <div></div>
        </div>
       <div style="background-color: white;width: 430px;height: 300px;display: flex;" >
         <div style="display: block;">
          <div style="height:20px;"></div>
          <el-input style="width: 300px;height: 200px;"/>
         </div>
         
       </div>  
      </div>  
      
      
      
       <div style="height: 60px;width: 10px;"></div>
      <div style="display: flex;">
        <div style="width: 30px;"></div>
        <div style="background-color: white;width: 1230px;height: 600px;">
              <div style="height:60px;"></div>
            <div style="display: flex;">  <div style="width: 20px;"></div>  <div style="font-size: 30px;: 20px;">组别信息</div>  
          
             </div>
             <div style="height:60px;"></div>
            <div style="display: flex;">  <div style="width: 20px;"></div>  <div>&nbsp&nbsp&nbsp&nbsp型号:&nbsp&nbsp&nbsp</div>  <div style="width: 20px;"></div>  <el-input style="width: 200px;height: 28px;"/> 
                                          <div style="width: 40px;"></div>
                                          <div style="width: 20px;"></div>  <div>监控范围:</div>  <div style="width: 20px;"></div>  <el-input style="width: 200px;height: 28px;"/>
             </div>
             <div style="height:20px;"></div>
            <div style="display: flex;">  <div style="width: 20px;"></div>  <div>&nbsp&nbsp&nbsp&nbsp型号:&nbsp&nbsp&nbsp</div>  <div style="width: 20px;"></div>  <el-input style="width: 200px;height: 28px;"/>
                                        
             </div>
             <div style="height:60px;"></div>
            <div style="display: flex;">  <div style="width: 20px;"></div>  <div style="font-size: 30px;: 20px;">组别信息</div>
                
                      
             </div>
             <div style="height:40px;"></div>
              <div style="display: flex;">   <div style="width: 20px;"></div> 
              <el-tag
                                  v-for="tag in tags"
                                  :key="tag.name"
                                  class="mx-1"
                                  closable
                                  :type="tag.type"
                                  size="large"
                                >
                                  {{ tag.name }}
                                </el-tag>      
               </div>
               <div style="height:20px;"></div>
                <div style="display: flex;">   <div style="width: 20px;"></div> 
                <el-tag
                                    v-for="tag in tagse"
                                    :key="tag.name"
                                    class="mx-1"
                                    closable
                                    :type="tag.type"
                                    size="large"
                                  >
                                    {{ tag.name }}
                                  </el-tag>      
                 </div>
                 <div style="height:20px;"></div>
                  <div style="display: flex;">   <div style="width: 20px;"></div> 
                  <el-input style="height:28px;width: 80px"></el-input>
                  <div style="width: 20px;"></div>
                  <div>至</div>
                  <div style="width: 20px;"></div>
                  <el-input style="height:28px;width: 80px"></el-input>
                  <div style="width: 20px;"></div>
                  <div>有</div>
                  <div style="width: 20px;"></div>
                  <el-input style="height:28px;width: 80px"></el-input>
                  <div style="width: 20px;"></div>
                  <div>米</div>
                   </div>
          <div></div>
        </div>
        
      </div>  
      
      
      
  </div>

</template>
<script lang="ts" setup>
import { ref } from 'vue'
const tags = ref([
  { name: '摄像头 1', type: 'info' },
  { name: '摄像头 2', type: 'info' },
  { name: '摄像头 3', type: 'info' },
  { name: '摄像头 4', type: 'info' },
  { name: '摄像头 5', type: 'info' },
   { name: '摄像头 6', type: 'info' },
])
const tagse = ref([
  { name: '摄像头 7', type: 'info' },
  { name: '摄像头 8', type: 'info' },
  { name: '摄像头 9', type: 'info' },

])
</script>
<style>
.wrap{

background-clip:content-box;/*居中的关键*/



}
</style>
