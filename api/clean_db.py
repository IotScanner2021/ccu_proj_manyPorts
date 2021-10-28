import pymysql
import sys

'''
for debug
快速刪除某些資料庫
'''

if __name__ == "__main__":
    
    db = pymysql.connect(host="140.123.230.32",user="root",password="a407410040",db="iot",cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()

    if len(sys.argv)!=2:
        print("argv len is less")
        exit()
    table_id = str(sys.argv[1])
    
    if table_id == '1':
        print('you don\'t have permisssion about table 1')
        exit()
    
    sql = "drop table port_" + table_id
    cursor.execute(sql)

    sql = "drop table cve_" + table_id
    cursor.execute(sql)
    
    sql = "drop table ip_" + table_id
    cursor.execute(sql)
    
