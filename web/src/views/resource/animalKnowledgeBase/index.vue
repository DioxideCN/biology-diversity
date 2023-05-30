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
    <Modal
      :visible="visible"
      title="编辑动物知识库信息"
      @ok="handleOk1"
      @cancel="handleNo"
      class="MMbox"
      style="width: 900px"
    >
      <div class="editor" style="position: relative; left: 9%">
        <span style="position: relative; left: 0%">动物名称</span>
        <a-input v-model:value="name" placeholder="" />
      </div>
      <div class="editor">
        <span>形态特征</span>
        <Tinymce
          v-model="description"
          :showImageUpload="false"
          :height="200"
          :width="700"
          :toolbar="[
            'fontsizeselect lineheight searchreplace bold italic underline strikethrough alignleftaligncenter alignright outdent indent blockquote undo redo removeformat subscriptsuperscript code codesample',
          ]"
        />
      </div>
      <div class="editor">
        <span>栖息环境</span>
        <Tinymce
          v-model="habitat"
          :showImageUpload="false"
          :height="200"
          :width="700"
          :toolbar="[
            'fontsizeselect lineheight searchreplace bold italic underline strikethrough alignleft aligncenter alignright outdent indent  blockquote undo redo removeformat subscript superscript code codesample',
          ]"
        />
      </div>
      <div class="editor">
        <span>生活习性</span>
        <Tinymce
          v-model="live"
          :showImageUpload="false"
          :height="200"
          :width="700"
          :toolbar="[
            'fontsizeselect lineheight searchreplace bold italic underline strikethrough alignleft aligncenter alignright outdent indent  blockquote undo redo removeformat subscript superscript code codesample',
          ]"
        />
      </div>
      <div class="editor">
        <span>分布范围</span>
        <Tinymce
          v-model="distribution"
          :showImageUpload="false"
          :height="200"
          :width="700"
          :toolbar="[
            'fontsizeselect lineheight searchreplace bold italic underline strikethrough alignleft aligncenter alignright outdent indent  blockquote undo redo removeformat subscript superscript code codesample',
          ]"
        />
      </div>
      <div class="editor">
        <span>繁殖方式</span>
        <Tinymce
          v-model="reproduction"
          :showImageUpload="false"
          :height="200"
          :width="700"
          :toolbar="[
            'fontsizeselect lineheight searchreplace bold italic underline strikethrough alignleft aligncenter alignright outdent indent  blockquote undo redo removeformat subscript superscript code codesample',
          ]"
        />
      </div>
      <div class="editor">
        <span>亚种分布</span>
        <Tinymce
          v-model="subclass_distribution"
          :showImageUpload="false"
          :height="200"
          :width="700"
          :toolbar="[
            'fontsizeselect lineheight searchreplace bold italic underline strikethrough alignleft aligncenter alignright outdent indent  blockquote undo redo removeformat subscript superscript code codesample',
          ]"
        />
      </div>
      <div class="editor">
        <span>种群现状</span>
        <Tinymce
          v-model="family_distribution"
          :showImageUpload="false"
          :height="200"
          :width="700"
          :toolbar="[
            'fontsizeselect lineheight searchreplace bold italic underline strikethrough alignleft aligncenter alignright outdent indent  blockquote undo redo removeformat subscript superscript code codesample',
          ]"
        />
      </div>
      <div class="editor">
        <span>保护级别</span>
        <Tinymce
          v-model="production_level"
          :showImageUpload="false"
          :height="200"
          :width="700"
          :toolbar="[
            'fontsizeselect lineheight searchreplace bold italic underline strikethrough alignleft aligncenter alignright outdent indent  blockquote undo redo removeformat subscript superscript code codesample',
          ]"
        />
      </div>
      <div class="editor">
        <span>备注</span>
        <Tinymce
          v-model="notes"
          :showImageUpload="false"
          :height="200"
          :width="700"
          :toolbar="[
            'fontsizeselect lineheight searchreplace bold italic underline strikethrough alignleft aligncenter alignright outdent indent  blockquote undo redo removeformat subscript superscript code codesample',
          ]"
        />
      </div>
    </Modal>
    <DemoDrawer @register="registerDrawer" @success="handleSuccess" />
  </div>
