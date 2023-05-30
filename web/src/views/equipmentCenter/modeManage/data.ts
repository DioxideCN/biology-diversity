import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';

export const columns: BasicColumn[] = [
  {
    title: '模板编号',
    dataIndex: 'id',
    width: 180,
  },
  {
    title: '模板名称',
    dataIndex: 'name',
    width: 180,
  },
  {
    title: '模板状态',
    dataIndex: 'status',
    width: 100,
  },
  {
    title: '添加日期',
    dataIndex: 'create_time',
    width: 100,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: '项目名称',
    component: 'Input',
    colProps: { span: 6 },
  },
];

export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: '设备编号',
    component: 'Input',
    show: false,
  },
  {
    field: 'name',
    label: '设备名称',
    component: 'Input',
  },
  {
    field: 'model',
    label: '设备型号',
    required: false,
    component: 'Input',
  },
  {
    field: 'equipment_id',
    label: '设备编号',
    component: 'Input',
    required: false,
  },
  {
    field: 'type',
    label: '设备类型',
    required: false,
    component: 'Select',
    componentProps: {
      options: [{ label: 'A型设备', value: 'A型设备' }],
    },
  },
  {
    field: 'input_voltage',
    component: 'Input',
    label: '输入电压',
    required: false,
  },
  {
    field: 'fps',
    label: '拍照帧率（每秒）',
    component: 'Input',
    required: false,
    labelWidth: 150,
  },
  {
    field: 'pixel',
    label: '系统总像素',
    component: 'Input',
    required: false,
  },
  {
    field: 'resolution',
    label: '微镜头分辨率',
    component: 'Input',
    required: false,
  },
  {
    field: 'size',
    label: '外观尺寸',
    component: 'Input',
    required: false,
  },
  {
    field: 'weight',
    label: '重量',
    component: 'Input',
    required: false,
  },
  {
    field: 'power_supply',
    label: '电源功率',
    component: 'Input',
    required: false,
  },
  {
    field: 'is_waterproof',
    label: '是否防水',
    component: 'Select',
    required: false,
    componentProps: {
      options: [
        { label: '是', value: true },
        { label: '否', value: false },
      ],
    },
  },
  {
    field: 'waterproof_grade',
    label: '防水等级',
    component: 'Input',
    required: false,
  },
  {
    field: 'is_dustproof',
    label: '是否防尘',
    component: 'Select',
    required: false,
    componentProps: {
      options: [
        { label: '是', value: true },
        { label: '否', value: false },
      ],
    },
  },
  {
    field: 'dustproof_grade',
    label: '防尘等级',
    component: 'Input',
    required: false,
  },
  {
    field: 'notes',
    label: '备注',
    component: 'InputTextArea',
    required: false,
    span: 24,
  },
];
