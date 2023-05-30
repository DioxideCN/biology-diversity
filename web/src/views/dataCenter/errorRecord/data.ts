import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { useGlobSetting } from '/@/hooks/setting';
import { h } from 'vue';
import { Image } from 'ant-design-vue';
const { apiUrl } = useGlobSetting();

export const columns: BasicColumn[] = [
  {
    title: '识别类型',
    dataIndex: 'type',
    width: 100,
  },
  {
    title: '识别数量',
    dataIndex: 'recognition_number',
    width: 100,
  },
  {
    title: '识别结果',
    dataIndex: 'result',
    width: 100,
  },
  {
    title: '置信度',
    dataIndex: 'degree',
    width: 100,
  },
  {
    title: '识别时间',
    dataIndex: 'time',
    width: 180,
  },
  {
    title: '是否优秀',
    dataIndex: 'isExcellent',
    width: 180,
  },
  {
    title: '英文名',
    dataIndex: 'EnglishName',
    width: 180,
  },
  {
    title: '地点',
    dataIndex: 'place',
    width: 180,
  },
  {
    title: '设备',
    dataIndex: 'equipment',
    width: 180,
  },
  {
    title: '保护区',
    dataIndex: 'reserve',
    width: 180,
  },
  {
    title: '文件类型',
    dataIndex: 'fileType',
    width: 180,
  },
  {
    title: '图像',
    dataIndex: 'url',
    width: 80,
    customRender: ({ record }) => {
      const url = record.url;
      // console.log(apiUrl + url);
      return h(Image, { src: apiUrl + url, width: 40 });
    },
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'cn',
    label: '物种名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'point_id',
    label: '点位 ',
    component: 'Select',
    colProps: { span: 6 },
  },
  {
    field: 'area_id',
    label: '区域 ',
    component: 'Select',
    colProps: { span: 8 },
  },
  {
    field: 'equipment_name',
    label: '设备名称 ',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'start_time',
    label: '拍摄时间',
    component: 'DatePicker',
    colProps: { span: 6 },
    componentProps: {
      placeholder: '开始时间',
    },
  },
  {
    field: 'end_time',
    component: 'DatePicker',
    colProps: { span: 6 },
    componentProps: {
      placeholder: '结束时间',
    },
  },
];

export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },
  {
    field: 'name',
    label: '名称',
    component: 'Input',
    required: true,
  },
  {
    field: 'type',
    label: '识别类型',
    component: 'Input',
    required: true,
  },
  {
    field: 'EnglishName',
    label: '英文名',
    component: 'Input',
    required: true,
  },
  {
    field: 'recognition_number',
    label: '识别数量',
    component: 'Input',
    required: true,
  },
  {
    field: 'result',
    label: '识别结果',
    component: 'Input',
    required: true,
  },

  {
    field: 'degree',
    label: '置信度',
    component: 'Input',
    required: true,
  },
  {
    label: '识别时间',
    field: 'time',
    component: 'Input',
    required: true,
  },
  {
    label: '是否优秀',
    field: 'isExcellent',
    component: 'Input',
    required: true,
  },
  {
    label: '地点',
    field: 'place',
    component: 'Input',
    required: true,
  },
  {
    label: '设备',
    field: 'equipment',
    component: 'Input',
    required: true,
  },
  {
    label: '保护区',
    field: 'reserve',
    component: 'Input',
    required: true,
  },
  {
    label: '文件类型',
    field: 'fileType',
    component: 'Input',
    required: true,
  },

  {
    label: '图像',
    field: 'urls',
    required: false,
    component: 'Input',
    slot: 'urls',
  },
];
