import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Image } from 'ant-design-vue';
import { useGlobSetting } from '/@/hooks/setting';

const { apiUrl } = useGlobSetting();

export const columns: BasicColumn[] = [
  {
    title: '项目名称',
    dataIndex: 'name',
    width: 200,
  },
  {
    title: '项目编码',
    dataIndex: 'code',
    width: 180,
  },
  {
    title: '项目排序',
    dataIndex: 'sort',
    width: 100,
  },
  {
    title: '项目状态',
    dataIndex: 'status',
    width: 100,
  },
  {
    title: '创建时间',
    dataIndex: 'create_datetime',
    width: 180,
  },
  {
    title: '视频',
    dataIndex: 'url',
    width: 80,
    customRender: ({ record }) => {
      const url = record.url;
      // console.log(apiUrl + url);
      return h(Image, { src: apiUrl + url, width: 40 });
    },
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'reserve',
    label: '保护区名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'name',
    label: '物种名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'time',
    label: '拍摄时间',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'fileType',
    label: '文件类型',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'equipment',
    label: '设备类型',
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
    required: true,
    component: 'Input',
  },
  {
    field: 'EnglishName',
    label: '动物学名',
    required: true,
    component: 'Input',
  },
  {
    field: 'time',
    label: '拍摄时间',
    required: true,
    component: 'DatePicker',
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
    label: '视频',
    field: 'urls',
    required: false,
    component: 'Input',
    slot: 'urls',
  },
];
