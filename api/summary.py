import os
import json
import pymysql
'''
steps
1. devicetype processing, store ip、devicetype、os、port
2. devicemodel processing, store cvee、description、cvss
3. summary above two info,ip、devicetype、os、port、cvee、description、cvss
'''

#ipFisrst,no devicemodel...
ips = []
ipFirst = {
    "ip" : [],
    "deviceType" : [],
    "os" : [],
    "port" : []
}

#devicemodel...
deviceIp = []
deviceInfo = []

#summary ip info + devicemodel
ipInfos = []
ipInfo = {
    "ip" : None,
    "deviceType" : None,
    "os" : None,
    "deviceModel" : None,
    "cvee" : [],
    "description" : [],
    "cvss" : []
}

#summary each engine info
def eng(eng_name,deviceType):
    filename = "/var/www/html/ccu_proj_manyPorts/api/log/" + eng_name + "_log/" + deviceType + ".log"
    if os.path.exists(filename) == False:
        return
    f = open(filename,"r")
    line_num = 0
    for line in f.readlines():
        line = line.strip()
        if line_num % 3 == 0:
            ip = line.split(':')[1]
        elif line_num % 3 == 1:
            o_sys = line.split(':')[1]
        elif line_num % 3 == 2:
            ps = []
            p_line = line.split(':')[1]
            port_serv = p_line.split(' ')
            for i in range(len(port_serv)):
                p = port_serv[i].split('/')[0]
                ps.append(p)
            
            if ip not in ips:
                ips.append(ip)
                ipFirst["ip"].append(ip)
                ipFirst["deviceType"].append(deviceType)
                ipFirst["os"].append(o_sys)
                ipFirst["port"].append(ps)
                '''
                device[deviceType].append(ip)
                op_sys[deviceType].append(o_sys)
                port[deviceType].append(ps)
                '''

        line_num += 1

    f.close()
    
def deviceTypeProcessing():
   
    eng("shod","router")
    eng("shod","printer")
    eng("shod","camera")
    eng("shod","nas")
    eng("cens","router")
    eng("cens","printer")
    eng("cens","nas")
    eng("cens","camera")
    eng("zoom","router")
    eng("zoom","printer")
    eng("zoom","camera")
    eng("zoom","nas")

'''deviceModel variable stores devicemodel,cvee,description,cvss'''

def deviceModelProcessing():
    # address cve
    filename = "/var/www/html/ccu_proj_manyPorts/api/log/cveInfo.log"
    fcve = open(filename,"r")
    deviceModel = {
        "ip" : None,
        "deviceModel" : None,
        "cvee" : [],
        "description" : [],
        "cvss" : []
    }
    for line in fcve.readlines():
        if "*ip:" in line:
            deviceModel["ip"] = line.split(':')[1]
            deviceIp.append(deviceModel["ip"])
            deviceModel["deviceModel"] = line.split(':')[2]
            infoNum = line.split(':')[3].replace('\n','')
            infoNum = int(infoNum)
            infoCur = 1
            loop = 0
        else:
            if infoCur == 1:
                deviceModel['cvee'].append(line.replace('\n',''))
                infoCur += 1
            elif infoCur == 2:
                deviceModel['description'].append(line.replace('\n',''))
                infoCur += 1
            elif infoCur == 3:
                deviceModel['cvss'].append(line.replace('\n',''))
                infoCur = 1
                loop += 1
                if loop == infoNum:
                    deviceInfo.append(deviceModel.copy())
                    #clean value
                    deviceModel.clear()
                    deviceModel["ip"] = None
                    deviceModel["deviceModel"] = None
                    deviceModel["cvee"] = []
                    deviceModel["description"] = []
                    deviceModel["cvss"] = []
    #print(deviceInfo)

