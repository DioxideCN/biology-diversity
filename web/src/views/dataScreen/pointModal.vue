<template>
<transition name="modal-fade">
    <div class="b-modal-container" v-show="$props.visible">
        <i class="t_l_line"></i> 
        <i class="l_t_line"></i> 
     
      <!--右上边框-->

<i class="t_r_line"></i> 
<i class="r_t_line"></i> 
     
      <!--左下边框-->

<i class="l_b_line"></i> 
<i class="b_l_line"></i> 

          <!--右下边框-->

<i class="r_b_line"></i> 
<i class="b_r_line"></i> 
      <!-- 头部标题 -->
      <div class="b-modal-header">
        <div class="b-modal-header-title">
          <!--具名插槽内容优先级会高于 props-->
          <slot name="title">
            <span>{{ title }}</span>
          </slot>
        </div>
      </div>
      <!-- 内容区域 -->
      <div class="b-modal-content">
        <slot></slot>
      </div>
      <!-- 底部按钮 -->
      <div class="b-modal-footer">
        <div class="b-modal-btn">
          <slot name="footer">
            <button @click="close">取消</button>
            <button @click="ok">确认</button>
          </slot>
        </div>
      </div>
    </div>
  </transition>
  <!-- 遮罩层 -->
  <div class="mask" v-show="$props.visible" @click="close"></div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue'
    import type { PropType } from 'vue'
    export default defineComponent({
      name: 'pointModal',
      props: {
        // 模态框标题
        title: {
          type: String as PropType<string>,
          default: '标题'
        },
        visible: {
          type: Boolean as PropType<boolean>,
          default: false
        }
      },
      emits: ['cancel', 'update:visible', 'ok'],
      setup(props, { emit }) {
        // 取消
        const close = () => {
        emit('cancel');
        emit('update:visible', false);
        // console.log(props.visible);
        }
        // 确认
        const ok = () => {
        emit('ok')
        emit('update:visible', false)
        }
        return {
          close,
          ok
        }
      }
    })
</script>

<style scoped lang="less">
  @import "./modal.less";
</style>