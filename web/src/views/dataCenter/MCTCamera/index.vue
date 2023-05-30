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
          style="margin-top: 0px; background-color: #339966"
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
      style="width: 200px"
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
        <span class="lcontent" style="margin-left: 100px"> 物种名称：{{ card.name }} </span>
        <span class="lcontent"> 物种分类：{{ card.type }} </span>
        <span class="lcontent"> 相似度：{{ card.degree }}% </span>
        <span class="lcontent"> 拍摄时间：{{ card.time }} </span>
      </div>
      <video :src="urlFirst + card.url" class="Mvid" controls>
        <source :src="card.url" type="video/mp4" />
      </video>
    </Modal>

    <div
      v-for="list in lists"
      class="bigBox"
      @click="showModal(list.name, list.type, list.degree, list.time, list.url)"
    >
      <div class="deleteBox" v-show="deleteVisible" @click.stop="deleteData(list.id)">
        <img src="/resource/img/delete.png" alt="" />
      </div>
      <div class="mov box"
        ><video :src="urlFirst + list.url" class="llbox vbox" controls>
          <source :src="urlFirst + list.url" type="video/mp4" /> </video
      ></div>
      <div class="title box">
        <span>{{ list.name }}</span>
      </div>
      <div class="content box">
        <span>{{ list.EnglishName }}</span
        ><br />
        <span>{{ list.type }}</span>
      </div>
      <div class="message box">
        <span>{{ list.time }}</span
        ><br />
        <span>{{ list.place }}</span> <span>{{ list.equipment }}</span>
      </div>
      <div class="credit box" id="box1">
        <span>置信度</span> <span class="content1">{{ list.degree }}%</span>
        <Progress :percent="list.degree" strokeColor="green" :showInfo="false" />
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
        name: '',
        type: '',
        recognition_number: undefined,
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
      function showModal(name, type, degree, time, url) {
        card.value.name = name;
        card.value.type = type;
        card.value.degree = degree;
        card.value.time = time;
        card.value.url = url;
        visible.value = true;
      }
      const lists = ref([]);
      function getData() {
        getList(true).then((res) => {
          lists.value = res.items;
          resourceLists.value = lists.value;
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
  .bigBox {
    display: inline-block;
    float: left;
    height: auto;
    width: auto;
    margin-left: 20px;
    margin-top: 20px;
    border-radius: 10px;
    border: 2px solid #c0c0c0;
    background-color: #fff;
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
  #box1 {
    color: #a9a9a9;
    margin-top: 10px;
  }
  .title {
    font-size: 16px;
    font-weight: 600;
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
  .content1 {
    float: right;
    color: green;
  }
  .textBox {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
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
    padding: 10px 20px;
  }
</style>
