<template>
  <div>
    <a-modal
      v-model:visible="visible"
      title="设备信息"
      style="top: 20px"
      width="1000px"
      @ok="handleOk"
      :footer="null"
      @cancel="handelCancel"
    >
      <div class="box">
        <div class="form-item">
          <div class="item-clo">
            <div class="text">是否使用模板</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="tempName"
              class="select"
              :options="temp"
              @change="handleChange"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">设备编号</div>
            <a-input v-model:value="equipment_number" :disabled="isRead" class="inp" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">视频直播</div>
            <a-input v-model:value="living_url" class="inp" :disabled="isRead" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">点位名称</div>
            <a-input v-model:value="point_name" class="inp" :disabled="isRead" />
          </div>
          <div class="item-clo2">
            <a-button v-show="!isRead" type="primary" class="btn" @click="showModal2()"
              >选择</a-button
            >
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">点位编号</div>
            <a-input v-model:value="point_id" class="inp" :disabled="isRead" />
          </div>
          <div class="item-clo">
            <div class="text">范围</div>
            <a-input v-model:value="range" :disabled="isRead" class="inp" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">设备名称</div>
            <a-input class="inp" :disabled="isRead" v-model:value="name" />
          </div>
          <div class="item-clo">
            <div class="text">设备型号</div>
            <a-input class="inp" :disabled="isRead" v-model:value="model" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">设备类型</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="type"
              class="select"
              :options="options"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">设备状态</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="status"
              class="select"
              :options="equipmentStatus"
              placeholder="请选择"
            />
          </div>
        </div>

        <div class="form-item">
          <div class="item-clo">
            <div class="text">拍摄帧率(每秒)</div>
            <a-input class="inp" :disabled="isRead" v-model:value="fps" />
          </div>
          <div class="item-clo">
            <div class="text">系统总像素</div>
            <a-input class="inp" :disabled="isRead" v-model:value="pixel" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">微镜头分辨率</div>
            <a-input class="inp" :disabled="isRead" v-model:value="resolution" />
          </div>
          <div class="item-clo">
            <div class="text">外观尺寸</div>
            <a-input class="inp" :disabled="isRead" v-model:value="size" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">拍照开始时间</div>
            <a-time-picker
              value-format="HH:mm:ss"
              v-model:value="startTime"
              style="width: 55%; margin: 0 1vh 0 9vh"
            />
            <!-- <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="hours"
              class="selectTime"
              :options="hour"
              placeholder="时"
            >
            </a-select>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="mins"
              class="selectTime"
              :options="min"
              placeholder="分"
            >
            </a-select>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="secs"
              class="selectTime"
              :options="sec"
              placeholder="秒"
            >
            </a-select> -->
          </div>
          <div class="item-clo">
            <div class="text">拍照结束时间</div>
            <a-time-picker
              value-format="HH:mm:ss"
              v-model:value="endTime"
              style="width: 55%; margin: 0 1vh 0 9vh"
            />
            <!-- <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="houre"
              class="selectTime"
              :options="hour"
              placeholder="时"
            >
            </a-select>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="mine"
              class="selectTime"
              :options="min"
              placeholder="分"
            >
            </a-select>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="sece"
              class="selectTime"
              :options="sec"
              placeholder="秒"
            >
            </a-select> -->
          </div>
        </div>
        <div class="form-item" style="margin-top: 2vh">
          <div class="item-clo">
            <div class="text">拍照间隔时间</div>
            <a-input class="inp" :disabled="isRead" v-model:value="interval_time" />
          </div>
          <div class="item-clo">
            <div class="text">重量</div
            ><a-input class="inp" :disabled="isRead" v-model:value="weight" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">输入电压</div>
            <a-input class="inp" :disabled="isRead" v-model:value="input_voltage" />
          </div>
          <div class="item-clo">
            <div class="text">电源功率</div
            ><a-input class="inp" :disabled="isRead" v-model:value="power_supply" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">是否防水</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="is_waterproof"
              class="select"
              :options="bool"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">防水等级</div
            ><a-input class="inp" :disabled="isRead" v-model:value="waterproof_grade" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">是否防尘</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="is_dustproof"
              class="select"
              :options="bool"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">防尘等级</div
            ><a-input class="inp" :disabled="isRead" v-model:value="dustproof_grade" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">设备品牌</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="brand"
              class="select"
              :options="brands"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">拍照图片是否审核</div
            ><a-select
              ref="select"
              :disabled="isRead"
              v-model:value="is_examine"
              class="select"
              :options="bool"
              placeholder="请选择"
            />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">经度</div>
            <a-input class="inp" :disabled="isRead" v-model:value="longitude" />
          </div>
          <div class="item-clo">
            <div class="text">纬度</div
            ><a-input :disabled="isRead" class="inp" v-model:value="latitude" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">是否开启大数据展示</div>
            <a-select
              ref="select"
              :disabled="isRead"
              v-model:value="is_dataShow"
              class="select"
              :options="bool"
              placeholder="请选择"
            />
          </div>
          <div class="item-clo">
            <div class="text">是否用于大屏显示</div
            ><a-select
              ref="select"
              :disabled="isRead"
              v-model:value="is_screenShow"
              class="select"
              :options="bool"
              placeholder="请选择"
            />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">云设备id</div>
            <a-input class="inp" :disabled="isRead" v-model:value="equipment_id" />
          </div>
          <div class="item-clo">
            <div class="text">云设备通道号</div
            ><a-input class="inp" :disabled="isRead" v-model:value="channel_number" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">摄像头ip</div>
            <a-input class="inp" :disabled="isRead" v-model:value="equipment_Ip" />
          </div>
          <div class="item-clo">
            <div class="text">摄像头端口</div
            ><a-input class="inp" :disabled="isRead" v-model:value="equipment_port" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo">
            <div class="text">摄像头账号</div>
            <a-input class="inp" :disabled="isRead" v-model:value="equipment_count" />
          </div>
          <div class="item-clo">
            <div class="text">摄像头密码</div
            ><a-input class="inp" :disabled="isRead" v-model:value="equipment_password" />
          </div>
        </div>
        <div class="form-item">
          <div class="item-clo1">
            <div>备注</div>
            <a-textarea
              :disabled="isRead"
              v-model:value="notes"
              placeholder="备注(非必填项)"
              :auto-size="{ minRows: 4 }"
              allow-clear
              class="inpArea"
            />
          </div>
        </div>
      </div>
      <div class="footer">
        <a-button type="default" @click="handelCancel">取消</a-button>
        <a-button class="sure" @click="handleOk">确定</a-button>
      </div>
    </a-modal>
    <a-modal v-model:visible="visible2" title="选择" width="700px" @ok="handleOk2">
      <div
        ><a-input
          v-model:value="k_name"
          style="width: 30vh; margin-left: 5vh"
          placeholder="动物名称"
        />
        <a-button type="primary" style="margin-left: 5vh" @click="selectPoint">查询</a-button>
        <a-button style="margin-left: 1vh" @click="reset">重置</a-button></div
      >
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
            {
              type: 'button',
              icon: 'ant-design:video-camera-outlined',
              color: 'primary',
              auth: ['post:update'],
              onClick: liveVideo.bind(null, record),
            },
          ]"
        />
      </template>
    </BasicTable>
    <DemoDrawer @register="registerDrawer" @success="handleSuccess" />
    <Modal v-model:visible="visible03" title="视频直播" @ok="handleOk2" style="width: 900px;" :footer="null">
      <template v-for="list in lists" :key="list.id">
        <div  v-if="list.id === am&&list.living_url.length==0">
          <p style="text-align:center;font-size:16px;font-weight:400;padding:10px 0">暂无数据</p>
        </div>
      <iframe
        id="video"
        v-if="list.id === am&&list.living_url"
        :src="list.living_url"
        
        style="margin: 10px auto;margin-bottom: 10px;padding-bottom: 15px;"
        width="800px"
        height="450px"
        allow="autoplay"
      ></iframe>
    </template>
    </Modal>
  </div>
