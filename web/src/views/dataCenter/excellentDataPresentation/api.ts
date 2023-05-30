import { defHttp } from '/@/utils/http/axios';

enum DeptApi {
  prefix = '/api/biology/recognition/realtime',
  prefix2 = '/api/biology/equipment',
  prefix3 = '/api/biology/area_manage',
  prefix4 = '/api/biology/animal',
}

export const getList = (params) => {
  params.isExcellent = true;
  return defHttp.get({ url: DeptApi.prefix, params, responseType: 'json' });
};
export const getList3 = (params) => {
  return defHttp.get({ url: DeptApi.prefix2, params });
};
export const getList4 = (params) => {
  return defHttp.get({ url: DeptApi.prefix3, params });
};
export const getList5 = (params) => {
  return defHttp.get({ url: DeptApi.prefix4, params });
};

export const deleteD = (id) => {
  return defHttp.delete({ url: DeptApi.prefix + '/' + id });
};

export const update = (params) => {
  return defHttp.put({ url: DeptApi.prefix, params });
};
/**
 * 保存或更新
 */

export const updateLike = (params, id) => {
  return defHttp.put({ url: DeptApi.prefix + '/' + id, params });
};

export const createOrUpdate = (params, isUpdate) => {
  // console.log(params)
  // console.log(params.url[0])
  params.url = params.urls[0];
  if (isUpdate) {
    return defHttp.put({ url: DeptApi.prefix + '/' + params.id, params });
  } else {
    return defHttp.post({ url: DeptApi.prefix, params });
  }
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
