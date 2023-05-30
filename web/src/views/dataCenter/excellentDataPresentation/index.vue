<template>
  <div>
    <BasicForm
      @register="register"
      :labelWidth="50"
      :actionColOptions="{ span: 24 }"
      @submit="handleSubmit"
      @reset="getData"
      class="componentBox"
      @updateSchema="updateSchema"
    />
    <div class="button">
      <Space style="height: 40px">
        <a-button
          v-show="false"
          type="primary"
          v-auth="['post:add']"
          preIcon="ant-design:plus-outlined"
          @click="handleCreate"
        >
          新增
        </a-button>
        <a-button
          class="button"
          type="error"
          v-auth="['post:delete']"
          preIcon="ant-design:delete-outlined"
          @click="handleBulkDelete"
          style="
            margin-top: 0px;
            color: rgba(0, 0, 0, 0.85);
            border-color: #d9d9d9;
            background: #fff;
          "
        >
          删除
        </a-button>
      </Space>
      <DemoDrawer @register="registerDrawer" @success="handleSuccess" @fatherMethod="getData()" />
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
      style="width: 1000px"
    >
    <div class="Mlbox">
        <span class="lcontent" style="margin-left: 10px"> 物种名称：{{ card.cn }} </span>
        <span class="lcontent"> 物种分类：{{ card.type }} </span>
        <span class="lcontent"> 置信度：{{ card.degree }}% </span>
        <span class="lcontent">
          拍摄时间：{{ card.create_datetime.slice(0, 10) + ' ' + card.create_datetime.slice(11, 19) }}
        </span>
        <span class="lcontent"> 标错信息：</span>
        <div style="display: inline-block; float: right; margin-top: -7px">
          <a-switch
            v-model:checked="card.isFalse"
            style="right: 70px"
            @click="open(card.list)"
          />
          <a-select
            v-model:value="card.erro_msg"
            show-search
            ref="select"
            style="width: 100px; margin-right: 20px; right: 50px"
            :options="option"
            :onSearch="handleChange(card.list, card.erro_msg)"
            :disabled="!card.isFalse"
            :defaultValue="card.erro_msg"
          />
        </div>
      </div>
      <video :src="card.url" class="Mvid" style="width: 120%; margin-top: 30px" controls></video>
    </Modal>

    <div class="jqbox">
      <div
        v-for="list of lists2"
        class="bigBox"
        @click="showModal(
            list.cn,
            list.type,
            list.degree,
            list.create_datetime,
            list.url,
            list.isFalse,
            list.erro_msg,
            list,
          )"
        :key="tableKey"
        @fatherMethod="getData()"
      >
        <div class="deleteBox" v-show="deleteVisible" @click.stop="deleteData(list.recognition_id)">
          <img src="/resource/img/delete.png" alt="" />
        </div>
        <div class="mov box"
          ><video :src="list.url" class="lbox vbox" style="width: 100%" ></video>
        </div>
        <div class="title box">
          <span>{{ list.cn }}</span>
          <img
            :src="showLike(list.isExcellent)"
            alt=""
            class="like"
            @click.stop="changeLike(list)"
          />
        </div>
        <div class="content box">
          <span>{{ list.en }}</span
          ><br />
          <span>{{ list.type }}</span>
        </div>
        <div class="message box ebox">
          <span>{{
            list.create_datetime.slice(0, 10) + ' ' + list.create_datetime.slice(11, 19)
          }}</span
          ><br />
          <span>{{ list.ponit_name }}</span> <span>{{ list.equipment_name }}</span>
        </div>
        <div class="credit box" id="box1">
          <span>置信度</span> <span class="content1">{{ list.degree }}%</span>
          <Progress :percent="list.degree" strokeColor="green" :showInfo="false" />
        </div>
      </div>
    </div>
        <Pagination
        size="small"
        style="float:right"
        :total="paginationData.total"
        showQuickJumper
        :onChange="handlePageNoChange"
        :showTotal="showtotal"
        :pageSize = "paginationData.defaultPageSize"
        :showSizeChanger="false"
        ></Pagination>
  </div>
