import json



def update_one_animations(animial_list_one_fps,cname,svrCode):
    for index_one,animial_one in enumerate(animial_list_one_fps):
        if animial_one["cname"] == cname:
            num = animial_one['num'] + 1
            animial_list_one_fps[index_one] = {"cname":cname,"svrCode":animial_one["svrCode"] ,"num":num}
            return animial_list_one_fps
    animial_list_one_fps.append({'cname':cname,"svrCode":svrCode ,'num':1})
    return animial_list_one_fps

def update_all_animations(animial_list_one_fps,animial_list):
    for animal_on in animial_list_one_fps:
        update = False
        for index, animial in enumerate(animial_list):
            if animial['cname'] == animal_on['cname']:
                if animal_on["num"] > animial["num"]:
                    animial_list[index] = {"cname": animial['cname'], "svrCode": animial["svrCode"],
                                           "num": animal_on['num']}
                    update = True
                    break
                update = True
        if not update:
            animial_list.append(animal_on)
    return animial_list


def get_best_result(result_test):
    best_result = {"cname": "", "prob":"", "svrCode":""}
    animial_list = []
    for fps in result_test:
        for i, result_list in fps.items():
            animial_list_one_fps = []
            for result in result_list:
                cname = result['cname']
                prob = float(result['prob'])
                svrCode = result['svrCode']
                if not bool(best_result):
                    best_result["cname"] = cname
                    best_result["prob"] = float(prob)*100
                    best_result["svrCode"] = svrCode
                else:
                    prob_tmp = float(best_result["prob"]) if best_result["prob"] else 0.0
                    if prob_tmp < prob:
                        best_result["cname"] = cname
                        best_result["prob"] = float(prob)*100
                        best_result["svrCode"] = svrCode
                animial_list_one_fps = update_one_animations(animial_list_one_fps, cname,svrCode)

        animial_list = update_all_animations(animial_list_one_fps, animial_list)
    return best_result,animial_list