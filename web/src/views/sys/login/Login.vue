<template>
  <div :class="prefixCls" class="relative w-full h-full px-4">
    <AppLocalePicker
      class="absolute text-white top-4 right-4 enter-x xl:text-gray-600"
      :showText="false"
      v-if="!sessionTimeout && showLocale"
    />
    <AppDarkModeToggle class="absolute top-3 right-7 enter-x" v-if="!sessionTimeout" />

    <span class="-enter-x xl:hidden"> </span>
    <div
      class="flex w-full h-full py-5 xl:h-auto xl:py-0 xl:my-0 xl:w-6/12 box"
    >
      <div
        :class="`${prefixCls}-form`"
        class="relative w-full px-5 py-8 mx-auto my-auto rounded-md shadow-md xl:ml-16 xl:bg-transparent sm:px-8 xl:p-4 xl:shadow-none sm:w-3/4 lg:w-2/4 xl:w-auto enter-x BigBox"
      >
        <LoginForm style="position: absolute" />
        <ForgetPasswordForm />
        <RegisterForm />
        <MobileForm />
        <QrCodeForm />
      </div>
    </div>
  </div>
</template>
<script lang="ts" setup>
  import { computed } from 'vue';
  import { AppLogo } from '/@/components/Application';
  import { AppLocalePicker, AppDarkModeToggle } from '/@/components/Application';
  import LoginForm from './LoginForm.vue';
  import ForgetPasswordForm from './ForgetPasswordForm.vue';
  import RegisterForm from './RegisterForm.vue';
  import MobileForm from './MobileForm.vue';
  import QrCodeForm from './QrCodeForm.vue';
  import { useGlobSetting } from '/@/hooks/setting';
  import { useI18n } from '/@/hooks/web/useI18n';
  import { useDesign } from '/@/hooks/web/useDesign';
  import { useLocaleStore } from '/@/store/modules/locale';

  defineProps({
    sessionTimeout: {
      type: Boolean,
    },
  });

  const globSetting = useGlobSetting();
  const { prefixCls } = useDesign('login');
  const { t } = useI18n();
  const localeStore = useLocaleStore();
  const showLocale = localeStore.getShowPicker;
  const title = computed(() => globSetting?.title ?? '');
</script>
<style scoped lang="less">
  @prefix-cls: ~'@{namespace}-login';
  @logo-prefix-cls: ~'@{namespace}-app-logo';
  @countdown-prefix-cls: ~'@{namespace}-countdown-input';
  @dark-bg: #293146;

  html[data-theme='dark'] {
    .@{prefix-cls} {
      background-color: @dark-bg;

      &::before {
        background-image: url(/@/assets/svg/login-bg-dark.svg);
      }

      .ant-input,
      .ant-input-password {
        background-color: #232a3b;
      }

      .ant-btn:not(.ant-btn-link):not(.ant-btn-primary) {
        border: 1px solid #4a5569;
      }

      &-form {
        background: transparent !important;
      }

      .app-iconify {
        color: #fff;
      }
    }

    input.fix-auto-fill,
    .fix-auto-fill input {
      -webkit-text-fill-color: #c9d1d9 !important;
      box-shadow: inherit !important;
    }
  }

  .@{prefix-cls} {
    min-height: 100%;
    background-image: url(/@/assets/images/Background.png);
    background-size: cover;
    position: relative;
  }
  .box {
    position: relative;
    border-radius: 3%;
    background-color: white;
    width: 415px;
	  height: 337px;
    box-shadow: 0px 0px 50px rgba(0, 0, 0, 0.4);
    margin: auto;
    top: 25%;
    padding-bottom: 0;
  }
  .BigBox {
    height: 100%;
    width: 100%;
    margin: 0;
    right: 0;
    top: 0;
    padding: 0;
  }
  .title {
    font-size: 27px;
    font-weight: 800;
    font-style: normal;
    font-family: 'Microsoft Sans Serif', Arial;
    color: rgba(1, 107, 9, 1);
    display: inline-block;
    vertical-align: middle;
  }
  .tBox {
    margin-top: 10px;
    position: absolute;
    top: -20%;
    left: 29px;
    width: 400%;
  }

  .icon {
    width: 5%;
    height: 5%;
    display: inline-block;
    vertical-align: middle;
  }
</style>
