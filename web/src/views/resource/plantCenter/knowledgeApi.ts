import { defHttp } from '/@/utils/http/axios';

enum DeptApi {
  prefix = '/api/biology/botany_knowledge',
}

export const KgetList = (params) => {
  return defHttp.get({ url: DeptApi.prefix ,params});
};

/**
 * 保存或更新
 */

export const createOrUpdate = (params, isUpdate) => {
  // console.log(params)
  // console.log(params.url[0])
  // params.url = params.urls[0]
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

 