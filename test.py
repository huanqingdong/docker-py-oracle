#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cx_Oracle


class UserInfo:
    # 构造方法
    def __init__(self, name, age, birthday):
        """
        :type name: 姓名
        :type age: 年龄
        :type birthday: 出生年月日
        """
        self.name = name
        self.age = age
        self.birthday = birthday

    # 重写toString方法
    def __str__(self):
        return '{ name:%s,age:%s,birthday:%s }' % (self.name, self.age, self.birthday)


def get_user_list():
    conn = cx_Oracle.connect("scott/tiger@//192.168.1.132:1521/xe", encoding='utf-8')
    cur = conn.cursor()
    cur.execute("select name,age,to_char(birthday,'yyyy-mm-dd') from user_info")  # 执行sql语句

    rs = cur.fetchall()  # 一次返回所有结果集
    user_list = []
    if len(rs) > 0:
        for r in rs:
            name = r[0]
            age = r[1]
            birthday = r[2]
            user_list.append(UserInfo(name, age, birthday))

    # 关闭cursor()
    cur.close()
    # 关闭数据库连接
    conn.close()
    return user_list


if __name__ == '__main__':
    userList = get_user_list()
    for userInfo in userList:
        print("用户信息:%s" % str(userInfo))
