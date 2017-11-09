# -*- coding: utf-8 -*-
import pymysql.cursors

# address, port, user, password
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='test',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        print('attention to the " ` " and " \' "')
    #     sql = "INSERT INTO `user` (`email`, `password`, `nick_name`, `user_name`) VALUES (%s, %s, %s, %s)"
    #     cursor.execute(sql, ('328838842@qq.com', 'very-secret', 'axiang', 'xiaoxiang'))
    # connection.commit()
    # // connection is not autocommit by default. So you must commit it to save. without the 'with' block

    with connection.cursor() as cursor:
        print('work!')
    #     sql = "SELECT `id`,`user_name` FROM `user` WHERE `password`=%s"
    #     cursor.execute(sql, ('cc',))
    #     result = cursor.fetchone()
    #     print(result)
finally:
    connection.close()
