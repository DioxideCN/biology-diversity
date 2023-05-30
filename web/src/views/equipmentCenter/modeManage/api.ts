import { defHttp } from '/@/utils/http/axios';

enum DeptApi {
  prefix = '/api/biology/template',
  prefix1 = '/api/biology/equipment',
}

export const getList = (params) => {
  return defHttp.get({ url: DeptApi.prefix, params });
};

// 视频接口
export const getList1 = (params) => {
  return defHttp.get({ url: DeptApi.prefix1, params });
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
export const Able = (params) => {
  return defHttp.put({ url: DeptApi.prefix + '/' + params.id, params });
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
