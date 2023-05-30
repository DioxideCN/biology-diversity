<template>
  <div>
    <Modal :visible="visible" @ok="handleOk" @cancel="handleOk" style="width: 1000px">
      <div style="width: 100%; height: 50px"></div>
      <iframe
        id="video"
        :src="url"
        width="800px"
        height="450px"
        style="margin: 10px auto; margin-bottom: 10px; padding-bottom: 15px"
        allow="autoplay"
      ></iframe>
    </Modal>
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
            新增
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
              onClick: handleEdit.bind(null, record),
            },
            {
              type: 'button',
              icon: 'ant-design:video-camera-outlined',
              color: 'primary',
              auth: ['post:update'],
              onClick: handleEdit1.bind(null, record),
            },
            {
              icon: 'ant-design:delete-outlined',
              type: 'button',
              color: 'error',
              placement: 'left',
              auth: ['post:delete'],
              popConfirm: {
                title: '是否确认删除',
                confirm: handleDelete.bind(null, record.id),
              },
            },
            {
              icon: 'ant-design:minus-circle-outlined',
              type: 'button',
              color: 'error',
              placement: 'left',
              auth: ['post:unable'],
              popConfirm: {
                title: '是否停用',
                confirm: handleAble.bind(null, record.id),
              },
            },
          ]"
        />
      </template>
    </BasicTable>
    <DemoDrawer @register="registerDrawer" @success="handleSuccess" />
  </div>
</template>
<script lang="ts">
  import { defineComponent, ref, onMounted } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { usePermission } from '/@/hooks/web/usePermission';
  import { useDrawer } from '/@/components/Drawer';
  import DemoDrawer from './Drawer.vue';
  import { Space } from 'ant-design-vue';
  import { BasicUpload } from '/@/components/Upload';
  import { deleteItem, getList, exportData, importData, Able, getList1 } from './api';
  import { columns, searchFormSchema } from './data';
  import { message } from 'ant-design-vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { downloadByData } from '/@/utils/file/download';
  import { Modal } from 'ant-design-vue';
  export default defineComponent({
    name: 'Demo',
    components: { BasicTable, DemoDrawer, TableAction, BasicUpload, Space, Modal },
    setup() {
      const [registerDrawer, { openDrawer }] = useDrawer();
      const { createConfirm } = useMessage();
      const { hasPermission } = usePermission();
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

      var visible = ref(false);

      function handleCreate() {
        openDrawer(true, {
          isUpdate: false,
        });
      }

      function handleEdit(record: Recordable) {
        openDrawer(true, {
          record,
          isUpdate: true,
        });
      }

      function handleEdit1(record: Recordable) {
        visible.value = true;
        getList1().then((res) => {
          // console.log(res);
          for (var i = 0; i < res.total; i++) {
            if ((res.items[i].model = record.model)) url.value = res.items[i].living_url;
          }
        });
      }

      function handleAble(record: Recordable) {
        record.status = !record.status;
        Able(record);
        reload();
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

      var url = ref('');

      onMounted(() => {
        getList1({}).then((res) => {
          // console.log(res);
        });
        getList({}).then((res) => {
          // console.log(res);
        });
      });

      async function handleChange(list: string[]) {
        // console.log(list[0]);
        await importData({ path: list[0] });
        message.success(`导入成功`);
        await reload();
      }

      async function handleExportData() {
        const response = await exportData();
        await downloadByData(response.data, '项目数据.xlsx');
      }

      function handleSuccess() {
        message.success('请求成功');
        reload();
      }

      function handleOk() {
        visible.value = false;
      }
      return {
        handleAble,
        registerTable,
        registerDrawer,
        handleCreate,
        handleEdit,
        handleEdit1,
        handleDelete,
        handleSuccess,
        hasPermission,
        handleBulkDelete,
        getSelectRows,
        handleExportData,
        handleChange,
        handleOk,
        visible,
        url,
      };
    },
  });
</script>
