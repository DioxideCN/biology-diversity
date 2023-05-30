import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Image } from 'ant-design-vue';
import { useGlobSetting } from '/@/hooks/setting';

const { apiUrl } = useGlobSetting();

export const columns: BasicColumn[] = [
  {
    title: '项目名称',
    dataIndex: 'name',
    width: 200,
  },
  {
    title: '项目编码',
    dataIndex: 'code',
    width: 180,
  },
  {
    title: '项目排序',
    dataIndex: 'sort',
    width: 100,
  },
  {
    title: '项目状态',
    dataIndex: 'status',
    width: 100,
  },
  {
    title: '创建时间',
    dataIndex: 'create_datetime',
    width: 180,
  },
  {
    title: '视频',
    dataIndex: 'url',
    width: 80,
    customRender: ({ record }) => {
      const url = record.url;
      console.log(apiUrl + url);
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
    label: '动物名称',
    required: true,
    component: 'Input',
  },
  {
    field: 'EnglishName',
    label: '动物学名',
    required: true,
    component: 'Input',
  },
  {
    field: 'status',
    component: 'DictSelect',
    label: '项目状态',
    componentProps: {
      dictCode: 'project_status',
    },
  },
  {
    field: 'type',
    label: '动物分类',
    component: 'Input',
    required: true,
  },
  {
    field: 'time',
    label: '拍摄日期',
    component: 'DatePicker',
    required: true,
  },
  {
    field: 'place',
    label: '拍摄地点',
    component: 'Input',
    required: true,
  },
  {
    field: 'equipment',
    label: '拍摄设备',
    component: 'Input',
    required: true,
  },
  {
    field: 'degree',
    label: '置信度',
    component: 'InputNumber',
    required: true,
  },
  {
    field: 'isExcellent',
    label: '标记优秀',
    component: 'Checkbox',
    required: false,
  },
  {
    label: '视频',
    field: 'urls',
    required: false,
    component: 'Input',
    slot: 'urls',
  },
];
