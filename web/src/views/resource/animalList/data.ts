import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Image } from 'ant-design-vue';
import { useGlobSetting } from '/@/hooks/setting';

const { apiUrl } = useGlobSetting();

export const columns: BasicColumn[] = [
  // {
  //   title: '动物编号',
  //   dataIndex: 'id',
  //   width: 60,
  //   align: 'left',
  // },
  // {
  //   title: '识别编号',
  //   dataIndex: 'recognition_id',
  //   width: 100,
  // },
  {
    title: '中文学名',
    dataIndex: 'cn',
    width: 100,
  },
  {
    title: '拉丁学名',
    dataIndex: 'ladin',
    width: 100,
  },
  {
    title: '别称',
    dataIndex: 'other_name',
    width: 100,
  },
  {
    title: '大类名称',
    dataIndex: 'big_class',
    width: 50,
  },
  {
    title: '小类名称',
    dataIndex: 'sub_class',
    width: 50,
  },
  // {
  //   title: '保护等级',
  //   dataIndex: 'protection_level',
  //   width: 100,
  // },
  {
    title: '知识库名称',
    dataIndex: 'k_name',
    width: 100,
  },
  {
    title: '知识库编号',
    dataIndex: 'k_id',
    width: 100,
  },
  {
    title: '是否重点保护',
    dataIndex: 'is_protected',
    width: 100,
    customRender: ({ record }) => {
      const is_protected = record.is_protected;
      const text = is_protected ? '是' : '否';
      return h( () => text);
    },
  },
  // {
  //   title: '图像',
  //   dataIndex: 'url',
  //   width: 80,
  //   customRender: ({ record }) => {
  //     const url = record.url;
  //     // console.log(apiUrl + url);
  //     return h(Image, { src: apiUrl + url, width: 40 });
  //   },
  // },
];
export const columns2: BasicColumn[] = [
  {
    title: '知识库编号',
    dataIndex: 'id',
    width: 180,
    align: 'left',
  },
  {
    title: '动物名称',
    dataIndex: 'name',
    width: 180,
    align: 'left',
  },
];
export const searchFormSchema2: FormSchema[] = [
  {
    field: 'id',
    label: '知识库编号',
    component: 'Input',
    colProps: { span: 8 },
    labelWidth: 80,
  },
  {
    field: 'name',
    label: '动物名称',
    component: 'Input',
    colProps: { span: 8 },
    labelWidth: 80,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'id',
    label: '动物编号',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'recognition_id',
    label: '识别编号',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'cn',
    label: '中文学名',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'ladin',
    label: '拉丁学名',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'other_name',
    label: '动物别称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'big_class',
    label: '大类名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'sub_class',
    label: '小类名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'kname',
    label: '知识库名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'kid',
    label: '知识库编号',
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
    label: '动物学名',
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
    required: false,
    component: 'Input',
    slot: 'urls',
  },
];