</template>
<script lang="ts">
import { defineComponent, ref, reactive, computed, watch, toRaw, onMounted } from 'vue';
import ImgUpload from '/@/components/Tinymce/src/ImgUpload.vue';
import { BasicTable, useTable, TableAction } from '/@/components/Table';
import { usePermission } from '/@/hooks/web/usePermission';
import { useDrawer } from '/@/components/Drawer';
import DemoDrawer from './Drawer.vue';
import { Space, Modal } from 'ant-design-vue';
import { BasicUpload } from '/@/components/Upload';
import { deleteItem, getList, exportData, importData, createOrUpdate } from './api';
import { PgetList } from './pointApi';
import { TgetList } from './tempApi';
import { columns, searchFormSchema, hour, min, sec } from './data';
import { message } from 'ant-design-vue';
import { useMessage } from '/@/hooks/web/useMessage';
import { downloadByData } from '/@/utils/file/download';
import dayjs, { Dayjs } from 'dayjs';
export default defineComponent({
  name: 'Animal',
  components: { BasicTable, DemoDrawer, TableAction, BasicUpload, Space, ImgUpload , Modal },
  setup() {
    const dataSource = reactive({
      arr: [],
    });

    const columnsA = [
      { title: '点位编号', dataIndex: 'id', key: 'id' },
      { title: '名称', dataIndex: 'name', key: 'name' },
      {
        title: '操作',
        key: 'operation',
        fixed: 'right',
        width: 120,
      },
    ];
    let startTime = ref<string>('08:00:00');
    let endTime = ref<string>('16:00:00');
    let temp = ref<SelectProps['options']>([]);
    let tempName = ref('');
    let id = ref('');
    let isRead = ref(false);
    const isUpdate = ref<boolean>(false);
    let point_id = ref('');
    let living_url = ref('');
    let point_name = ref('');
    let range = ref('');
    let equipment_number = ref('');
    let name = ref('');
    let model = ref('');
    let type = ref('');
    let status = ref('');
    let fps = ref('');
    let pixel = ref('');
    let resolution = ref('');
    let size = ref('');
    let hours = ref('');
    let mins = ref('');
    let secs = ref('');
    let houre = ref('');
    let mine = ref('');
    let sece = ref('');
    let interval_time = ref('');
    let weight = ref('');
    let input_voltage = ref('');
    let power_supply = ref('');
    let is_waterproof = ref(false);
    let waterproof_grade = ref('');
    let is_dustproof = ref(false);
    let dustproof_grade = ref('');
    let brand = ref('');
    let is_examine = ref(false);
    let longitude = ref('');
    let latitude = ref('');
    let equipment_id = ref('');
    let is_dataShow = ref(false);
    let is_screenShow = ref(false);
    let channel_number = ref('');
    let equipment_Ip = ref('');
    let equipment_count = ref('');
    let equipment_port = ref('');
    let equipment_password = ref('');
    let notes = ref('');
    const bool = ref<SelectProps['options']>([
      { value: false, label: '否' },
      { value: true, label: '是' },
    ]);
    const equipmentStatus = ref<SelectProps['options']>([
      { value: '正常', label: '正常' },
      { value: '故障', label: '故障' },
      { value: '报废', label: '报废' },
    ]);
    const brands = ref<SelectProps['options']>([
      { value: 'HUAWEI', label: 'HUAWEI' },
      { value: 'WEIZHI', label: 'WEZHI' },
    ]);
    const options = ref<SelectProps['options']>([
      {
        value: 'A型',
        label: 'A型',
      },
      {
        value: 'B型',
        label: 'B型',
      },
      {
        value: 'C型',
        label: 'C型',
      },
    ]);

    const visible = ref<boolean>(false);
    const visible03 = ref<boolean>(false);

    const showVideo = () => {
      visible03.value = true;
    };

    const showModal = () => {
      visible.value = true;
    };

    const handleOk = (e: MouseEvent) => {
      if (isRead.value != true) {
        let form = {
          name: name.value,
          model: model.value,
          type: type.value,
          status: status.value,
          fps: fps.value,
          pixel: pixel.value,
          resolution: resolution.value,
          size: size.value,
          point_id: point_id.value,
          living_url:living_url.value,
          point_name: point_name.value,
          range: range.value,
          start_time: startTime.value,
          end_time: endTime.value,
          interval_time: interval_time.value,
          weight: weight.value,
          input_voltage: input_voltage.value,
          power_supply: power_supply.value,
          is_waterproof: is_waterproof.value,
          waterproof_grade: waterproof_grade.value,
          is_dustproof: is_dustproof.value,
          dustproof_grade: dustproof_grade.value,
          brand: brand.value,
          is_examine: is_examine.value,
          longitude: longitude.value,
          latitude: latitude.value,
          equipment_id: equipment_id.value,
          is_dataShow: is_dataShow.value,
          is_screenShow: is_screenShow.value,
          channel_number: channel_number.value,
          equipment_Ip: equipment_Ip.value,
          equipment_count: equipment_count.value,
          equipment_port: equipment_port.value,
          equipment_password: equipment_password.value,
          notes: notes.value,
          equipment_number: equipment_number.value,
        };
        if (isUpdate.value != true) {
          // console.log(startTime.value);
          // console.log(endTime.value);
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
          let form2 = {
            id: id.value,
            name: name.value,
            model: model.value,
            type: type.value,
            status: status.value,
            fps: fps.value,
            pixel: pixel.value,
            resolution: resolution.value,
            size: size.value,
            point_id: point_id.value,
            living_url:living_url.value,
            point_name: point_name.value,
            range: range.value,
            start_time: startTime.value,
            end_time: endTime.value,
            interval_time: interval_time.value,
            weight: weight.value,
            input_voltage: input_voltage.value,
            power_supply: power_supply.value,
            is_waterproof: is_waterproof.value,
            waterproof_grade: waterproof_grade.value,
            is_dustproof: is_dustproof.value,
            dustproof_grade: dustproof_grade.value,
            brand: brand.value,
            is_examine: is_examine.value,
            longitude: longitude.value,
            latitude: latitude.value,
            equipment_id: equipment_id.value,
            is_dataShow: is_dataShow.value,
            is_screenShow: is_screenShow.value,
            channel_number: channel_number.value,
            equipment_Ip: equipment_Ip.value,
            equipment_count: equipment_count.value,
            equipment_port: equipment_port.value,
            equipment_password: equipment_password.value,
            notes: notes.value,
            equipment_number: equipment_number.value,
          };
          // console.log(startTime.value);
          //console.log(endTime.value);
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
      tempName.value = '';
      name.value = '';
      model.value = '';
      type.value = '';
      status.value = '';
      fps.value = '';
      pixel.value = '';
      resolution.value = '';
      size.value = '';
      point_id.value = '';
      living_url.value = '';
      point_name.value = '';
      range.value = '';
      startTime.value = '08:00:00';
      endTime.value = '16:00:00';
      interval_time.value = '';
      weight.value = '';
      input_voltage.value = '';
      power_supply.value = '';
      is_waterproof.value = true;
      waterproof_grade.value = '';
      is_dustproof.value = true;
      dustproof_grade.value = '';
      brand.value = '';
      is_examine.value = true;
      longitude.value = '';
      latitude.value = '';
      equipment_id.value = '';
      is_dataShow.value = true;
      is_screenShow.value = true;
      channel_number.value = '';
      equipment_Ip.value = '';
      equipment_count.value = '';
      equipment_port.value = '';
      equipment_password.value = '';
      equipment_number.value = '';
      notes.value = '';
      isRead.value = false;
      visible.value = false;
    };
    const handelCancel = (e: MouseEvent) => {
      tempName.value = '';
      isRead.value = false;
      name.value = '';
      model.value = '';
      type.value = '';
      status.value = '';
      fps.value = '';
      pixel.value = '';
      resolution.value = '';
      size.value = '';
      point_id.value = '';
      living_url.value = '';
      point_name.value = '';
      range.value = '';
      startTime.value = '08:00:00';
      endTime.value = '16:00:00';
      interval_time.value = '';
      weight.value = '';
      input_voltage.value = '';
      power_supply.value = '';
      is_waterproof.value = true;
      waterproof_grade.value = '';
      is_dustproof.value = true;
      dustproof_grade.value = '';
      brand.value = '';
      is_examine.value = true;
      longitude.value = '';
      latitude.value = '';
      equipment_id.value = '';
      is_dataShow.value = true;
      is_screenShow.value = true;
      channel_number.value = '';
      equipment_Ip.value = '';
      equipment_count.value = '';
      equipment_port.value = '';
      equipment_password.value = '';
      notes.value = '';
      equipment_number.value = '';
      visible.value = false;
    };
    const visible2 = ref<boolean>(false);
    const visible3 = ref<boolean>(false);
    const showModal2 = () => {
      PgetList().then((res) => {
        dataSource.arr = res.items;
      });
      visible2.value = true;
    };
    const showModal3 = () => {
      visible3.value = true;
    };

    const handleOk2 = (e: MouseEvent) => {
      // console.log(e);
      visible2.value = false;
      visible03.value = false;
      visible3.value = false;
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
    let am = ref('');
    const lists = ref([]);
    function getData(){
      getList({}).then((res) =>{
        lists.value = res.items;
        // console.log(res,'res');
        
      })
    }
    function liveVideo(record: Recordable, Read) {
      am.value = record.id;
      isRead.value = Read;
      living_url.value = record.living_url;
      showVideo();
    }
    function handleEdit(record: Recordable, Read) {
      isRead.value = Read;
      isUpdate.value = true;
      id.value = record.id;
      name.value = record.name;
      model.value = record.model;
      type.value = record.type;
      status.value = record.status;
      fps.value = record.fps;
      pixel.value = record.pixel;
      resolution.value = record.resolution;
      size.value = record.size;
      point_id.value = record.point_id;
      range.value = record.range;
      point_name.value = record.point_name;
      startTime.value = record.start_time;
      endTime.value = record.end_time;
      interval_time.value = record.interval_time;
      weight.value = record.weight;
      input_voltage.value = record.input_voltage;
      power_supply.value = record.power_supply;
      is_waterproof.value = record.is_waterproof;
      waterproof_grade.value = record.waterproof_grade;
      is_dustproof.value = record.is_dustproof;
      dustproof_grade.value = record.dustproof_grade;
      brand.value = record.brand;
      is_examine.value = record.is_examine;
      longitude.value = record.longitude;
      latitude.value = record.latitude;
      equipment_id.value = record.equipment_id;
      is_dataShow.value = record.is_dataShow;
      is_screenShow.value = record.is_screenShow;
      channel_number.value = record.channel_number;
      equipment_Ip.value = record.equipment_Ip;
      equipment_count.value = record.equipment_count;
      equipment_port.value = record.equipment_port;
      equipment_password.value = record.equipment_password;
      notes.value = record.notes;
      equipment_number.value = record.equipment_number;
      living_url.value = record.living_url;
      showModal();
      // openDrawer(true, {
      //   record,
      //   isUpdate: true,
      // });
    }
    function selectPoint() {
      // dataSource.arr = dataSource.arr.filter((item)=>{
      //   if(item.name == k_name.value){
      //     return
      //   }
      // })
      PgetList({ name: point_name.value }).then((res) => {
        dataSource.arr = res.items;
      });
    }
    function show(record) {
      point_id.value = record.id;
      point_name.value = record.name;
      longitude.value = record.longitude;
      latitude.value = record.latitude;
      visible2.value = false;
    }
    function reset() {
      point_name.value = '';
      point_id.value = '';
      PgetList().then((res) => {
        dataSource.arr = res.items;
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
      // await importData({ path: list[0] });
      // message.success(`导入成功`);
      // await reload();
      TgetList({ name: tempName.value }).then((res) => {
        model.value = res.items[0].model;
        type.value = res.items[0].type;
        fps.value = res.items[0].fps;
        pixel.value = res.items[0].pixel;
        resolution.value = res.items[0].resolution;
        size.value = res.items[0].size;
        weight.value = res.items[0].weight;
        input_voltage.value = res.items[0].input_voltage;
        power_supply.value = res.items[0].power_supply;
        is_waterproof.value = res.items[0].is_waterproof;
        waterproof_grade.value = res.items[0].waterproof_grade;
        is_dustproof.value = res.items[0].is_dustproof;
        dustproof_grade.value = res.items[0].dustproof_grade;
      });
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
      getData();
      TgetList().then((res) => {
        res.items.forEach((item) => {
          let newObj = {
            value: item.name,
            label: item.name,
          };
          temp.value.push(newObj);
        });
      });
    });
    return {
      lists,
      am,
      startTime,
      endTime,
      tempName,
      temp,
      brands,
      dataSource,
      columnsA,
      point_id,
      living_url,
      point_name,
      range,
      isRead,
      equipmentStatus,
      id,
      name,
      model,
      type,
      status,
      fps,
      pixel,
      resolution,
      size,
      hours,
      mins,
      secs,
      houre,
      mine,
      sece,
      interval_time,
      weight,
      input_voltage,
      power_supply,
      is_waterproof,
      waterproof_grade,
      is_dustproof,
      dustproof_grade,
      brand,
      is_examine,
      longitude,
      latitude,
      equipment_id,
      is_dataShow,
      is_screenShow,
      channel_number,
      equipment_Ip,
      equipment_count,
      equipment_port,
      equipment_password,
      notes,
      bool,
      hour,
      min,
      sec,
      options,
      visible,
      visible03,
      equipment_number,
      showVideo,
      showModal,
      handleOk,
      handelCancel,
      visible2,
      visible3,
      selectPoint,
      getData,
      show,
      reset,
      showModal2,
      showModal3,
      handleOk2,
      registerTable,
      registerDrawer,
      handleCreate,
      handleEdit,
      liveVideo,
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
  padding: 1vh 1vh 0vh 14%;
  display: flex;
  width: 80%;
}
.item-clo2 {
  padding: 1vh 1vh 0vh 0vh;
  display: flex;
  width: 50%;
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
.selectTime {
  margin: 0vh 1vh 1vh 2vh;
  float: right;
  width: 15%;
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
  height: 90%;
  object-fit: contain;
}
.imgBox {
  padding: 1vh;
  border: 1px #e6e6e6 solid;
  width: 180px;
  height: 210px;
}
.inpArea {
  margin: 0vh 1vh 1vh 5vh;
  float: right;
  width: 70%;
}
.footer {
  display: flex;
  margin-top: 20px;
  margin-left: 82%;
}
.sure {
  background-color: #339966 !important;
  color: white;
  border-color: #339966 !important;
  margin-left: 15px;
}
.ant-modal .ant-modal-body{
  padding: 5px;
}
</style>
