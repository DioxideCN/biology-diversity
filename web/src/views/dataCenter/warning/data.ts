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
    title: '预警类型',
    dataIndex: 'type',
    width: 100,
  },
  {
    title: '预警内容',
    dataIndex: 'message',
    width: 100,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'type',
    label: '预警类型',
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
    field: 'type',
    label: '预警类型',
    component: 'Input',
    required: true,
  },
  {
    field: 'message',
    label: '预警内容',
    component: 'Input',
    required: true,
  },
];
