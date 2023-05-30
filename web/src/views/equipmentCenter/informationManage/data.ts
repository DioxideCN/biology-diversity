import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';

export const columns: BasicColumn[] = [
  {
    title: '设备名称',
    dataIndex: 'name',
    width: 100,
    align: 'left',
  },
  {
    title: '所属组别',
    dataIndex: 'group',
    width: 100,
  },
  {
    title: '是否有权限查看',
    dataIndex: 'range',
    width: 100,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: '设备名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'type',
    label: '型号',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'group',
    label: '所属组别',
    component: 'Input',
    colProps: { span: 6 },
  },
];

export const formSchema: FormSchema[] = [
  {
    field: 'name',
    label: '设备名称',
    component: 'Input',
    required: true,
  },
  {
    field: 'type',
    label: '型号',
    component: 'Input',
    required: true,
  },
  {
    field: 'group',
    label: '所属组别',
    component: 'Input',
    required: true,
  },
  {
    field: 'range',
    label: '是否有查看权限',
    component: 'Input',
    required: true,
  },
];
