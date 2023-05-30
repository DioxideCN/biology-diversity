<template>
  <BasicModal v-bind="$attrs"
              @register="registerModal"
              :title="getTitle"
              @ok="handleSubmit">
    <BasicForm class="form" @register="registerForm">
    </BasicForm>
  </BasicModal>
</template>

<script lang="ts">
import { defineComponent,ref,computed,unref } from "vue";
import { BasicModal,useModalInner } from "/@/components/Modal";
import { BasicForm,useForm } from "/@/components/Form";
import { formSchema } from "./data";
import {createOrUpdate} from './api';
import { uploadApi } from "/@/api/sys/upload";
import { BasicUpload } from "/@/components/Upload";
import { PageWrapper } from "/@/components/Page";
import {Alert} from 'ant-design-vue';

export default defineComponent({
    name:'kingdom',
    components:{BasicModal,BasicForm,BasicUpload,PageWrapper,[Alert.name]:Alert},
    emits:['success','register'],
    setup(_,{emit}){
        const isUpdate = ref(true);
        const rowId = ref('');
        let fileNameValue:string;
        // let bucketNameValue:string;
        const [registerForm,{setFieldsValue,resetFields,validate}] = useForm({
            labelWidth:80,
            schemas:formSchema,
            showActionButtonGroup:false,
            actionColOptions:{
                span:10,
            }
        });
        const [registerModal,{setModalProps,closeModal}] = useModalInner(async (data)=>{
            resetFields();
            setModalProps({confirmLoading:false});
            isUpdate.value = !!data?.isUpdate;
            if(unref(isUpdate)){
                rowId.value = data.record.id;
                setFieldsValue({
                    ...data.record,
                });
            }
        })
        const getTitle = computed (() => (!unref(isUpdate) ? '添加动物分类类型信息' : '编辑动物分类类型信息'));
        async function handleSubmit(){
            try{
                const values = await validate();
                setModalProps({confirmLoading:true});
                values.docName = fileNameValue;
                if(!!unref(isUpdate)){
                    values.id = rowId.value;
                }
                await createOrUpdate(values,unref(isUpdate));
                closeModal();
                emit('success',{isUpdate:unref(isUpdate),values:{...values,id:rowId.value}});
            }finally{
                setModalProps({confirmLoading:false});
            }
        }
        return{
            registerModal,
            registerForm,
            getTitle,
            handleSubmit,
            uploadApi,
        }
    }

})
</script>

<style scoped>
.form{
    margin-left: 30px;
    margin-top: 20px;
}

</style>