import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Image } from 'ant-design-vue';
import { useGlobSetting } from '/@/hooks/setting';

const { apiUrl } = useGlobSetting();

export const columns: BasicColumn[] = [
  {
    title: '识别批次编号',
    dataIndex: 'id',
    width: 200,
  },
  {
    title: '所含分割图数量',
    dataIndex: 'number',
    width: 180,
  },
  {
    title: '识别开始时间',
    dataIndex: 'start_time',
    width: 100,
  },
  {
    title: '识别结束时间',
    dataIndex: 'end_time',
    width: 100,
  },
  {
    title: '识别成功数',
    dataIndex: 'number',
    width: 180,
  },
  {
    title: '识别失败数',
    dataIndex: 'number',
    width: 180,
  },
  // {
  //   title: '视频',
  //   dataIndex: 'url',
  //   width: 80,
  //   customRender: ({ record }) => {
  //     const url = record.url;
  //     console.log(apiUrl + url);
  //     return h(Image, { src: apiUrl + url, width: 40 });
  //   },
  // },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'reserve',
    label: '',
    component: 'Input',
    colProps: { span: 4},
    componentProps:{
      placeholder:'识别批次编号',
    }
  },
  {
    field: 'name',
    label: '  ',
    component: 'Input',
    colProps: { span: 6 },
    componentProps:{
      placeholder:'开始识别时间',
    }
  },
  {
    field: 'time',
    label: '  ',
    component: 'Input',
    colProps: { span: 6 },
    componentProps:{
      placeholder:'结果识别时间',
    }
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
    field: 'number',
    label: '所含分割图数量',
    required: true,
    component: 'Input',
  },
 

];