</template>
<script lang="ts">
  import { defineComponent, ref, onMounted } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { usePermission } from '/@/hooks/web/usePermission';
  import { useDrawer } from '/@/components/Drawer';
  import DemoDrawer from './Drawer.vue';
  import { Space, Modal } from 'ant-design-vue';
  import { BasicUpload } from '/@/components/Upload';
  import { deleteItem, getList, exportData, importData, increaseData, createOrUpdate } from './api';
  import { columns, searchFormSchema } from './data';
  import { message } from 'ant-design-vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { downloadByData } from '/@/utils/file/download';
  import { Tinymce } from '/@/components/TinyMce';
  export default defineComponent({
    name: 'Animal',
    components: { BasicTable, DemoDrawer, TableAction, BasicUpload, Space, Modal, Tinymce },
    setup() {
      const id = ref('');
      const isUpdate = ref<boolean>(false);
      const visible = ref(false);
      const name = ref();
      const description = ref();
      const habitat = ref();
      const live = ref();
      const reproduction = ref();
      const distribution = ref();
      const subclass_distribution = ref();
      const family_distribution = ref();
      const production_level = ref();
      const notes: notes = ref();
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

      var handleOk1 = (e: MouseEvent) => {
        let postValue = {
          id: id.value,
          name: name.value,
          description: description.value,
          habitat: habitat.value,
          live: live.value,
          reproduction: reproduction.value,
          distribution: distribution.value,
          subclass_distribution: subclass_distribution.value,
          family_distribution: family_distribution.value,
          protection_level: production_level.value,
          notes: notes.value,
        };
        if (isUpdate.value != true) {
          increaseData(postValue)
            .then(() => {
              message.success('创建成功');
              reload();
            })
            .catch(() => {
              message.error('创建失败');
              reload();
            });
        } else {
          // postValue.id = id.value
          createOrUpdate(postValue, isUpdate.value)
            .then(() => {
              message.success('更改成功');
              reload();
            })
            .catch(() => {
              message.error('更改失败');
              reload();
            });
        }
        (id.value = ''),
          (name.value = ''),
          (description.value = ''),
          (habitat.value = ''),
          (live.value = ''),
          (reproduction.value = ''),
          (distribution.value = ''),
          (subclass_distribution.value = ''),
          (family_distribution.value = ''),
          (production_level.value = ''),
          (notes.value = ''),
          (isUpdate.value = false);
        visible.value = false;
      };

      function handleEdit(record: Recordable) {
        // console.log('Edit');
        isUpdate.value = true;
        (id.value = record.id),
          (name.value = record.name),
          (description.value = record.description),
          (habitat.value = record.habitat),
          (live.value = record.live),
          (reproduction.value = record.reproduction),
          (distribution.value = record.distribution),
          (subclass_distribution.value = record.subclass_distribution),
          (family_distribution.value = record.family_distribution),
          (production_level.value = record.production_level),
          (notes.value = record.notes),
          (visible.value = true);
      }

      function handleCreate() {
        visible.value = true;
      }

      // function handleEdit(record: Recordable) {
      //   openDrawer(true, {
      //     record,
      //     isUpdate: true,
      //   });
      // }

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

      function handleNo() {
        (id.value = ''),
          (name.value = ''),
          (description.value = ''),
          (habitat.value = ''),
          (live.value = ''),
          (reproduction.value = ''),
          (distribution.value = ''),
          (subclass_distribution.value = ''),
          (family_distribution.value = ''),
          (production_level.value = ''),
          (notes.value = ''),
          (visible.value = false);
      }
      return {
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
        handleOk1,
        handleNo,
        createOrUpdate,
        id,
        name,
        description,
        habitat,
        live,
        reproduction,
        distribution,
        subclass_distribution,
        family_distribution,
        production_level,
        notes,
        visible,
        isUpdate,
      };
    },
  });
</script>
<style scope>
  .editor {
    width: 90%;
    margin: 10px auto;
    font-weight: 500;
    font-size: 16px;
    color: #676a6c;
  }
  .editor > input {
    display: inline-block;
    width: 25%;
    margin-left: 2%;
  }
  .editor > span {
    position: relative;
    left: 10%;
    display: inline-block;
    margin-bottom: 1%;
  }
  .editor > div:nth-of-type(1) {
    width: 85%;
  }
</style>
