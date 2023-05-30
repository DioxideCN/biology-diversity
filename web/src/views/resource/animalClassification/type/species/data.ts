import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';


export const columns: BasicColumn[] = [
  
  {
    title: '动物分类编号',
    dataIndex: 'code',
    width: 200,
  },
  {
    title: '动物分类名称',
    dataIndex: 'name',
    width: 200,
  },
  {
    title: '分类级别',
    dataIndex: 'type',
    width: 200,
  },
  
  
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: '动物分类名称',
    component: 'Input',
    colProps: { span: 12},
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
    field: 'type',
    component: 'Input',
    label: '分类级别',
    defaultValue: '种',
    dynamicDisabled: ({ values }) => {
      return !!values.type;
    },
  },
  {
    field: 'animal_id',
    label: '动物分类编号',
    component: 'Input',
    required: true,
  },
  {
    field: 'name',
    label: '分类名称',
    component: 'Input',
    required: true,
  },
  {
    field: 'notes',
    label: '备注',
    component: 'InputTextArea',
  },
  
];
