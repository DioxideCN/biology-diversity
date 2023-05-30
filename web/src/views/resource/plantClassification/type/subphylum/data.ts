import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';


export const columns: BasicColumn[] = [
  
  {
    title: '植物分类编号',
    dataIndex: 'id',
    width: 100,
  },
  {
    title: '植物分类名称',
    dataIndex: 'name',
    width: 100,
  },
  {
    title: '分类级别',
    dataIndex: 'type',
    width: 100,
  },
  
  
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: '分类名称',
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
    defaultValue: '亚门',
    dynamicDisabled: ({ values }) => {
      return !!values.type;
    },
  },
  // {
  //   field: 'animal_id',
  //   label: '植物分类编号',
  //   component: 'Input',
  //   // required: true,
  // },
  {
    field: 'name',
    label: '植物分类名称',
    component: 'Input',
    required: true,
  },
  {
    field: 'notes',
    label: '备注',
    component: 'InputTextArea',
  },
  
];
