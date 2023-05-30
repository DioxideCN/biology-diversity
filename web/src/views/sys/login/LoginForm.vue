<template>
  <LoginFormTitle v-show="getShow" class="enter-x" />
  <Form
    class="p-4 enter-x form"
    :model="formData"
    :rules="getFormRules"
    ref="formRef"
    v-show="getShow"
    @keypress.enter="handleLogin"
  >
    <FormItem name="account" class="user">
      <div class="usertext" style="">用户名</div>
      <Input
        size="large"
        v-model:value="formData.account"
        :placeholder="t('sys.login.userName')"
        class="inputBox"
        :bordered= 'haveBordered'
      />
    </FormItem>
    <FormItem name="password" class="enter-x user">
      <div class="usertext" style="">密码</div>
      <InputPassword
        size="large"
        visibilityToggle
        v-model:value="formData.password"
        :placeholder="t('sys.login.password')"
        class="inputBox2"
        :bordered= 'haveBordered'
      />
    </FormItem>

    <FormItem class="enter-x user" name="captcha">
      <div class="usertext" style="">验证码</div>
      <Input
        size="large"
        v-model:value="formData.captcha"
        placeholder="请输入验证码"
        class="box1 box2 inputBox3"
        :bordered="haveBordered"
      />
      <img :src="formData.image_url" alt="" class="imageBox" @dblclick="refreshCaptch" />
    </FormItem>
    <FormItem class="enter-x">
      <Button class="buttomBox" type="primary" size="large" block @click="handleLogin" :loading="loading">
        {{ t('sys.login.loginButton') }}
      </Button>
      <!-- <Button size="large" class="mt-4 enter-x" block @click="handleRegister">
        {{ t('sys.login.registerButton') }}
      </Button> -->
    </FormItem>
    <!--    <ARow class="enter-x">-->
    <!--      <ACol :md="8" :xs="24">-->
    <!--        <Button block @click="setLoginState(LoginStateEnum.MOBILE)">-->
    <!--          {{ t('sys.login.mobileSignInFormTitle') }}-->
    <!--        </Button>-->
    <!--      </ACol>-->
    <!--      <ACol :md="8" :xs="24" class="!my-2 !md:my-0 xs:mx-0 md:mx-2">-->
    <!--        <Button block @click="setLoginState(LoginStateEnum.QR_CODE)">-->
    <!--          {{ t('sys.login.qrSignInFormTitle') }}-->
    <!--        </Button>-->
    <!--      </ACol>-->
    <!--      <ACol :md="7" :xs="24">-->
    <!--        <Button block @click="setLoginState(LoginStateEnum.REGISTER)">-->
    <!--          {{ t('sys.login.registerButton') }}-->
    <!--        </Button>-->
    <!--      </ACol>-->
    <!--    </ARow>-->

    <!--    <Divider class="enter-x">{{ t('sys.login.otherSignIn') }}</Divider>-->

    <!--    <div class="flex justify-evenly enter-x" :class="`${prefixCls}-sign-in-way`">-->
    <!--      <GithubFilled />-->
    <!--      <WechatFilled />-->
    <!--      <AlipayCircleFilled />-->
    <!--      <GoogleCircleFilled />-->
    <!--      <TwitterCircleFilled />-->
    <!--    </div>-->
  </Form>
