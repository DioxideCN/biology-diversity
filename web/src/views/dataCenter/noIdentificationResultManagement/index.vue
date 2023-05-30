<template>
  <div>
    <BasicForm
      @register="register"
      :labelWidth="50"
      :actionColOptions="{ span: 24 }"
      @submit="handleSubmit"
      @reset="getData"
      class="componentBox"
    />
    <div class="button">
      <Space style="height: 40px">
        <a-button
          v-show="false"
          type="primary"
          v-auth="['post:add']"
          preIcon="ant-design:plus-outlined"
          @click="handleCreate"
          style="background-color: #339966"
        >
          新增
        </a-button>
        <a-button
          class="button"
          type="error"
          v-auth="['post:delete']"
          preIcon="ant-design:delete-outlined"
          @click="handleBulkDelete"
          style="margin-top: 0px; background-color: #f55c47"
        >
          删除
        </a-button>
      </Space>
      <DemoDrawer @register="registerDrawer" @success="handleSuccess" @fatherMethod="getData" />
    </div>
    <Modal
      v-model:visible="visible1"
      title="删除"
      @ok="handleOk1"
      class="MMbox"
      style="width: 900px"
    >
      <div class="MMInnerBox"> 确认删除？ </div>
    </Modal>
    <Modal
      v-model:visible="visible"
      title="查看信息"
      @ok="handleOk"
      class="Mbox"
      style="width: 900px"
    >
      <div class="Mlbox">
        <span class="lcontent" style="margin-left: 200px">
          识别时间：{{ card.time.slice(0, 10) + ' ' + card.time.slice(11, 19) }}
        </span>
        <span class="lcontent"> 设备名称：{{ card.equipment }} </span>
      </div>
      <img :src="urlFirst + card.url" class="Mvid" />
    </Modal>

    <div
      v-for="list in lists"
      class="bigBox"
      @click="showModal(list.create_datetime, list.url, list.equipment)"
    >
      <div class="deleteBox" v-show="deleteVisible" @click.stop="deleteData(list.recognition_id)">
        <img src="/resource/img/delete.png" alt="" />
      </div>
      <div class="mov box"><img :src="urlFirst + list.url" class="llbox vbox" /> </div>
      <div class="textBox">
        <span>{{
          list.create_datetime.slice(0, 10) + ' ' + list.create_datetime.slice(11, 19)
        }}</span
        ><br />
        <span>{{ list.ponit_name }}-{{ list.equipment_name }}</span>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
  import { defineComponent, onMounted, ref } from 'vue';
  import { Progress, Modal, Space } from 'ant-design-vue';
  import { getList, deleteD } from './api';
  import { ScrollContainer } from '/@/components/Container/index';
  import { useDrawer } from '/@/components/Drawer';
  import DemoDrawer from './Drawer.vue';
  import { BasicForm, useForm } from '/@/components/Form';
  import { searchFormSchema } from './data';
  import { BasicUpload } from '/@/components/Upload';
  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { useMessage } from '/@/hooks/web/useMessage';

  export default defineComponent({
    name: 'Demo',
    components: {
      Progress,
      Modal,
      ScrollContainer,
      DemoDrawer,
      BasicUpload,
      BasicTable,
      DemoDrawer,
      TableAction,
      BasicUpload,
      Space,
      BasicForm,
    },
    setup() {
      const card = ref({
        equipment: '',
        time: '',
        url: '',
      });
      const visible1 = ref(false);
      const deleteId = ref();
      const urlFirst = ref('/basic-api/');
      const deleteVisible = ref(false);
      const resourceLists = ref([]);
      const protect = ref('');
      const animalType = ref('');
      const photoTime = ref('');
      const fileType = ref('');
      const deviceType = ref('');
      const visible = ref(false);
      const opt = ref('');
      const [registerDrawer, { openDrawer }] = useDrawer();
      const { createMessage } = useMessage();
      var handleOk = (e: MouseEvent) => {
        // console.log(e);
        visible.value = false;
      };
      const [register, { setProps }] = useForm({
        labelWidth: 100,
        schemas: searchFormSchema,
        actionColOptions: {
          span: 15,
        },
      });
      var handleOk1 = (e: MouseEvent) => {
        visible1.value = false;
        deleteD(deleteId.value);
        getData();
      };
      function ReSet() {
        protect.value = '';
        animalType.value = '';
        photoTime.value = '';
        fileType.value = '';
        deviceType.value = '';
        lists.value = resourceLists.value;
      }
      function showModal(time, url, equipment) {
        card.value.equipment = equipment;
        card.value.time = time;
        card.value.url = url;
        visible.value = true;
      }
      const lists = ref([]);
      function getData() {
        getList(true).then((res) => {
          lists.value = res.items;

          resourceLists.value = lists.value;
          // console.log(lists);
        });
      }
      function handleCreate() {
        openDrawer(true, {
          isUpdate: false,
        });
      }
      function handleBulkDelete() {
        if (deleteVisible.value) {
          deleteVisible.value = false;
          // console.log(deleteVisible.value);
        } else {
          deleteVisible.value = true;
          // console.log(deleteVisible.value);
        }
      }
      async function handleDelete(id: number) {
        await deleteItem(id);
        message.success('删除成功');
        await reload();
      }
      function deleteData(id) {
        deleteId.value = id;
        visible1.value = true;
      }
      function search(protect, animalType, photoTime, fileType, deviceType) {
        const filterList = [];
        for (var i = 0; i < resourceLists.value.length; i++) {
          if (resourceLists.value[i].reserve == protect || protect == undefined || protect == '')
            if (
              resourceLists.value[i].name == animalType ||
              animalType == undefined ||
              animalType == ''
            )
              if (
                resourceLists.value[i].time == photoTime ||
                photoTime == undefined ||
                photoTime == ''
              )
                if (
                  resourceLists.value[i].fileType == fileType ||
                  fileType == undefined ||
                  fileType == ''
                )
                  if (
                    resourceLists.value[i].equipment == deviceType ||
                    deviceType == undefined ||
                    deviceTpye == ''
                  )
                    filterList.push(resourceLists.value[i]);
        }
        lists.value = filterList;
      }
      onMounted(() => {
        getData();
      });
      return {
        handleBulkDelete,
        handleOk,
        showModal,
        ReSet,
        handleCreate,
        handleDelete,
        registerDrawer,
        openDrawer,
        search,
        deleteData,
        register,
        handleSubmit: (values: any) => {
          // console.log(values);
          search(values.reserve, values.name, values.time, values.fileType, values.equipment);
          createMessage.success('查询成功');
        },
        getData,
        handleOk1,
        urlFirst,
        deleteVisible,
        resourceLists,
        visible,
        lists,
        deleteId,
        card,
        protect,
        animalType,
        photoTime,
        fileType,
        deviceType,
        opt,
        visible1,
      };
    },
  });
