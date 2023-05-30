<template>
  <div>
    <CollapseContainer title="植物分类类型管理" :canExpan="false">
      <BasicTable @register="registerTable">
        <template #tableTitle>
          <Space style="height: 40px">
            <a-button
              type="primary"
              v-auth="['post:add']"
              preIcon="ant-design:plus-outlined"
              @click="handleCreate"
              style="background-color: #339966; border-color: #339966"
            >
              添加
            </a-button>
            <a-button
              type="error"
              v-auth="['post:delete']"
              preIcon="ant-design:delete-outlined"
              @click="handleBulkDelete"
              style="color: rgba(0, 0, 0, 0.85); border-color: #d9d9d9; background: #fff"
            >
              删除
            </a-button>
          </Space>
        </template>
        <template #action="{ record }">
          <TableAction
            :actions="[
              {
                type: 'button',
                icon: 'clarity:note-edit-line',
                color: 'primary',
                auth: ['post:update'],
                //点击跳出编辑抽屉，并绑定当前表格行的信息内容
                onClick: handleEdit.bind(null, record),
              },
              {
                icon: 'ant-design:delete-outlined',
                type: 'button',
                color: 'error',
                placement: 'left',
                auth: ['post:delete'],
                //弹出是否确认删除的提示信息，确认后删除当前行id的数据
                popConfirm: {
                  title: '是否确认删除',
                  confirm: handleDelete.bind(null, record.id),
                },
              },
            ]"
          />
        </template>
      </BasicTable>
    </CollapseContainer>
    <DemoModal @register="registerModal" @success="handleSuccess" />
  </div>
</template>
<script lang="ts">
  import { defineComponent } from 'vue';
  import DemoModal from './Modal.vue';
  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { usePermission } from '/@/hooks/web/usePermission';
  import { useModal } from '/@/components/Modal';
  import { Space, Modal, Input } from 'ant-design-vue';
  import { BasicUpload } from '/@/components/Upload';
  import { deleteItem, getList } from './api';
  import { columns, searchFormSchema } from './data';
  import { message } from 'ant-design-vue';
  import { CollapseContainer } from '/@/components/Container';
  import { useMessage } from '/@/hooks/web/useMessage';
  export default defineComponent({
    name: 'Animal',
    components: {
      DemoModal,
      CollapseContainer,
      Modal,
      BasicTable,
      TableAction,
      BasicUpload,
      Space,
      Input,
    },
    emits: ['success', 'register'],
    setup() {
      // const isUpdate = ref(true);
      // const editData = ref({
      //     name:'',
      //     notes:'',
      // });
      // const value = ref<string>('界');
      // const value2 = ref<string>('');
      // const value3 = ref<string>('');
      // const value4 = ref<string>('');
      // const value5 = ref<string>('');
      // const visible = ref<boolean>(false);
      // const visible2 = ref<boolean>(false);
      const { createConfirm } = useMessage();
      const { hasPermission } = usePermission();
      const [registerModal, { openModal }] = useModal();
      const [registerTable, { reload, getSelectRows }] = useTable({
        api: getList,
        columns,
        formConfig: {
          labelWidth: 80,
          schemas: searchFormSchema,
        },
        useSearchForm: true,
        showTableSetting: true,
        tableSetting: { fullScreen: true },
        bordered: true,
        showIndexColumn: false,
        rowSelection: {
          type: 'checkbox',
        },
        actionColumn: {
          width: 150,
          title: '操作',
          dataIndex: 'action',
          slots: { customRender: 'action' },
          fixed: undefined,
        },
      });

      // function handleCreate() {
      //   visible.value = true;
      // }
      function handleCreate() {
        openModal(true, {
          isUpdate: false,
        });
      }

      function handleEdit(record: Recordable) {
        openModal(true, {
          record,
          isUpdate: true,
        });
      }

      async function handleDelete(id: number) {
        await deleteItem(id);
        message.success('删除成功');
        await reload();
      }

      function handleBulkDelete() {
        if (getSelectRows().length == 0) {
          message.warning('请选择一个选项');
        } else {
          createConfirm({
            iconType: 'warning',
            title: '提示',
            content: '是否确认删除？',
            async onOk() {
              for (const item of getSelectRows()) {
                await deleteItem(item.id);
              }
              message.success('删除成功');
              await reload();
            },
          });
        }
      }

      function handleSuccess() {
        message.success('请求成功');
        reload();
      }

      return {
        //editData,
        // value,
        // value2,
        // value3,
        // value4,
        // value5,
        // visible,
        // visible2,
        registerTable,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        hasPermission,
        registerModal,
        handleBulkDelete,
        getSelectRows,
      };
    },
  });
</script>
<style scoped>
  .m-2 {
    margin: 20px auto;
    font-size: 16px;
    padding-left: 90px;
  }
  .m-3 {
    width: 200px;
  }
</style>