'''
ipInfo stores full info containing ip,deviceType,deviceModel,cvee,description,cvss
'''
def putIpInfo():
    
    for ip in ips:
        ipInfo = {
            "ip" : None,
            "deviceType" : None,
            "os" : None,
            "deviceModel" : None,
            "cvee" : [],
            "description" : [],
            "cvss" : []
        }
        # ipfirst    
        fIndex = ipFirst["ip"].index(ip)
        ipInfo["ip"] = ipFirst["ip"][fIndex]
        ipInfo["deviceType"] = ipFirst["deviceType"][fIndex]
        ipInfo["os"] = ipFirst["os"][fIndex]
        ipInfo["port"] = ipFirst["port"][fIndex]
        if ip in deviceIp:
            findIndex = deviceIp.index(ip)
            ipInfo["deviceModel"] = deviceInfo[findIndex]["deviceModel"]
            ipInfo["cvee"] = deviceInfo[findIndex]["cvee"]
            ipInfo["description"] = deviceInfo[findIndex]["description"]
            ipInfo["cvss"] = deviceInfo[findIndex]["cvss"]
        else:
            ipInfo["deviceModel"] = None
            ipInfo["cvee"] = []
        ##copy(because the value of ipInfo change, ipInfos change sequentially)
        ipInfos.append(ipInfo.copy())
    #print(ipInfos)

def db_output():
    db = pymysql.connect(host="140.123.230.32",user="root",password="a407410040",db="iot",cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    
    #create table ip、port、cve
    f = open("table.txt","r") 
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
    
    f = open("/var/www/html/ccu_proj_manyPorts/www/cur_table.txt","w")
    next_id = int(table_id)
    f.write(str(next_id))
    f.close()

    #insert value
    for i in range(len(ipInfos)):
        #ip table
        ip = ipInfos[i]["ip"]
        os = ipInfos[i]["os"]
        devicetype = ipInfos[i]["deviceType"]
        devicemodel = str(ipInfos[i]["deviceModel"])
        
        sql = "insert into ip_" + table_id +" (ip,os,product_model,device_type) values (%s,%s,%s,%s)"
        cursor.execute(sql,(ip,os,devicemodel,devicetype))
        
        #cvee table
        if ipInfos[i]["deviceModel"] != None:
            for j in range(len(ipInfos[i]["cvee"])):
                cveeid = ipInfos[i]["cvee"][j]
                description = ipInfos[i]["description"][j]
                cvss = float(ipInfos[i]["cvss"][j])
                sql = "insert into cve_" + table_id + " (cve_ip,cve_id,description,cvss) values (%s,%s,%s,%s)"
                cursor.execute(sql,(ip,cveeid,description,cvss))
        
        #port table
        for j in range(len(ipInfos[i]["port"])):
            port = ipInfos[i]["port"][j]
            sql = "insert into port_" + table_id + " (port_ip,port) values (%s,%s)"
            cursor.execute(sql,(ip,port))
        
    db.commit()
    db.close()

def db_select(cursor,sql):
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        print(row)


def summaryStart():

    deviceTypeProcessing()
    deviceModelProcessing()
    debug_print()
    putIpInfo()
    db_output();
   

def debug_print():
    
    #ipfirst
    print(ipFirst)
    
    #de
    print(deviceInfo)

'''
    #ipinfo debug 
    for i in range(len(ipInfos)):
        print("ip:"+ipInfos[i]["ip"]) 
        print("device type:"+ipInfos[i]["deviceType"])
        print("os:"+ipInfos[i]["os"])
        print("port:"+str(ipInfos[i]["port"]))
        if ipInfos[i]["deviceModel"] != None:
            print("device model:"+str(ipInfos[i]["deviceModel"]))
            for j in range(len(ipInfos[i]["cvee"])):
                print("cvee:"+ipInfos[i]["cvee"][j])
                print("description:"+ipInfos[i]["description"][j])
                print("cvss:"+ipInfos[i]["cvss"][j])
''' 

if __name__ == "__main__":
    summaryStart()
