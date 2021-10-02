#! python3
import pymysql
import sys
import os
import threading
import subprocess
import re
import requests
from bs4 import BeautifulSoup as bs

'''
find cve steps
1. nmap_thread() : find cve by nmap
2. getCveDescrip() : find cveDescrip、cvss by corresponding cve

summary steps
1. putipInfo() : summary each api info
2. summary() : create a small db & write to the db(table_id:used to determine the db number)
'''

cveInfos = []

iots = []
ips = []
ip_db = []
ipInfo = {
    "ip" : None,
    "device_type" : None,
    "os" : None,
    "device_model" : None,
    "port" : [],    
    "cve" : [],
    "description" : [],
    "cvss" : []
}
ip_infos = []

def findCveStart():
    filename = "/var/www/html/ccu_proj_manyPorts/api/log/cens_ip.log"
    if os.path.exists(filename) == False :
        print("no ip in these ips")
        exit()

    f = open(filename,"r")
    
    for line in f.readlines():
        ip = line.split(':')[1].replace('\n','')
        ips.append(ip)
    
    for i in range(len(ips)):
        iot = {
            "cve" : []
        }
        iot["cve"] = ["cve_1","cve_2"]

        #get cve description & cvss
        cveInfo = {
            "cve" : [],
            "description" : [],
            "cvss" : []
        }
        cveInfo["description"] = ["none","none"]
        cveInfo["cvss"] = [5.0,5.0]
        cveInfo["cve"] = iot["cve"]
        cveInfos.append(cveInfo)
            
def putipInfo():
    filename = "/var/www/html/ccu_proj_manyPorts/api/log/cens.log"
    f = open(filename,"r")
    cur = 0
    cve_cur = 0
    for line in f.readlines():
        cur += 1
        if cur%5 == 1:
            ipInfo["ip"] = line.split(':')[1].replace('\n','')
        elif cur%5 == 2:
            ipInfo["os"] = line.split(':')[1].replace('\n','')
        elif cur%5 == 3:
            ipInfo["device_model"] = line.split(':')[1].replace('\n','')
        elif cur%5 == 4:
            ipInfo["device_type"] = line.split(':')[1].replace('\n','')
        elif cur%5 == 0:
            txt = line.split(':')[1].replace('\n','')
            txt = txt.split(' ')
            ports = []
            for i in range(len(txt)-1):
                port = txt[i].split('/')[0] 
                ports.append(port)
            ipInfo["port"] = ports

            ipInfo["cve"] = cveInfos[cve_cur]["cve"]
            ipInfo["description"] = cveInfos[cve_cur]["description"]
            ipInfo["cvss"] = cveInfos[cve_cur]["cvss"]
            cve_cur += 1
            ip_infos.append(ipInfo.copy())

