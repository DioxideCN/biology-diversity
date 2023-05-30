<template>
  <div>
    <a-modal
      v-model:visible="visible"
      title="植物信息"
      style="top: 20px"
      width="1000px"
      @ok="handleOk"
      @cancel="handelCancel"
    >
      <div class="box">
        <div class="form-item">
          <div class="item-clo">
            <div class="text">中文学名</div>
            <a-input v-model:value="cn" class="inp" :disabled="isRead" />
          </div>
          <div class="item-clo">
            <div class="text">识别编号</div>
            <a-input v-model:value="recognition_id" class="inp" :disabled="isRead" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">植物知识库</div>
            <a-input v-model:value="k_name" class="inp" :disabled="isRead" />
          </div>
          <div class="item-clo1">
            <a-button v-show="!isRead" type="primary" class="btn" @click="showModal2()"
              >选择</a-button
            >
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">植物知识库编号</div>
            <a-input v-model:value="k_id" class="inp" :disabled="isRead" />
          </div>
          <div class="item-clo">
            <div class="text">拉丁学名</div>
            <a-input v-model:value="ladin" :disabled="isRead" class="inp" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">英文名称</div>
            <a-input :disabled="isRead" v-model:value="en" class="inp" />
          </div>
          <div class="item-clo">
            <div class="text">别称</div>
            <a-input :disabled="isRead" v-model:value="other_name" class="inp" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">命名者</div>
            <a-input :disabled="isRead" v-model:value="name_man" class="inp" />
          </div>
          <div class="item-clo">
            <div class="text">命名时间</div>
            <a-input v-model:value="name_date" :disabled="isRead" class="inp" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">是否重点保护物种</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="is_protected"
              class="select"
              :options="bool"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">保护等级</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="protection_level"
              class="select"
              :options="level"
              placeholder="请选择"
            />
          </div>
        </div>
        <div class="form-item" style="margin-top: 2vh">
          <div class="item-clo">
            <div class="text">大类名称</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="big_class"
              class="select"
              :options="big_classes"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">小类名称</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="sub_class"
              class="select"
              :options="sub_classes"
              placeholder="请选择"
            />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">界</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="kingdom"
              class="select"
              :options="jie"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">属</div>
            <a-input v-model:value="genus" :disabled="isRead" class="inp" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">门</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="phylum"
              class="select"
              :options="men"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">亚门</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="subphylum"
              class="select"
              :options="yamen"
              placeholder="请选择"
            />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">纲</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="gang"
              class="select"
              :options="gan"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">亚纲</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="subclass"
              class="select"
              :options="yagan"
              placeholder="请选择"
            />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">目</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="order"
              class="select"
              :options="mu"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">亚目</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="suborder"
              class="select"
              :options="yamu"
              placeholder="请选择"
            />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">科</div>
            <a-input v-model:value="family" :disabled="isRead" class="inp" />
          </div>
          <div class="item-clo">
            <div class="text">亚科</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="subfamily"
              class="select"
              :options="yake"
              placeholder="请选择"
            />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">种</div>
            <a-input v-model:value="species" :disabled="isRead" class="inp" />
          </div>
          <div class="item-clo">
            <div class="text">亚种</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="subspecies"
              class="select"
              :options="yazhong"
              placeholder="请选择"
            />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">族</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="tribe"
              class="select"
              :options="zu"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">成长阶段</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="grow"
              class="select"
              :options="grows"
              placeholder="请选择"
            />
          </div>
        </div>
        <div class="form-item-img">
          <div class="imgBox">
            <a-upload
              name="file"
              list-type="txt"
              :customRequest="uploadImage"
              :maxCount="1"
              :showUploadList="false"
            >
              <div>
                <a-button :disabled="isRead"> <a-icon type="upload" />上传图片</a-button>
              </div>
            </a-upload>
            <div style="font-size: 20px">预览图</div>
            <a-image :src="imgSrc || '/src/assets/images/animal.png'" alt="" class="img" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo2">
            <div class="text">简介</div>
            <a-textarea
              v-model:value="introduction"
              :disabled="isRead"
              placeholder="请填写植物简介"
              :auto-size="{ minRows: 1 }"
              allow-clear
              class="inpArea"
            />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo2">
            <div class="text">备注</div>
            <a-textarea
              v-model:value="notes"
              :disabled="isRead"
              placeholder="请填写备注"
              :auto-size="{ minRows: 1 }"
              allow-clear
              class="inpArea"
            />
          </div>
        </div>
      </div>
    </a-modal>
    <a-modal v-model:visible="visible2" title="选择" width="700px" @ok="handleOk2">
      <div>
        <a-input
          v-model:value="k_name"
          style="width: 30vh; margin-left: 5vh"
          placeholder="植物名称"
        />
        <a-button type="primary" style="margin-left: 5vh" @click="selectAnimal">查询</a-button>
        <a-button style="margin-left: 1vh" @click="reset">重置</a-button>
      </div>
      <a-table :dataSource="dataSource.arr" :columns="columnsA" size="small"
        ><template #bodyCell="{ column, record }">
          <template v-if="column.key === 'operation'">
            <a @click="show(record)">选择</a>
          </template>
        </template></a-table
      >
    </a-modal>
    <BasicTable @register="registerTable">
      <template #tableTitle>
        <Space style="height: 40px">
          <a-button
            type="primary"
            v-auth="['post:add']"
            style="background-color: #339966; border-color: #339966"
            preIcon="ant-design:plus-outlined"
            @click="handleCreate"
          >
            新增
          </a-button>
          <a-button
            type="error"
            v-auth="['post:delete']"
            preIcon="ant-design:delete-outlined"
            style="color: rgba(0, 0, 0, 0.85); border-color: #d9d9d9; background: #fff"
            @click="handleBulkDelete"
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
              icon: 'ant-design:info-circle-filled',
              color: 'primary',
              onClick: handleEdit.bind(null, record, true),
            },
            {
              type: 'button',
              icon: 'clarity:note-edit-line',
              color: 'primary',
              auth: ['post:update'],
              onClick: handleEdit.bind(null, record, false),
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
    <DemoDrawer @register="registerDrawer" @success="handleSuccess" />
  </div>
</template>
<script lang="ts">
  import axios from 'axios';
  import { useUserStoreWithOut } from '/@/store/modules/user';
  import { getToken } from '/@/utils/auth';
  import { defineComponent, ref, reactive, computed, watch, toRaw, onMounted } from 'vue';
  import ImgUpload from '/@/components/Tinymce/src/ImgUpload.vue';
  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { usePermission } from '/@/hooks/web/usePermission';
  import { useDrawer } from '/@/components/Drawer';
  import DemoDrawer from './Drawer.vue';
  import { Space } from 'ant-design-vue';
  import { BasicUpload } from '/@/components/Upload';
  import { deleteItem, getList, exportData, importData, createOrUpdate, upload } from './api';
  import { KgetList } from './knowledgeApi';
  import { CgetList } from './classApi';
  import { columns, searchFormSchema } from './data';
  import { message } from 'ant-design-vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { downloadByData } from '/@/utils/file/download';
  import { useGlobSetting } from '/@/hooks/setting';

  const globSetting = useGlobSetting();
  export default defineComponent({
    name: 'Animal',
    components: { BasicTable, DemoDrawer, TableAction, BasicUpload, Space, ImgUpload },
    setup() {
      const userStore = useUserStoreWithOut();
      const token1 = userStore.getToken;

      const id = ref('');
      let token = ref('');
      let url = ref('');
      let isRead = ref(false);
      const isUpdate = ref<boolean>(false);
      const bool = ref<SelectProps['options']>([
        { value: false, label: '否' },
        { value: true, label: '是' },
      ]);
      let jie = ref<SelectProps['options']>([]);
      let men = ref<SelectProps['options']>([]);
      let yamen = ref<SelectProps['options']>([]);
      let gan = ref<SelectProps['options']>([]);
      let yagan = ref<SelectProps['options']>([]);
      let mu = ref<SelectProps['options']>([]);
      let yamu = ref<SelectProps['options']>([]);
      let yake = ref<SelectProps['options']>([]);
      let yazhong = ref<SelectProps['options']>([]);
      let zu = ref<SelectProps['options']>([]);
      let grows = ref<SelectProps['options']>([
        { value: '幼体', label: '幼体' },
        { value: '亚成体', label: '亚成体' },
        { value: '成体', label: '成体' },
      ]);
      const level = ref<SelectProps['options']>([
        { value: '灭绝', label: '灭绝' },
        { value: '野外灭绝', label: '野外灭绝' },
        { value: '极危', label: '极危' },
        { value: '濒危', label: '濒危' },
        { value: '易危', label: '易危' },
        { value: '近危', label: '近危' },
        { value: '低危', label: '低危' },
        { value: '数据缺乏', label: '数据缺乏' },
        { value: '未评估', label: '未评估' },
      ]);
      const state = reactive({
        arr: [],
      });

      const dataSource = reactive({
        arr: [],
      });
      const columnsA = [
        { title: '植物编号', dataIndex: 'animal_id', key: 'animal_id' },
        { title: '名称', dataIndex: 'name', key: 'name' },
        {
          title: '操作',
          key: 'operation',
          fixed: 'right',
          width: 100,
        },
      ];
      let k_id = ref('');
      let cn = ref('');
      let recognition_id = ref('');
      let k_name = ref('');
      let ladin = ref('');
      let en = ref('');
      let other_name = ref('');
      let name_man = ref('');
      let name_date = ref('');
      let is_protected = ref(true);
      let protection_level = ref('');
      let big_class = ref('');
      let sub_class = ref('');
      let kingdom = ref('');
      let genus = ref('');
      let phylum = ref('');
      let subphylum = ref('');
      let gang = ref('');
      let subclass = ref('');
      let order = ref('');
      let suborder = ref('');
      let family = ref('');
      let subfamily = ref('');
      let species = ref('');
      let subspecies = ref('');
      let tribe = ref('');
      let grow = ref('');
      let introduction = ref('');
      let notes = ref('');
      const big_classes = ref<SelectProps['options']>([
        {
          value: '植物',
          label: '植物',
        },
      ]);
      const sub_classes = ref<SelectProps['options']>([
        {
          value: '乔木',
          label: '乔木',
        },
        {
          value: '灌木',
          label: '灌木',
        },
        {
          value: '藤类',
          label: '藤类',
        },
        {
          value: '草本',
          label: '草本',
        },
      ]);
      let prefix = import.meta.env.VITE_GLOB_API_URL;
      let imgUrl = ref(''); //上传图片的src
      //该方法当上传列表新增上传和删除上传项都会执行，我们可以通过状态来获取最新的fileList内容，其中状/态有loading,removed,done。

      let imgSrc = computed(() => {
        // console.log('imgSrc', imgUrl.value);
        return imgUrl.value;
      });
      function uploadImage(file) {
        // console.log('in upload');
        // console.log(file.data.file);
        const formData = new FormData();
        formData.append('file', file.file);
        saveFile(formData);
      }

      function saveFile(file) {
        // console.log('save File');
        axios
          .post(globSetting.apiUrl + globSetting.urlPrefix + '/api/system/uploadImage', file)
          .then((res) => {
           // console.log('图片上传成功', res);
            imgUrl.value = res.data.url;
           // console.log('url:', imgUrl.value);
          })
          .catch(function (error) {
           // console.log(error);
          });
      }
      const visible = ref<boolean>(false);

      const showModal = () => {
        // CgetList().then((res) => {
        //   console.log(res);
        // });
        visible.value = true;
      };

      const handleOk = (e: MouseEvent) => {
        if (isRead.value != true) {
          let form = {
            cn: cn.value,
            recognition_id: recognition_id.value,
            k_name: k_name.value,
            k_id: k_id.value,
            ladin: ladin.value,
            en: en.value,
            other_name: other_name.value,
            name_man: name_man.value,
            name_date: name_date.value,
            is_protected: is_protected.value,
            protection_level: protection_level.value,
            big_class: big_class.value,
            sub_class: sub_class.value,
            kingdom: kingdom.value,
            genus: genus.value,
            phylum: phylum.value,
            subphylum: subphylum.value,
            gang: gang.value,
            subclass: subclass.value,
            order: order.value,
            suborder: suborder.value,
            family: family.value,
            subfamily: subfamily.value,
            species: species.value,
            subspecies: subspecies.value,
            tribe: tribe.value,
            grow: grow.value,
            url: imgUrl.value,
            introduction: introduction.value,
            notes: notes.value,
          };
          if (isUpdate.value != true) {
            createOrUpdate(form, isUpdate.value)
              .then(() => {
                message.success('创建成功');
                reload();
              })
              .catch(() => {
                message.error('创建失败');
                reload();
              });
          } else {
            let tempUrl = '';
            if (typeof imgUrl.value == 'string') {
              tempUrl = imgUrl.value;
            } else {
              tempUrl = imgUrl.value[imgUrl.value.length - 1];
            }
            let form2 = {
              id: id.value,
              cn: cn.value,
              recognition_id: recognition_id.value,
              k_name: k_name.value,
              k_id: k_id.value,
              ladin: ladin.value,
              en: en.value,
              other_name: other_name.value,
              name_man: name_man.value,
              name_date: name_date.value,
              is_protected: is_protected.value,
              protection_level: protection_level.value,
              big_class: big_class.value,
              sub_class: sub_class.value,
              kingdom: kingdom.value,
              genus: genus.value,
              phylum: phylum.value,
              subphylum: subphylum.value,
              gang: gang.value,
              subclass: subclass.value,
              order: order.value,
              suborder: suborder.value,
              family: family.value,
              subfamily: subfamily.value,
              species: species.value,
              subspecies: subspecies.value,
              tribe: tribe.value,
              grow: grow.value,
              url: imgUrl.value,
              introduction: introduction.value,
              notes: notes.value,
            };
            createOrUpdate(form2, isUpdate.value)
              .then(() => {
                message.success('更改成功');
                reload();
              })
              .catch(() => {
                message.error('更改失败');
                reload();
              });
          }
        }
        (cn.value = ''),
          (recognition_id.value = ''),
          (k_name.value = ''),
          (ladin.value = ''),
          (en.value = ''),
          (other_name.value = ''),
          (name_man.value = ''),
          (name_date.value = ''),
          (is_protected.value = false),
          (protection_level.value = ''),
          (big_class.value = ''),
          (sub_class.value = ''),
          (kingdom.value = ''),
          (genus.value = ''),
          (phylum.value = ''),
          (subphylum.value = ''),
          (gang.value = ''),
          (subclass.value = ''),
          (order.value = ''),
          (suborder.value = ''),
          (family.value = ''),
          (subfamily.value = ''),
          (species.value = ''),
          (subspecies.value = ''),
          (tribe.value = ''),
          (grow.value = ''),
          (introduction.value = ''),
          (notes.value = ''),
          (imgUrl.value = '');
        isUpdate.value = false;
        visible.value = false;
      };
      const handelCancel = (e: MouseEvent) => {
        isRead.value = false;
        isUpdate.value = false;
        visible.value = false;
        (cn.value = ''),
          (recognition_id.value = ''),
          (k_name.value = ''),
          (ladin.value = ''),
          (en.value = ''),
          (other_name.value = ''),
          (name_man.value = ''),
          (name_date.value = ''),
          (is_protected.value = false),
          (protection_level.value = ''),
          (big_class.value = ''),
          (sub_class.value = ''),
          (kingdom.value = ''),
          (genus.value = ''),
          (phylum.value = ''),
          (subphylum.value = ''),
          (gang.value = ''),
          (subclass.value = ''),
          (order.value = ''),
          (suborder.value = ''),
          (family.value = ''),
          (subfamily.value = ''),
          (species.value = ''),
          (subspecies.value = ''),
          (tribe.value = ''),
          (grow.value = ''),
          (introduction.value = ''),
          (notes.value = ''),
          (imgUrl.value = '');
        // (imgSrc.value = '');
      };
      const visible2 = ref<boolean>(false);
      const showModal2 = () => {
        KgetList().then((res) => {
          dataSource.arr = res.items;
        });
        visible2.value = true;
      };

      const handleOk2 = (e: MouseEvent) => {
       // console.log(e);
        visible2.value = false;
      };
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

      function handleCreate() {
        isRead.value = false;
        isUpdate.value = false;
        showModal();
        // openDrawer(true, {
        //   isUpdate: false,
        // });
      }

      function handleEdit(record: Recordable, Read) {
        isRead.value = Read;
        isUpdate.value = true;
        (id.value = record.id),
          (cn.value = record.cn),
          (recognition_id.value = record.recognition_id),
          (k_name.value = record.k_name),
          (k_id.value = record.k_id),
          (ladin.value = record.ladin),
          (en.value = record.en),
          (other_name.value = record.other_name),
          (name_man.value = record.name_man),
          (name_date.value = record.name_date),
          (is_protected.value = record.is_protected),
          (protection_level.value = record.protection_level),
          (big_class.value = record.big_class),
          (sub_class.value = record.sub_class),
          (kingdom.value = record.kingdom),
          (genus.value = record.genus),
          (phylum.value = record.phylum),
          (subphylum.value = record.subphylum),
          (gang.value = record.gang),
          (subclass.value = record.subclass),
          (order.value = record.order),
          (suborder.value = record.suborder),
          (family.value = record.family),
          (subfamily.value = record.subfamily),
          (species.value = record.species),
          (subspecies.value = record.subspecies),
          (tribe.value = record.tribe),
          (grow.value = record.grow),
          (introduction.value = record.introduction),
          (notes.value = record.notes),
          (imgUrl.value = record.url);
        showModal();

        // openDrawer(true, {
        //   record,
        //   isUpdate: true,
        // });
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
      function show(record) {
        k_id.value = record.id;
        k_name.value = record.name;
        visible2.value = false;
      }
      function selectAnimal() {
        KgetList({ name: k_name.value }).then((res) => {
          dataSource.arr = res.items;
        });
      }
      function reset() {
        k_name.value = '';
        k_id.value = '';
        KgetList().then((res) => {
          dataSource.arr = res.items;
        });
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
      onMounted(() => {
        token.value = getToken();
        // console.log(token1)
        // url.value = upload()
        CgetList({ type: '界' }).then((res) => {
          res.items.forEach((item) => {
            let newObj = {
              value: item.name,
              label: item.name,
            };
            jie.value.push(newObj);
          });
        });
        CgetList({ type: '门' }).then((res) => {
          res.items.forEach((item) => {
            let newObj = {
              value: item.name,
              label: item.name,
            };
            men.value.push(newObj);
          });
        });
        CgetList({ type: '亚门' }).then((res) => {
          res.items.forEach((item) => {
            let newObj = {
              value: item.name,
              label: item.name,
            };
            yamen.value.push(newObj);
          });
        });
        CgetList({ type: '纲' }).then((res) => {
          res.items.forEach((item) => {
            let newObj = {
              value: item.name,
              label: item.name,
            };
            gan.value.push(newObj);
          });
        });
        CgetList({ type: '亚纲' }).then((res) => {
          res.items.forEach((item) => {
            let newObj = {
              value: item.name,
              label: item.name,
            };
            yagan.value.push(newObj);
          });
        });
        CgetList({ type: '目' }).then((res) => {
          res.items.forEach((item) => {
            let newObj = {
              value: item.name,
              label: item.name,
            };
            mu.value.push(newObj);
          });
        });
        CgetList({ type: '亚目' }).then((res) => {
          res.items.forEach((item) => {
            let newObj = {
              value: item.name,
              label: item.name,
            };
            yamu.value.push(newObj);
          });
        });
        CgetList({ type: '亚科' }).then((res) => {
          res.items.forEach((item) => {
            let newObj = {
              value: item.name,
              label: item.name,
            };
            yake.value.push(newObj);
          });
        });
        CgetList({ type: '亚种' }).then((res) => {
          res.items.forEach((item) => {
            let newObj = {
              value: item.name,
              label: item.name,
            };
            yazhong.value.push(newObj);
          });
        });
        CgetList({ type: '族' }).then((res) => {
          res.items.forEach((item) => {
            let newObj = {
              value: item.name,
              label: item.name,
            };
            zu.value.push(newObj);
          });
        });
      });
      return {
        isRead,
        url,
        token,
        prefix,
        jie,
        men,
        yamen,
        gan,
        yagan,
        mu,
        yamu,
        yake,
        yazhong,
        zu,
        grows,
        show,
        reset,
        selectAnimal,
        id,
        isUpdate,
        k_id,
        cn,
        recognition_id,
        k_name,
        ladin,
        en,
        other_name,
        name_man,
        name_date,
        is_protected,
        protection_level,
        big_class,
        sub_class,
        kingdom,
        genus,
        phylum,
        subphylum,
        gang,
        subclass,
        order,
        suborder,
        family,
        subfamily,
        species,
        subspecies,
        tribe,
        grow,
        introduction,
        notes,
        dataSource,
        columnsA,
        state,
        bool,
        level,
        imgUrl,
        imgSrc,
        big_classes,
        sub_classes,
        visible,
        showModal,
        handleOk,
        handelCancel,
        visible2,
        showModal2,
        handleOk2,
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
        uploadImage,
        saveFile,
      };
    },
  });
</script>
<style scoped>
  .form-item {
    display: flex;
  }

  .item-clo {
    justify-content: flex-end;
    padding: 1vh 5vh 0vh 1vh;
    display: flex;
    width: 50%;
  }

  .item-clo1 {
    padding: 1vh 1vh 0vh 0vh;
    display: flex;
    width: 50%;
  }

  .item-clo2 {
    padding: 1vh 30vh 0vh 15%;
    display: flex;
    width: 100%;
  }

  .inp {
    margin: 0vh 1vh 1vh 5vh;
    float: right;
    width: 55%;
  }

  .select {
    margin: 0vh 1vh 1vh 5vh;
    float: right;
    width: 55%;
  }

  .text {
    margin: 0 0 0 2vh;
    white-space: nowrap;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .img {
    width: 100%;
    height: 90% !important;
    object-fit: contain;
  }

  .imgBox {
    margin-left: 20%;
    padding: 1vh;
    border: 1px #e6e6e6 solid;
    width: 30vh;
    height: 100%;
  }

  .inpArea {
    margin: 0vh 1vh 1vh 5vh;
    float: right;
    width: 80%;
  }
  .form-item-img {
    display: flex;
    height: 40vh;
  }
</style>
