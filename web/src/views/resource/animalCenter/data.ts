import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Image } from 'ant-design-vue';
// import moment from 'moment';
const baseUrl = import.meta.env.VITE_GLOB_API_URL

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
    customRender: ({ record }) => {
        const create_datetime = record.create_datetime
        return moment(create_datetime).format("YYYY-MM-DD HH:mm:ss")
    }

  },
  {
   title: '图像',
   dataIndex: 'url',
   width: 80,
   customRender: ({ record }) => {
     const url = record.url;
     // console.log(baseUrl + url)
     return h(Image, { src:  'http://localhost:8000' + url, width: 40 });
   },
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
    field: 'EnglishName',
    label: '英文名称',
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
    required: true,
  },
 {
   label: '栖息环境',
   field: 'habitat',
   component: 'InputTextArea',
   required: true,
 },
 {
   label: '生活习性',
   field: 'live',
   component: 'InputTextArea',
   required: true,
 },
 {
   label: '繁殖方式',
   field: 'reproduction',
   component: 'InputTextArea',
   required: true,
 },
 {
    label: '地域分布',
    field: 'distribution',
    component: 'InputTextArea',
    required: true,
  },
 {
   label: '图像(必填)',
   field: 'urls',
   required: false,
   component: 'Input',
   slot: 'urls',
 },
];