def db_output():
    db = pymysql.connect(host="140.123.230.32",user="root",password="a407410040",db="iot",cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    
    #create table ip、port、cve
    f = open("/var/www/html/ccu_proj_manyPorts/api/table.txt","r") 
    lines = f.readlines()
    table_id = lines[0]

    sql = "create table ip_" + table_id + "(\
        ip char(20),\
        os char(50),\
        session text,\
        site char(20),\
        product_model char(50),\
        device_type char(50),\
        primary key (ip)\
    )"
    cursor.execute(sql)

    sql = "create table port_" + table_id + "(\
        port_ip char(20),\
        port int,\
        foreign key (port_ip) references ip_" + table_id + "(ip) on delete cascade on update cascade\
    )"
    
    cursor.execute(sql)
    sql = "create table cve_" + table_id + "(\
        cve_ip char(20),\
        cve_id char(50),\
        cvss float,\
        description text,\
        foreign key (cve_ip) references ip_" + table_id + "(ip) on delete cascade on update cascade\
    )"
    cursor.execute(sql)
    f.close()

    f = open("/var/www/html/ccu_proj_manyPorts/api/table.txt","w")
    next_id = int(table_id) + 1
    f.write(str(next_id))
    f.close()

    f = open("/var/www/html/ccu_proj_manyPorts/www/table.txt","w")
    next_id = int(table_id)
    f.write(str(next_id))
    f.close()
    
    #insert value
    for i in range(len(ip_infos)):
        #ip table
        if ip_infos[i]["ip"] in ip_db:
            continue
        ip_db.append(ip_infos[i]["ip"])
        ip = ip_infos[i]["ip"]
        os = ip_infos[i]["os"]
        devicetype = ip_infos[i]["device_type"]
        devicemodel = str(ip_infos[i]["device_model"])
        
        sql = "insert into ip_" + table_id +" (ip,os,product_model,device_type) values (%s,%s,%s,%s)"
        cursor.execute(sql,(ip,os,devicemodel,devicetype))
        
        #cve table
        for j in range(len(ip_infos[i]["cve"])):
            cveeid = ip_infos[i]["cve"][j]
            description = ip_infos[i]["description"][j]
            cvss = float(ip_infos[i]["cvss"][j])
            sql = "insert into cve_" + table_id + " (cve_ip,cve_id,description,cvss) values (%s,%s,%s,%s)"
            cursor.execute(sql,(ip,cveeid,description,cvss))
        
        #port table
        for j in range(len(ip_infos[i]["port"])):
            port = ip_infos[i]["port"][j]
            sql = "insert into port_" + table_id + " (port_ip,port) values (%s,%s)"
            cursor.execute(sql,(ip,port))
         

    sql = "select * from ip_" + table_id
    cursor.execute(sql)
    print(cursor.fetchall())
    
    db.commit()
    db.close()

def update_table(table_id):
    db = pymysql.connect(host="140.123.230.32",user="root",password="a407410040",db="iot",cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
  
    #drop table
    sql = "drop table port_"+table_id
    cursor.execute(sql)
    
    sql = "drop table cve_"+table_id
    cursor.execute(sql)
   
    sql = "drop table ip_"+table_id
    cursor.execute(sql)

    #create table
    sql = "create table ip_" + table_id + "(\
        ip char(20),\
        os char(50),\
        session text,\
        site char(20),\
        product_model char(50),\
        device_type char(50),\
        primary key (ip)\
    )"
    cursor.execute(sql)

    sql = "create table port_" + table_id + "(\
        port_ip char(20),\
        port int,\
        foreign key (port_ip) references ip_" + table_id + "(ip) on delete cascade on update cascade\
    )"
    
    cursor.execute(sql)
    sql = "create table cve_" + table_id + "(\
        cve_ip char(20),\
        cve_id char(50),\
        cvss float,\
        description text,\
        foreign key (cve_ip) references ip_" + table_id + "(ip) on delete cascade on update cascade\
    )"
    cursor.execute(sql)

    #insert value
    for i in range(len(ip_infos)):
        #ip table
        if ip_infos[i]["ip"] in ip_db:
            continue
        ip_db.append(ip_infos[i]["ip"])
        ip = ip_infos[i]["ip"]
        os = ip_infos[i]["os"]
        devicetype = ip_infos[i]["device_type"]
        devicemodel = str(ip_infos[i]["device_model"])
        
        sql = "insert into ip_" + table_id +" (ip,os,product_model,device_type) values (%s,%s,%s,%s)"
        cursor.execute(sql,(ip,os,devicemodel,devicetype))
        
        #cve table
        for j in range(len(ip_infos[i]["cve"])):
            cveeid = ip_infos[i]["cve"][j]
            description = ip_infos[i]["description"][j]
            cvss = float(ip_infos[i]["cvss"][j])
            sql = "insert into cve_" + table_id + " (cve_ip,cve_id,description,cvss) values (%s,%s,%s,%s)"
            cursor.execute(sql,(ip,cveeid,description,cvss))
        
        #port table
        for j in range(len(ip_infos[i]["port"])):
            port = ip_infos[i]["port"][j]
            sql = "insert into port_" + table_id + " (port_ip,port) values (%s,%s)"
            cursor.execute(sql,(ip,port))
         

    sql = "select * from ip_" + table_id
    cursor.execute(sql)
    print(cursor.fetchall())
    
    db.commit()
    db.close()

def summary():
    putipInfo()
    db_output()

if __name__ == "__main__":
    findCveStart()
    summary()
