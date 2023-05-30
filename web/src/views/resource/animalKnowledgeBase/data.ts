import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Image } from 'ant-design-vue';
import { useGlobSetting } from '/@/hooks/setting';

const { apiUrl } = useGlobSetting();

export const columns: BasicColumn[] = [
  {
    title: '知识库编号',
    dataIndex: 'code',
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

export const searchFormSchema: FormSchema[] = [
  {
    field: 'id',
    label: '知识库编号',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'name',
    label: '动物名称',
    component: 'Input',
    colProps: { span: 6 },
  },
];

export const formSchema: FormSchema[] = [
  // {
  //   field: 'id',
  //   label: 'id',
  //   component: 'Input',
  //   show: false,
  // },
  {
    field: 'name',
    label: '动物名称',
    component: 'Input',
    required: true,
  },
  {
    field: 'program',
    label: '纲',
    component: 'InputTextArea',
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
  }
];
