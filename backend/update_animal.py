

#jdbc信息#
user = 'root'  # 获取user对应的值
password = 'P2p@58066815'  # 获取password对应的值
db_host = '172.16.30.188'  # 获取host对应的值
database = 'reservecang_dt'  # 获取dbname对应的值



import pymysql






if __name__ == '__main__':

    db = pymysql.connect(
        host=db_host,
        user=user,
        password=password,
        database=database,
        port=3306
    )  # 建立连接
    cursor = db.cursor()  # 游标
    Sql = """select * from am_animal_information;"""  # 执行的sql
    cursor.execute(Sql)  # 执行sql
    while True:  # 判断是否为真
        result = cursor.fetchone()  # 每次获取一条数据
        if not result:  # 判断是否还有数据，没有就break该循环
            break
        SKNOWLEDGE_ID =result[3] #界
        SCIRCLES = result[14] #界
        SDOOR = result[15] #门
        SSUBGATE = result[16] #亚门
        SOUTLINE = result[17] #纲
        SUBCLASS = result[18] #亚纲
        SORDER = result[19]  #目
        SSUBORDER = result[20] #亚目
        SSECTION = result[21] #科
        SSUBFAMILY = result[22] #亚科
        SSUBSPECIES = result[25] #亚种
        RACERACE = result[30] #族

        cursor1 = db.cursor()
        Sql = f"select scode from am_animal_knowledge where id='{SKNOWLEDGE_ID}' order by id limit 1;"  # 执行的sql
        cursor1.execute(Sql)  # 执行sql
        rest = cursor1.fetchall()
        for i in rest:
            sql = f"update am_animal_information_copy1 set SKNOWLEDGE_ID = '{i[0]}' where id ='{result[0]}';"
            print(sql)
            # cursor1.execute(sql)
            # print(i)

        # print(result)  # 打印数据

    db.close()  # 关闭连接

    # 中间有很多的逻辑处理，假设最后结果还是ori#
    # to_dws(ori, 'test2')
