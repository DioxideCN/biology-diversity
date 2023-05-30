import { defHttp } from '/@/utils/http/axios';

enum DeptApi {
  prefix = '/api/biology/data',
  prefix2 = '/api/biology/title',
  prefix3 = '/api/biology/equipment',

}

export const DgetList = () => {
  return defHttp.get({ url: DeptApi.prefix });
};

export const getTitle = () => {
  return defHttp.get({ url: DeptApi.prefix2 });
};

export const getVideo = () => {
  return defHttp.get({ url: DeptApi.prefix3 });
};

//动物总量
export const DgetNumber = (data) => {
  return defHttp.get({ url: DeptApi.prefix + '/number', params: data });
};

//每月识别总量
export const DgetTrend = () => {
  return defHttp.get({ url: DeptApi.prefix + '/trend' });
};

//重点动物
export const DgetImportant = () => {
  return defHttp.get({ url: DeptApi.prefix + '/important' });
};
//高清图片
export const GetImages = (data) => {
  return defHttp.get({ url: DeptApi.prefix + '/image', params: data });
};
//视频直播
export const GetStream = (data) => {
  return defHttp.get({ url: DeptApi.prefix + '/video', params: data });
};
//总量统计
export const GetChart = (data) => {
  return defHttp.get({ url: DeptApi.prefix + '/trend', params: data });
};
/**
 * 保存或更新
 */

export const createOrUpdate = (params, isUpdate) => {
  if (isUpdate) {
    return defHttp.put({ url: DeptApi.prefix + '/' + params.id, params });
  } else {
    return defHttp.post({ url: DeptApi.prefix, params });
  }
};

export const updateTitle = (params) => {

    return defHttp.put({ url: DeptApi.prefix2  , params });

};

export const importData = (params) => {
  return defHttp.post({ url: DeptApi.prefix + '/all/import', params });
};

export const exportData = () => {
  return defHttp.get(
          { url: DeptApi.prefix + '/all/export', responseType: 'blob' },
          { isReturnNativeResponse: true },
  );
};

/**
 * 删除
 */

export const deleteItem = (id) => {
  return defHttp.delete({ url: DeptApi.prefix + '/' + id });
};