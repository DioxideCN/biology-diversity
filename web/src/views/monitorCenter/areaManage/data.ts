import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';

export const columns: BasicColumn[] = [
  {
    title: '区域编号',
    dataIndex: 'id',
    width: 180,
  },
  {
    title: '区域名称',
    dataIndex: 'name',
    width: 180,
  },
  {
    title: '区域地址',
    dataIndex: 'address',
    width: 100,
  },
  {
    title: '区域负责人',
    dataIndex: 'manager',
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
    label: 'id',
    component: 'Input',
    show: false,
  },
  {
    field: 'name',
    label: '项目名称',
    required: true,
    component: 'Input',
  },
  {
    field: 'code',
    label: '项目编码',
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
    field: 'sort',
    label: '岗位排序',
    component: 'InputNumber',
    required: true,
  },
];