</script>
<style scoped>
  .box {
  }
  .bigBox {
    display: inline-block;
    float: left;
    height: auto;
    width: auto;
    margin-left: 20px;
    margin-top: 20px;
    border-radius: 10px;
    border: 2px solid #c0c0c0;
    box-shadow: #c0c0c0 0px 0px 10px 1px;
    padding: 20px;
    padding-top: 5px;
    width: 230px;
    position: relative;
  }
  .mov {
    margin-bottom: 5px;
  }
  .llbox {
    border-bottom: 1px solid #a9a9a9;
    margin-bottom: 10px;
  }

  .btn {
    float: right;
    margin: 7px 0px;
    border-radius: 9px;
    width: 50px;
    height: 25px;
  }
  .btn2 {
    background-color: green;
    border-color: green;
    color: white;
    margin-right: 20px;
  }

  .btn1 {
    background-color: #a9a9a9;
    border-color: #a9a9a9;
    color: white;
    margin-right: 50px;
  }
  .ltbox2 {
    display: inline-block;
    margin: 10px 0px;
    margin-left: 20px;
  }

  .ltbox1 {
    border-radius: 3px;
    border: 1px solid #a9a9a9;
  }

  .ltbox2 > span {
    color: #a9a9a9;
    font-weight: 600;
  }

  .tbox {
    background-color: #edeaea;
  }

  .Mbox {
    border-radius: 15px;
    padding: 20px;
  }
  .ant-modal-header {
    border-radius: 15px;
  }

  .Mvid {
    height: 300px;
    margin: 10px auto;
  }
  .Mlbox {
    margin: 10px auto;
  }

  .lcontent {
    display: inline-block;
    margin-left: 50px;
    font-weight: 600;
  }
  .vbox {
    margin-top: 10px;
    padding-bottom: 10px;
    border-radius: 3px;
    width: 200px;
    height: 120px;
  }
  .textBox {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .button {
    margin-top: 20px;
    margin-left: 10px;
  }

  .deleteBox {
    position: absolute;
    top: -10px;
    right: -10px;
    height: 30px;
    width: 30px;
  }
  .componentBox {
    background-color: white;
    margin-top: 10px;
    padding-top: 10px;
  }

  .MMbox {
    position: relative;
    top: 200px;
  }

  .MMInnerBox {
    height: 50px;
    font-size: 15px;
    padding: 10px 50px;
  }
</style>