</template>
<script lang="ts">
  import { defineComponent, onMounted, ref, reactive } from 'vue';
  import { Progress, Modal, Space, Pagination } from 'ant-design-vue';
  import { getList, updateLike, deleteD, getList3, getList4, getList5 } from './api';
  import { useDrawer } from '/@/components/Drawer';
  import DemoDrawer from './Drawer.vue';
  import { BasicForm, useForm } from '/@/components/Form';
  import { searchFormSchema, PaginationConfig } from './data';
  import { BasicUpload } from '/@/components/Upload';
  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { useModal } from '/@/components/Modal';
  import { usePagination } from './hooks/usePagination';

  export default defineComponent({
    name: 'Demo',
    components: {
      Progress,
      Modal,
      DemoDrawer,
      BasicUpload,
      BasicTable,
      DemoDrawer,
      TableAction,
      BasicUpload,
      Space,
      BasicForm,
      Pagination,
    },
    setup() {
      const { createMessage } = useMessage();
      const like = ref('/resource/img/like_fill.png');
      const card = reactive({
        cn: '',
        type: '',
        create_datetime: '',
        url: '',
        degree: 0,
        list: '',
        erro_msg: '',
        isFalse: false,
      });
      let option = ref([{
        label:'',
        value:''
      }
      ]);
      const deleteId = ref();
      const urlFirst = ref('/basic-api/');
      const deleteVisible = ref(false);
      const protect = ref('');
      const animalType = ref('');
      const photoTime = ref('');
      const fileType = ref('');
      const deviceType = ref('');
      const visible = ref(false);
      const visible1 = ref(false);
      const opt = ref('');
      const tableKey = ref(1);
      const [registers, { openModal }] = useModal();
      const [registerDrawer, { openDrawer }] = useDrawer();
      const [register, { setProps, updateSchema }] = useForm({
        labelWidth: 100,
        schemas: searchFormSchema,
        actionColOptions: {
          span: 15,
        },
      });

      var handleOk = (e: MouseEvent) => {
       // console.log(e);
        visible.value = false;
      };
      var handleOk1 = (e: MouseEvent) => {
        visible1.value = false;
        deleteD(deleteId.value);
        getData();
      };
      function deleteData(id) {
        deleteId.value = id;
        visible1.value = true;
      }
      function handleSuccess() {
        message.success('请求成功');
        reload();
      }
      function changeLike(list) {
        if (list.isExcellent) {
          list.isExcellent = false;
          const id = list.id;
          const params = list;
          updateLike(params, id);
        } else {
          list.isExcellent = true;
          const id = list.id;
          const params = list;
          updateLike(params, id);
        }
      }
      function ReSet() {
        protect.value = '';
        animalType.value = '';
        photoTime.value = '';
        fileType.value = '';
        deviceType.value = '';
        lists.value = resourceLists.value;
      }
      function showLike(isExcellent) {
        if (isExcellent) {
          return '/resource/img/like_fill.png';
        } else {
          return '/resource/img/like.png';
        }
      }
      function showModal(cn, type, degree, create_datetime, url, isFalse, erro_msg, list) {
        card.cn = cn;
        card.type = type;
        card.degree = degree;
        card.create_datetime = create_datetime;
        card.url = url;
        card.isFalse = isFalse;
        card.erro_msg = erro_msg;
        card.list = list;
       // console.log(list, 'list');
        visible.value = true;
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
      const lists = ref([]);
      const resourceLists = ref([]);
      function handlePageSizeChange(current, pageSize) {
        paginationData.defaultCurrent = 1;
        paginationData.defaultPageSize = pageSize;
        if(searchTem.area_id===''&&searchTem.cn===''&&searchTem.point_id===''&&searchTem.equipment_name===''&&searchTem.start_time===''&&searchTem.end_time===''){
          getData2();
        } else {
          search(searchTem.cn, searchTem.point_id, searchTem.area_id, searchTem.equipment_name, searchTem.start_time, searchTem.end_time)
        }
      }
      function handlePageNoChange(current, size) {
        paginationData.defaultCurrent = current;
        paginationData.defaultPageSize = size;
        if(searchTem.area_id===''&&searchTem.cn===''&&searchTem.point_id===''&&searchTem.equipment_name===''&&searchTem.start_time===''&&searchTem.end_time===''){
          getData2();
        } else {
          search(searchTem.cn, searchTem.point_id, searchTem.area_id, searchTem.equipment_name, searchTem.start_time, searchTem.end_time)
        }
      }
      let paginationData = reactive({
        total: 0,
        defaultCurrent: 1, // 默认当前页数
        defaultPageSize: 12, // 默认当前页显示数据的大小
      });
      function showtotal(){
        return `共 ${paginationData.total} 条数据`;
      }
      const lists2 = ref([]);
      let pointid = ref([{
        label:'',
        value:''
      }
      ]);
      let areaid = ref([{
        label:'',
        value:''
      }
      ]);
      let searchTem = reactive({
        area_id: '',
        cn: '',
        point_id: '',
        equipment_name: '',
        start_time: '',
        end_time: '',
      });
      function getData() {
        getList({}).then((res) => {
          lists2.value = res.items;
          paginationData.total = res.total;
          for (let key in searchTem) {
            searchTem[key] = '';
          }
        });
        getList3({}).then((res) => {
          let tem = res.items;
          for(let i = 0;i < tem.length; i++){
            pointid.value.push({label:tem[i].point_name,value:tem[i].point_id});
          }
        });
        getList4({}).then((res) => {
          let tem = res.items;
          //console.log(res, 'res2');
          for(let i = 0;i < tem.length; i++){
            areaid.value.push({label:tem[i].name,value:tem[i].id});
          }
        });
        getList5({}).then((res) => {
          let tem = res.items;
          //console.log(res, 'res5');
          for(let i = 0;i < tem.length; i++){
            option.value.push({label:tem[i].cn,value:tem[i].cn});
          }
        });
      }
      function getData2() {
        getList({
          pageSize: paginationData.defaultPageSize,
          page: paginationData.defaultCurrent,
        }).then((res) => {
          lists2.value = res.items;
          paginationData.total = res.total;
          for (let key in searchTem) {
            searchTem[key] = '';
          }
        });
      }
      function open(params) {
        if (params.isFalse) {
          params.isFalse = false;
          const id = params.id;
          const params1 = params;
          updateLike(params1, id);
        } else {
          params.isFalse = true;
          const id = params.id;
          const params1 = params;
          updateLike(params1, id);
        }
      }
      function handleChange(params, value) {
        //console.log(value, 'value');
        if (params.isFalse) {
          params.erro_msg = value;
          const id = params.id;
          const params1 = params;
          updateLike(params1, id);
        } else {
          params.erro_msg = '';
          const id = params.id;
          const params1 = params;
          updateLike(params1, id);
        }
      }
      function search(animalType, pointId, areaId, deviceType, startTime, endTime) {
        getList({
          area_id: areaId,
          cn: animalType,
          point_id: pointId,
          equipment_name: deviceType,
          start_time: startTime,
          end_time: endTime,
          pageSize: paginationData.defaultPageSize,
          page: paginationData.defaultCurrent,
        }).then((res) => {
          //console.log('ressdad', res);
          lists2.value = res.items;
          paginationData.total = res.total;
          searchTem.area_id = areaId;
          searchTem.cn = animalType;
          searchTem.point_id = pointId;
          searchTem.equipment_name = deviceType;
          searchTem.start_time = startTime;
          searchTem.end_time = endTime;
        });
      }
      function handleCreate() {
        openDrawer(true, {
          isUpdate: false,
        });
      }
      onMounted( async() => {
        getData();
        await updateSchema([
        {
          field: 'point_id',
          componentProps: {
             options: pointid.value,
          },
        },
        {
          field: 'area_id',
          componentProps: {
             options: areaid.value,
          },
        }
        ]);
      });
      return {
        option,
        handleChange,
        open,
        handleOk,
        showModal,
        changeLike,
        showLike,
        ReSet,
        search,
        handleCreate,
        registerDrawer,
        openDrawer,
        handleBulkDelete,
        deleteData,
        getData,
        getData2,
        register,
        handleSuccess,
        setProps,
        handleOk1,
        handleSubmit: (values: any) => {
          //console.log(values);
          search(values.cn, values.point_id, values.area_id, values.equipment_name, values.start_time,values.end_time);
          createMessage.success('查询成功');
        },
        updateSchema,
        registers,
        openModal,
        deleteId,
        urlFirst,
        tableKey,
        deleteVisible,
        resourceLists,
        visible,
        lists,
        card,
        like,
        protect,
        animalType,
        photoTime,
        fileType,
        deviceType,
        opt,
        visible1,
        handlePageSizeChange,
        handlePageNoChange,
        lists2,
        pointid,
        areaid,
        paginationData,
        showtotal,
        searchTem,
      };
    },
  });
</script>
<style scoped lang="less">
  :deep(.ant-col-15) {
    flex: revert;
  }
  .bigBox {
    display: inline-block;
    float: left;
    height: auto;
    width: auto;
    margin-left: 2%;
    margin-top: 20px;
    border-radius: 10px;
    border: 2px solid #c0c0c0;
    box-shadow: #c0c0c0 0px 0px 10px 1px;
    width: 230px;
    position: relative;
  }
  .title {
    position: relative;
  }

  .content {
    color: #a9a9a9;
    font-weight: 500;
    font-style: italic;
    position: relative;
  }

  .like {
    display: inline-block;
    height: 20px;
    position: absolute;
    right: 10px;
    margin-right: 10px;
  }

  .box {
    padding: 0px 10px;
    margin-bottom: 5px;
  }

  .message {
    color: #c0c0c0;
    font-weight: 300;
  }

  .img1 {
    width: 250px;
    margin: 0 auto;
    margin-top: 30px;
    margin-bottom: 10px;
  }

  .lbox {
    border-bottom: 1px solid #a9a9a9;
    margin-bottom: 10px;
  }

  .mov {
    margin-bottom: 5px;
    height: 120px;
  }

  #box1 {
    color: #a9a9a9;
    margin-top: 20px;
  }

  .content1 {
    float: right;
    color: green;
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
    height: 450px;
    margin: 20px auto;
  }
  .Mlbox {
    margin: 14px 18px;
  }

  .lcontent {
    display: inline-block;
    margin-left: 20px;
    font-weight: 600;
  }
  .vbox {
    margin-top: 10px;
    padding-bottom: 10px;
    border-radius: 3px;
    width: 200px;
    height: 120px;
  }

  .button {
    position: absolute;
    margin-top: -72px;
    margin-left: 84.5%;
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
  .errorRecord {
    margin: 2px;
    position: relative;
    left: 60%;
  }
  .ebox {
    height: 44px;
  }
  .jqbox {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    margin-left: 2vh;
  }
</style>
