import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
export const columns: BasicColumn[] = [
  {
    title: '点位编号',
    dataIndex: 'id',
    width: 200,
  },
  {
    title: '点位名称',
    dataIndex: 'name',
    width: 140,
  },
  {
    title: '所属区域名称',
    dataIndex: 'area',
    width: 220,
  }, 
  {
    title: '点位经度',
    dataIndex: 'longitude',
    width: 100,
  },
  {
    title: '点位纬度',
    dataIndex: 'latitude',
    width: 100,
  },
  {
    title: '点位详细地址',
    dataIndex: 'address',
    width: 180,
  },
  // {
  //   title: '点位负责人',
  //   dataIndex:'manager',
  //   width: 100
  // },
  // {
  //   title: '点位投放时间',
  //   dataIndex:'time',
  //   width: 100,
  //   customRender: ({ record }) => {
  //     const res = record.time;
  //     const text = res.replace('T',' ')
  //     return h( () => text);
  //   },
  // }

];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: '点位名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'id',
    label: '点位编号',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'area',
    label: '所属区域',
    component: 'Input',
    colProps: { span: 6 },
  },
];

export const formSchema: FormSchema[] = [
  {
    field: 'time',
    label: '投放点位时间',
    component: 'Input',
    show: false,
  },
  {
    field: 'longitude',
    label: '点位经度',
    required: true,
    component: 'Input',
  },
  {
    field: 'latitude',
    label: '点位纬度',
    required: true,
    component: 'Input',
  },
  {
    field: 'manager',
    label: '负责人',
    component: 'Input',
    required: true,
  },
  {
    field: 'manager_phone',
    label: '点位负责人联系方式',
    component: 'Input',
    required: true,
    labelWidth:150,
  },
  {
    field: 'introduction',
    label: '点位简介',
    component: 'InputTextArea',
    required: true,
  },
  {
    field: 'address',
    label: '点位详细地址',
    component: 'InputTextArea',
    required: true,
  },
  {
    field: 'notes',
    label: '点位备注',
    component: 'InputTextArea',
    required: true,
  },
];