import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';

export const columns: BasicColumn[] = [
  {
    title: '序号',
    dataIndex: 'id',
    width: 60,
    align: 'left',
  },
  {
    title: '动物名称',
    dataIndex: 'name',
    width: 100,
  },
  {
    title: '纲',
    dataIndex: 'program',
    width: 100,
  },
  {
    title: '目',
    dataIndex: 'order',
    width: 100,
  },
  {
    title: '科',
    dataIndex: 'family',
    width: 100,
  },
  {
    title: '创建时间',
    dataIndex: 'create_datetime',
    width: 180,
  },
];
export const settingList = [
  {
    key: '1',
    name: '界',
    component: 'kingdom',
  },
  {
    key: '2',
    name: '门',
    component: 'phylum',
  },
  {
    key: '3',
    name: '亚门',
    component: 'subphylum',
  },
  {
    key: '4',
    name: '纲',
    component: 'classes',
  },
  {
    key: '5',
    name: '亚纲',
    component: 'subclass',
  },
  {
    key: '6',
    name: '目',
    component: 'order',
  },
  {
    key: '7',
    name: '亚目',
    component: 'suborder',
  },
  {
    key: '8',
    name: '科',
    component: 'family',
  },
  {
    key: '9',
    name: '亚科',
    component: 'subfamily',
  },
  {
    key: '10',
    name: '种',
    component: 'suborder',
  },
  {
    key: '11',
    name: '亚种',
    component: 'subspecies',
  },

  {
    key: '12',
    name: '族',
    component: 'tribe',
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'program',
    label: '纲',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
   field: 'order',
   label: '目',
   component: 'Input',
   colProps: { span: 6 },
 },
 {
   field: 'family',
   label: '科',
   component: 'Input',
   colProps: { span: 6 },
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
    component: 'Input',
    required: true,
  },
  {
    field: 'program',
    label: '纲',
    component: 'Input',
    required: true,
  },
  {
    field: 'order',
    label: '目',
    component: 'Input',
    required: true,
  },

  {
    field: 'family',
    label: '科',
    component: 'Input',
    required: true,
  },
  {
    label: '形态特征',
    field: 'description',
    component: 'InputTextArea',
  },
  {
   label: '形态特征',
   field: 'description',
   component: 'InputTextArea',
 },
 {
   label: '栖息环境',
   field: 'habitat',
   component: 'InputTextArea',
 },
 {
   label: '生活习性',
   field: 'live',
   component: 'InputTextArea',
 },
 {
   label: '繁殖方式',
   field: 'reproduction',
   component: 'InputTextArea',
 },
 {
    label: '图像',
    field: 'urls',
    required: true,
    component: 'Input',
    slot: 'urls',
    
  },
];
