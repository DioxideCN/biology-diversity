<template>
  <ConfigProvider :locale="getAntdLocale">
    <AppProvider>
      <RouterView v-if="isRouterAlive" />
    </AppProvider>
  </ConfigProvider>
</template>

<script lang="ts" setup>
import { onMounted, ref, nextTick, provide } from 'vue';
import { ConfigProvider } from 'ant-design-vue';
import { AppProvider } from '/@/components/Application';
import { useTitle } from '/@/hooks/web/useTitle';
import { useLocale } from '/@/locales/useLocale';

import 'dayjs/locale/zh-cn';
onMounted(() => {
  if (isMobile()) {
    alert('请在PC端打开');
  } 
});
// support Multi-language
const { getAntdLocale } = useLocale();
const isRouterAlive = ref(true);
const reload = () => {
  isRouterAlive.value = false;
  nextTick(() => {
    isRouterAlive.value = true;
  });
};
provide('reload', reload);

// Listening to page changes and dynamically changing site titles
useTitle();

function isMobile() {
  let flag = navigator.userAgent.match(
    /(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i,
  );
  return flag;
}

</script>
<style>
.bigemap-logo {
  display: none;
}
</style>
