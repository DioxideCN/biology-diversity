import { defHttp } from '/@/utils/http/axios';

enum DeptApi {
  prefix = '/api/biology/equipment',
}

export const EgetList = (params) => {
  return defHttp.get({ url: DeptApi.prefix , params });
};
export const EgetUrlList = (params) => {
  // console.log("UrlList",params)
  return defHttp.get({ url: "/api/biology/history/" + params.point_id});
};
export const EgetById = (id) => {
  return defHttp.get({ url: DeptApi.prefix +`/${id}`});
};
export const EgetAllList = () => {
  return defHttp.get({ url: DeptApi.prefix+'/all/list'});
};
/**
 * 保存或更新
 */

export const EcreateOrUpdate = (params, isUpdate) => {
  // console.log(params)
  // console.log(params.url[0])
  // params.url = params.urls[0]
  if (isUpdate) {
    return defHttp.put({ url: DeptApi.prefix + '/' + params.id, params });
  } else {
    return defHttp.post({ url: DeptApi.prefix, params });
  }
};

export const EimportData = (params) => {
  return defHttp.post({ url: DeptApi.prefix + '/all/import', params });
};

export const EexportData = () => {
  return defHttp.get(
          { url: DeptApi.prefix + '/all/export', responseType: 'blob' },
          { isReturnNativeResponse: true },
  );
};

/**
 * 删除
 */

export const EdeleteItem = (id) => {
  return defHttp.delete({ url: DeptApi.prefix + '/' + id });
};

 