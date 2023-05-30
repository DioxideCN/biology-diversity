import { BasicColumn } from '/@/components/Table';
 import { FormSchema } from '/@/components/Table';
 import { useGlobSetting } from '/@/hooks/setting';
 
 const { apiUrl } = useGlobSetting();
 
 
 export const columns: BasicColumn[] = [
   
  
   {
     title: '识别类型',
     dataIndex: 'type',
     width: 100,
   },
   {
     title: '识别数量',
     dataIndex: 'recognition_number',
     width: 100,
   },
   {
     title: '识别结果',
     dataIndex: 'result',
     width: 100,
   },
   {
     title: '置信度',
     dataIndex: 'degree',
     width: 100,
   },
   {
     title: '识别时间',
     dataIndex: 'time',
     width: 180,
   },
   {
     title: '是否优秀',
     dataIndex: 'isExcellent',
     width: 180,
   },
   {
     title: '英文名',
     dataIndex: 'EnglishName',
     width: 180,
   },
   {
     title: '地点',
     dataIndex: 'place',
     width: 180,
   },
   {
     title: '设备',
     dataIndex: 'equipment',
     width: 180,
   },
   {
     title: '保护区',
     dataIndex: 'reserve',
     width: 180,
   },
   {
     title: '文件类型',
     dataIndex: 'fileType',
     width: 180,
   },
   {
     title: '图像',
     dataIndex: 'url',
     width: 80,
     customRender: ({ record }) => {
       const url = record.url;
       console.log(apiUrl + url)
       return h(Image, { src:  apiUrl + url, width: 40 });
     },
   },
 ];
 
 export const searchFormSchema: FormSchema[] = [
   {
     field: 'program',
     label: '保护区名称 ',
     component: 'Input',
     colProps: { span: 6 },
   },
   {
    field: 'order',
    label: '物种名称  ',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'family',
    label: '拍摄时间',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'family',
    label: '文件类型 ',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'family',
    label: '设备类型 ',
    component: 'Input',
    colProps: { span: 6 },
  },
 ];
 
 export const formSchema: FormSchema[] = [
   
   {
     field: 'name',
     label: '名称',
     component: 'Input',
     required: true,
   },
   {
     field: 'type',
     label: '识别类型',
     component: 'Input',
     required: true,
   },
   {
     field: 'EnglishName',
     label: '英文名',
     component: 'Input',
     required: true,
   },
   {
     field: 'recognition_number',
     label: '识别数量',
     component: 'Input',
     required: true,
   },
   {
     field: 'result',
     label: '识别结果',
     component: 'Input',
     required: true,
   },
 
   {
     field: 'degree',
     label: '置信度',
     component: 'Input',
     required: true,
   },
   {
     label: '识别时间',
     field: 'time',
     component: 'Input',
     required: true,
   },
   {
    label: '是否优秀',
    field: 'isExcellent',
   component: 'Select',
   required: true,
  },
  {
    label: '地点',
    field: 'place',
    component: 'Input',
    required: true,
  },
  {
    label: '设备',
    field: 'equipment',
    component: 'Input',
    required: true,
  },
  {
    label: '保护区',
    field: 'reserve',
    component: 'Input',
    required: true,
  },
  {
    label: '文件类型',
    field: 'fileType',
    component: 'Input',
    required: true,
    
  },
 
 {
    label: '图像',
    field: 'urls',
    required: false,
    component: 'Input',
    slot: 'urls',
  },
 ];
