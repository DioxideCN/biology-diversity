import { defHttp } from '/@/utils/http/axios';

enum DeptApi {
  prefix = '/api/biology/animal',
  //识别接口 prefix1
  prefix1 = '/api/biology/recognition/realtime',
  prefix2 = '/api/biology/equipment',
  prefix3 = '/api/biology/area_manage',
  // prefix1 = '/api/biology/recognition/realtime',
}

export const getList1 = (params) => {
  return defHttp.get({
    url: DeptApi.prefix + '/' + params.id,
    params,
    responseType: 'json',
  });
};
export const getList3 = (params) => {
  return defHttp.get({ url: DeptApi.prefix2, params });
};
export const getList4 = (params) => {
  return defHttp.get({ url: DeptApi.prefix3, params });
};

export const getList2 = (params) => {
  return defHttp.get({
    url: DeptApi.prefix2 + '/' + params.id,
    params,
    responseType: 'json',
  });
};
export const getList5 = (params) => {
  return defHttp.get({ url: DeptApi.prefix, params });
};

export const getList = (params) => {
  return defHttp.get({ url: DeptApi.prefix1, params, responseType: 'json' });
};

// export const create1 = (params) => {
//   return defHttp.post({ url: DeptApi.prefix1, params });
// };

export const deleteD = (id) => {
  return defHttp.delete({ url: DeptApi.prefix + '/' + id });
};

// export const update = (params) => {
//   return defHttp.put({ url: DeptApi.prefix, params });
// };
/**
 * 保存或更新
 */

export const updateErrorTrue = (params, id) => {
  params.isFalse = true;
  return defHttp.put({ url: DeptApi.prefix1 + '/' + id, params });
};
export const updateErrorFalse = (params, id) => {
  params.isFalse = false;
  return defHttp.put({ url: DeptApi.prefix1 + '/' + id, params });
};

export const updateLike = (params, id) => {
  return defHttp.put({ url: DeptApi.prefix1 + '/' + id, params });
};

export const createOrUpdate = (params, isUpdate) => {
  // console.log(params)
  // console.log(params.url[0])
  params.url = params.urls[0];
  if (isUpdate) {
    return defHttp.put({ url: DeptApi.prefix1 + '/' + params.id, params });
  } else {
    return defHttp.post({ url: DeptApi.prefix1, params });
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