</template>
<script lang="ts" setup>
  import { reactive, ref, unref, computed, onMounted } from 'vue';

  import { Checkbox, Form, Input, Row, Col, Button, Divider, message, Space } from 'ant-design-vue';
  import {
    GithubFilled,
    WechatFilled,
    AlipayCircleFilled,
    GoogleCircleFilled,
    TwitterCircleFilled,
  } from '@ant-design/icons-vue';
  import LoginFormTitle from './LoginFormTitle.vue';

  import { useI18n } from '/@/hooks/web/useI18n';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { useGlobSetting } from '/@/hooks/setting';
  import { useUserStore } from '/@/store/modules/user';
  import { LoginStateEnum, useLoginState, useFormRules, useFormValid } from './useLogin';
  import { useDesign } from '/@/hooks/web/useDesign';
  import axios from 'axios';
  import { fallbackWithSimple } from '@intlify/core-base';
  //import { onKeyStroke } from '@vueuse/core';

  const ACol = Col;
  const ARow = Row;
  const FormItem = Form.Item;
  const InputPassword = Input.Password;
  const { t } = useI18n();
  const { notification, createErrorModal } = useMessage();
  const { prefixCls } = useDesign('login');
  const userStore = useUserStore();
  const globSetting = useGlobSetting();

  const { setLoginState, getLoginState } = useLoginState();
  const { getFormRules } = useFormRules();

  const formRef = ref();
  const loading = ref(false);
  const rememberMe = ref(false);
  const haveBordered = ref(false);

  const formData = reactive({
    account: '',
    password: '',
    image_url: '',
    captch_id: '',
  });

  function refreshCaptch() {
    axios
      //params:可传递多个参数,固定写法,不能改,否则参数传递失败
      .get(globSetting.apiUrl + globSetting.urlPrefix + '/api/system/getCode')
      .then((res) => {
        // console.log(globSetting.apiUrl +globSetting.urlPrefix+ "/api/system/getCode")
        formData.image_url = res.data.image_url;
        formData.captch_id = res.data.captch_id;
      })
      .catch((err) => {
       // console.log(err);
      });
  }

  function handleCaptch() {
    axios
      //params:可传递多个参数,固定写法,不能改,否则参数传递失败
      .get(globSetting.apiUrl + globSetting.urlPrefix + '/api/system/getCode')
      .then((res) => {
        //console.log("handler code",res)
        // console.log(globSetting.apiUrl +globSetting.urlPrefix+ "/api/system/getCode")
        formData.image_url = res.data.image_url;
        formData.captch_id = res.data.captch_id;
      })
      .catch((err) => {
       // console.log(err);
      });
  }
  onMounted(() => {
    handleCaptch();
  });

  const { validForm } = useFormValid(formRef);

  //onKeyStroke('Enter', handleLogin);

  const getShow = computed(() => unref(getLoginState) === LoginStateEnum.LOGIN);
  const captchaSuccess = reactive({ value: false });

  async function handleLogin() {
    const data = await validForm();
    if (!data) return;
    if (data.captcha === '') {
      message.error('验证码不能为空！');
      return;
    }
    try {
      // console.log(formData.captch_id);
      const userInfo = userStore.login({
        password: data.password,
        username: data.account,
        captcha: data.captcha,
        captch_id: formData.captch_id,
        mode: undefined, //不要默认的错误提示
      });
      userInfo.then(() => {
        // notification.success({
        //   message: t('sys.login.loginSuccessTitle'),
        //   description: `${t('sys.login.loginSuccessDesc')}: ${userInfo.name}`,
        //   duration: 3,
        // });
        // loading.value = false;
      });
    } catch (error) {
      createErrorModal({
        title: t('sys.api.errorTip'),
        content: (error as unknown as Error).message || t('sys.api.networkExceptionMsg'),
        getContainer: () => document.body.querySelector(`.${prefixCls}`) || document.body,
      });
    } finally {
      handleCaptch();
      loading.value = false;
    }

    // axios
    //   .post(globSetting.apiUrl + globSetting.urlPrefix + '/api/system/postCode', captchaForm)
    //   .then(function (res) {
    //
    //     //
    //     // if (res.data.code == -1) {
    //     //   handleCaptch();
    //     //   message.error('验证码错误！');
    //     //   loading.value = false;
    //     // } else {
    //     //
    //     // }
    //   });
  }
</script>
<style scoped lang="less">
  :deep(.ant-form-item-with-help .ant-form-item-explain) {
    margin-top: -44px;
  }
  .box1 {
    display: inline-block;
  }

  input {
    padding-right: 10%;
  }
  .inputBox {
    height: 2.5625rem;
    width: 210px;
    bottom: 45px;
    left: 70px;
    border: none;
    outline: none;
  }
  .inputBox2 {
    height: 2.5625rem;
    width: 250px;
    bottom: 45px;
    left: 70px;
    border: none;
    outline: none;
  }
  .inputBox3 {
    height: 2.5625rem;
    width: 140px;
    bottom: 45px;
    left: 70px;
    border: none;
    outline: none;
  }
  .imageBox{
    height: 30px;
    left: 270px;
    right: 260px;
    margin-left: 60%;
    margin-top: -25%;
  }
  .user{
    top: 2%;
    left: 25px;
    bottom: 25px;
    margin-left: 10%;
    margin-right: 40px;
    margin-bottom: 1px;
    height: 50px;
    display: flex;
  }
  .usertext{
	  border-bottom: 1px solid #2D456B;
    width: 320px;
	  height: 30px;
	  line-height: 10px;
    font-size: 15px;
    padding-top: 1px;
  }
  .buttomBox {
    background-color: #2D456B;
    border-color: #2D456B;
    margin-top: 20px;
    margin: auto;
    width: 18rem;
    text-align: center;
    left: 14%;
  }

  button:hover {
    background-color: #2D456B;
    border-color: #2D456B;
  }
</style>
