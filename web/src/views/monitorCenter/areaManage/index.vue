<template>
  <div>
    <BasicTable @register="registerTable">
      <template #tableTitle>
        <Space style="height: 40px">
          <a-button
            type="primary"
            preIcon="ant-design:plus-outlined"
            @click="handleCreate"
            style="background-color: #339966; border-color: #339966"
          >
            新增
          </a-button>
          <a-button
            type="error"
            preIcon="ant-design:delete-outlined"
            @click="handleBulkDelete"
            style="color: rgba(0, 0, 0, 0.85); border-color: #d9d9d9; background: #fff"
          >
            删除
          </a-button>
          <!-- <BasicUpload
            :maxSize="20"
            :maxNumber="1"
            @change="handleChange"
            class="my-5"
            type="warning"
            text="导入"
          />
          <a-button type="success" preIcon="carbon:cloud-download" @click="handleExportData">
            导出
          </a-button> -->
        </Space>
      </template>
      <template #action="{ record }">
        <TableAction
          :actions="[
            {
              type: 'button',
              icon: 'clarity:note-edit-line',
              color: 'primary',
              onClick: handleEdit.bind(null, record),
            },
            {
              icon: 'ant-design:delete-outlined',
              type: 'button',
              color: 'error',
              placement: 'left',
              popConfirm: {
                title: '是否确认删除',
                confirm: handleDelete.bind(null, record.id),
              },
            },
          ]"
        />
      </template>
    </BasicTable>
    <a-drawer
      title="新增项目"
      :width="720"
      :visible="visible"
      :body-style="{ paddingBottom: '80px' }"
      @close="Close"
    >
      <a-form :model="form" :rules="rules" layout="vertical">
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="区域名称" name="name">
              <a-input v-model:value="form.name" placeholder="请输入区域名称" />
            </a-form-item>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="投放省份" name="province">
              <v-distpicker class="place" @selected="onSelected" />
            </a-form-item>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="区域负责人" name="manager">
              <a-input
                v-model:value="form.manager"
                style="width: 100%"
                placeholder="请输入区域负责人"
              />
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="区域负责人联系方式" name="manager_phone">
              <a-input
                v-model:value="form.manager_phone"
                style="width: 100%"
                placeholder="请输入区域负责人联系方式"
              />
            </a-form-item>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="24">
            <a-form-item label="区域简介" name="introduction">
              <a-textarea
                v-model:value="form.introduction"
                :rows="4"
                placeholder="请输入区域简介"
              />
            </a-form-item>
          </a-col>
          <a-col :span="24">
            <a-form-item label="备注" name="notes">
              <a-textarea v-model:value="form.notes" :rows="4" placeholder="请输入区域简介" />
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
      <div
        :style="{
          position: 'absolute',
          right: 0,
          bottom: 0,
          width: '100%',
          borderTop: '1px solid #e9e9e9',
          padding: '10px 16px',
          background: '#fff',
          textAlign: 'right',
          zIndex: 1,
        }"
      >
        <a-button style="margin-right: 8px" @click="Close">取消</a-button>
        <a-button type="primary" @click="onClose">提交</a-button>
      </div>
    </a-drawer>
  </div>
</template>
<script lang="ts">
  import { Modal } from 'ant-design-vue';
  import { defineComponent, ref, reactive } from 'vue';
  import VDistpicker from 'v-distpicker';
  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { usePermission } from '/@/hooks/web/usePermission';
  import { useDrawer } from '/@/components/Drawer';
  import DemoDrawer from './Drawer.vue';
  import { Space } from 'ant-design-vue';
  import { BasicUpload } from '/@/components/Upload';
  import { deleteItem, getAreaList, exportData, importData, createOrUpdate } from './api';
  import { columns, searchFormSchema } from './data';
  import { message } from 'ant-design-vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { downloadByData } from '/@/utils/file/download';
  export default defineComponent({
    name: 'Demo',
    components: { BasicTable, DemoDrawer, TableAction, BasicUpload, Space, VDistpicker },
    setup() {
      const [registerDrawer, { openDrawer }] = useDrawer();
      const { createConfirm } = useMessage();
      const { hasPermission } = usePermission();
      const visible = ref<boolean>(false);
      const isUpdate = ref<boolean>(false);
      const form = reactive({
        name: '',
        address: '11',
        manager: '',
        manager_phone: '',
        introduction: '',
        notes: '',
      });
      const rules = {
        name: [{ required: true, message: '请输入区域名称' }],
        province: [{ required: true, message: '请输入投放省份' }],
        city: [{ required: true, message: '请输入投放城市' }],
        county: [{ required: true, message: '请输入投放区县' }],
        owner: [{ required: true, message: '请输入区域负责人' }],
        dateTime: [{ required: true, message: '请输入区域负责人联系方式', type: 'object' }],
        description: [{ required: true, message: 'Please enter url description' }],
      };
      const [registerTable, { reload, getSelectRows }] = useTable({
        api: getAreaList,
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

      function handleCreate() {
        visible.value = true;
        isUpdate.value = false;
      }
      function Close() {
        visible.value = false;
        // console.log(visible.value);
      }
      function onClose() {
        createOrUpdate(form, isUpdate.value).then((res) => {
          if (res.code == 2000) {
            Modal.success({
              title: '成功',
              content: h('div', {}, [h('p', res.message)]),
            });
          } else {
            Modal.success({
              title: '成功',
              content: res.message,
            });
          }
        });
        visible.value = false;
        reload();
      }
      function onSelected(data) {
        const { province, city, area } = data;
        if (!province.code && !city.code && !area.code) return;
        // console.log(form.address, province.value, city.value, area.value);
        form.address = province.value + city.value + area.value;
      }
      function handleEdit(record: Recordable) {
        visible.value = true;
        isUpdate.value = true;
        getAreaList({ id: record.id }).then((res) => {
          // console.log(res);
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

      return {
        Close,
        form,
        rules,
        visible,
        onSelected,
        onClose,
        registerTable,
        registerDrawer,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        hasPermission,
        handleBulkDelete,
        getSelectRows,
        handleExportData,
        handleChange,
      };
    },
  });
</script>
<style scoped>
  :global(.distpicker-address-wrapper select) {
    height: 40px;
    font-size: 1rem;
    line-height: 1.25;
    color: #464a4c;
    background-color: #fff;
    background-image: none;
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, 0.15);
    border-radius: 0.25rem;
    /* -webkit-transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
    transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
    -o-transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
    transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s; */
    transition: border-color ease-in-out 0.15s, box-shadow ease-in-out 0.15s,
      -webkit-box-shadow ease-in-out 0.15s;
    margin: 5px 5px;
  }
</style>
