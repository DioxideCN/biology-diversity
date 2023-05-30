<template>
  <div>
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
          <!-- <BasicUpload
            :maxSize="20"
            :maxNumber="1"
            @change="handleChange"
            class="my-5"
            type="warning"
            text="导入"
            v-auth="['post:update']"
          />
          <a-button
            type="success"
            v-auth="['post:update']"
            preIcon="carbon:cloud-download"
            @click="handleExportData"
          >
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
              auth: ['post:update'],
              onClick: handleEdit.bind(null, record),
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
            <a-form-item label="点位名称" name="name">
              <a-input v-model:value="form.name" placeholder="请输入点位名称" />
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="投放点位时间" name="time">
              <a-date-picker show-time placeholder="请选择点位时间" v-model:value="form.time" />
            </a-form-item>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="点位经度" name="longitude">
              <a-input
                v-model:value="form.longitude"
                style="width: 100%"
                placeholder="请输入点位经度"
              />
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="点位纬度" name="latitude">
              <a-input
                v-model:value="form.latitude"
                style="width: 100%"
                placeholder="请输入点位纬度"
              />
            </a-form-item>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="所属区域名称" name="area">
              <a-input
                v-model:value="form.area"
                style="width: 75%"
                placeholder="请输入所属区域名称"
              />
              <a-button type="primary" style="margin-left: 5%" @click="open">选择</a-button>
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="所属区域编号" name="area_id">
              <a-input
                v-model:value="form.area_id"
                style="width: 100%"
                placeholder="请输入所属区域编号"
              />
            </a-form-item>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="点位负责人" name="manager">
              <a-input
                v-model:value="form.manager"
                style="width: 100%"
                placeholder="请输入点位负责人"
              />
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="点位负责人联系方式" name="manager_phone">
              <a-input
                v-model:value="form.manager_phone"
                style="width: 100%"
                placeholder="请输入点位负责人联系方式"
              />
            </a-form-item>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="24">
            <a-form-item label="点位简介" name="introduction">
              <a-textarea
                v-model:value="form.introduction"
                :rows="4"
                placeholder="请输入点位简介"
              />
            </a-form-item>
          </a-col>
          <a-col :span="24">
            <a-form-item label="点位详细地址" name="address">
              <a-textarea v-model:value="form.address" :rows="4" placeholder="请输入点位详细地址" />
            </a-form-item>
          </a-col>
          <a-col :span="24">
            <a-form-item label="备注" name="notes">
              <a-textarea v-model:value="form.notes" :rows="4" placeholder="请输入备注" />
            </a-form-item>
          </a-col>
        </a-row>
        <a-drawer
          v-model:visible="childrenDrawer"
          title="选择监测区域"
          width="500"
          :closable="false"
        >
          <a-table :data-source="table.arr" :columns="Columns">
            <template #bodyCell="{ column, record }">
              <template v-if="column.key === 'operation'">
                <a-button type="primary" @click="select(record)">选择</a-button>
              </template>
            </template>
          </a-table>
        </a-drawer>
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
  import moment from 'moment';
  import { Dayjs } from 'dayjs';
  import { Modal } from 'ant-design-vue';
  import { defineComponent, ref, reactive, onMounted, h } from 'vue';
  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { usePermission } from '/@/hooks/web/usePermission';
  import { useDrawer } from '/@/components/Drawer';
  import DemoDrawer from './Drawer.vue';
  import { Space } from 'ant-design-vue';
  import { BasicUpload } from '/@/components/Upload';
  import { deleteItem, getList, exportData, importData, createOrUpdate } from './api';
  import { columns, searchFormSchema } from './data';
  import { message } from 'ant-design-vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { downloadByData } from '/@/utils/file/download';
  import { getAreaList } from '../areaManage/api';
  export default defineComponent({
    name: 'Demo',
    components: { BasicTable, DemoDrawer, TableAction, BasicUpload, Space },
    setup() {
      const [registerDrawer, { openDrawer }] = useDrawer();
      const { createConfirm } = useMessage();
      const { hasPermission } = usePermission();
      const visible = ref<boolean>(false);
      const isUpdate = ref<boolean>(false);
      const childrenDrawer = ref<boolean>(false);
      const table = reactive({
        arr: [],
      });
      const form = reactive({
        name: '',
        time: '',
        longitude: '',
        latitude: '',
        area: '',
        area_id: '',
        address: '',
        manager: '',
        manager_phone: '',
        introduction: '',
        notes: '',
      });

      const Columns = reactive([
        {
          title: '区域编号',
          dataIndex: 'id',
          key: 'id',
        },
        {
          title: '区域名称',
          dataIndex: 'name',
          key: 'name',
        },
        {
          title: '区域地址',
          dataIndex: 'address',
          key: 'address',
        },
        {
          title: '区域负责人',
          dataIndex: 'manager',
          key: 'manager',
        },
        {
          title: '操作',
          key: 'operation',
          fixed: 'right',
          width: 100,
        },
      ]);
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

      function handleCreate() {
        visible.value = true;
        isUpdate.value = false;
        // console.log(visible.value);
      }
      function Close() {
        visible.value = false;
        form.name = '';
        form.time = '';
        form.longitude = '';
        form.latitude = '';
        form.area = '';
        form.area_id = '';
        form.manager = '';
        form.manager_phone = '';
        form.introduction = '';
        form.address = '';
        form.notes = '';
        // console.log(visible.value);
      }
      function onClose() {
        createOrUpdate(form, isUpdate.value).then((res) => {
          // console.log(res);
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
      function open() {
        childrenDrawer.value = true;
        getArea();
      }
      function handleEdit(record: Recordable) {
        visible.value = true;
        // console.log(visible.value);
        isUpdate.value = true;
        form.id = record.id;
        // console.log(form);
        getList({ id: record.id }).then((res) => {
          form.name = res.items[0].name;
          form.time = res.items[0].time;
          // console.log(form.time);
          form.longitude = res.items[0].longitude;
          form.latitude = res.items[0].latitude;
          form.area = res.items[0].area;
          form.area_id = res.items[0].area_id;
          form.manager = res.items[0].manager;
          form.manager_phone = res.items[0].manager_phone;
          form.introduction = res.items[0].introduction;
          form.address = res.items[0].address;
          form.notes = res.items[0].notes;
          // console.log(form);
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
      function select(record) {
        form.area_id = record.id;
        form.area = record.name;
        childrenDrawer.value = false;
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
      function getArea() {
        getAreaList().then((res) => {
          // console.log(res);
          table.arr = res.items;
          // console.log(table.arr);
        });
      }
      onMounted(() => {});
      return {
        Close,
        isUpdate,
        table,
        Columns,
        childrenDrawer,
        visible,
        form,
        rules,
        select,
        getArea,
        open,
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
