<template>
  <BasicDrawer v-bind="$attrs" @register="registerDrawer" showFooter :title="getTitle" width="50%" @ok="handleSubmit">
    <BasicForm @register="registerForm">
      <template #urls="{ model, field }">
        <!-- <BasicUpload
          width="80"
          :showBtn="false"
          :uploadApi="uploadApi"
          v-model:value="model[field]"
        /> -->
      <BasicUpload :maxSize="20" :maxNumber="2"  class="my-5" v-model:value="model[field]"/>
      <!-- <ImgUpload
        :action="uploadApi"
        v-model:value="model[field]"
      /> -->
      </template>
    </BasicForm>
  </BasicDrawer>
</template>
<script lang="ts">
import { defineComponent, ref, computed, unref } from 'vue';
import { BasicForm, useForm } from '/@/components/Form/index';
import { BasicDrawer, useDrawerInner } from '/@/components/Drawer';
import { createOrUpdate } from './api';
import { formSchema } from './data';
import { BasicUpload } from '/@/components/Upload';
import ImgUpload from '/@/components/Tinymce/src/ImgUpload.vue';
import { uploadApi } from '/@/api/sys/upload';
import { Upload } from 'ant-design-vue';

export default defineComponent({
  name: 'ButtonDrawer',
  components: { BasicDrawer, BasicForm, BasicUpload, ImgUpload, Upload},
  emits: ['success', 'register'],
  setup(_, { emit }) {
    const isUpdate = ref(true);

    const [registerForm, { resetFields, setFieldsValue, validate }] = useForm({
      labelWidth: 100,
      schemas: formSchema,
      showActionButtonGroup: false,
      baseColProps: { lg: 12, md: 24 },
    });

    const [registerDrawer, { setDrawerProps, closeDrawer }] = useDrawerInner(async (data) => {
      await resetFields();
      setDrawerProps({ confirmLoading: false });
      isUpdate.value = !!data?.isUpdate;

      if (unref(isUpdate)) {
        await setFieldsValue({
          ...data.record,
        });
      }
    });

    const getTitle = computed(() => (!unref(isUpdate) ? '新增项目' : '编辑项目'));

    async function handleSubmit() {
      try {
        const values = await validate();
        setDrawerProps({ confirmLoading: true });
        await createOrUpdate(values, unref(isUpdate));
        closeDrawer();
        emit('success');
      } finally {
        setDrawerProps({ confirmLoading: false });
      }
    }

    return {
      registerDrawer,
      registerForm,
      getTitle,
      handleSubmit,
      uploadApi
    };
  },
});
</script>
