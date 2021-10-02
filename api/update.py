import sys
import find_cve
import pymysql
import threading
import subprocess
import os
import re
import requests
from bs4 import BeautifulSoup as bs
from shod import shodan_engine
from cens import censys_engine
from zoom import zoomeye_engine
from parser import process_parser

nmap_infos = []
cveInfos = []

def getCvesDescrip(cve): 
    url = "https://www.cvedetails.com/cve/" + cve
    print(url)
    cvePage = requests.get(url)
    cveSoup = bs(cvePage.text , 'html.parser')
    ##get cve description
    #no this cve info
    if cveSoup.find('div','errormsg') != None:
        print("page not found")
        return None
    cveDescription = str(cveSoup.find("div" , "cvedetailssummary")).replace('<div class="cvedetailssummary">' , "").strip()
    pos = cveDescription.index("<br/>")
    cveDescription = cveDescription[0 : pos]
    print("Description : ")
    print(str(cveDescription))

    cveScore = float(cveSoup.find("div" , "cvssbox").string)
    print("Score : " + str(cveScore)) 
    
    cveInfo = {"cve":cve,"description":cveDescription,"cvss":cveScore}
    return cveInfo

def nmap_single(ip):
    #print(ip)
    out = subprocess.check_output(["nmap","-A","--script=vulners.nse",ip])
    out = out.decode().split('\n')

    port_pattern = re.compile(r'\d*/')
    device_pattern = re.compile(r'Device:(.*);')
    os_pattern = re.compile(r'OS:(.*);')
    cpe_pattern = re.compile(r'CPE:(.*)')
    cve_pattern = re.compile(r'CVE-\d*-\d*')

    ports = []
    cve_list = []
    device = ''
    os = ''
    vendor = ''
    product = ''

    for line in out:
        res = re.match(port_pattern, line)
        if(res != None):
            # print('port    ', line)
            ports.append(res.group()[:-1])
            continue

        res = re.search(cve_pattern, line)
        if(res != None):
            # print('cve    ', line)
            cve_list.append(res.group())
            continue
        
        res = re.search(device_pattern, line)
        if(res != None):
            # print('device   ', line)
            res = res.group()
            device = re.search(r':(.*);',res).group()
            device = device.lstrip(': ').rstrip(';')
            # print(device)

        res = re.search(os_pattern, line)
        if(res != None):
            # print('os   ', line)
            res = res.group()
            os = re.search(r':(.*);',res).group()
            os = os.lstrip(': ').rstrip(';')
            # print(os)

        res = re.search(cpe_pattern, line)
        if(res != None):
            # print('cpe   ', line)
            res = res.group()
            cpe = re.search(r':(.*)',res).group()
            cpe = cpe.lstrip(': ').rstrip(';')
            # print(cpe)
            
            info = cpe.split(':')
            vendor = info[2]
            product = info[3]
            # print(vendor, product)
    
    nmap_info = {'ip': ip,
            'port': ports,
            'device_type': device,
            'os': os,
            'product': product,
            'vendor': vendor,
            'cve': cve_list
            }
    return nmap_info


def nmap_thread(ips,first,end):
    ip = ips[first:end]
    for i in range(len(ip)):
        nmap_info = nmap_single(ip[i])
        for key,value in nmap_info.items():
            print(key+":"+str(value))
        cve = nmap_info["cve"]
        nmap_infos.append(nmap_info)

def nmap_threads(ips):
    t_list = []
    
    ip_first = int(len(ips)/10*0)
    ip_end = int(len(ips)/10*1)
    t1 = threading.Thread(target=nmap_thread,args=(ips,ip_first,ip_end))
    t_list.append(t1)
    
    ip_first = int(len(ips)/10*1)
    ip_end = int(len(ips)/10*2)
    t2 = threading.Thread(target=nmap_thread,args=(ips,ip_first,ip_end))
    t_list.append(t2)
    
    ip_first = int(len(ips)/10*2)
    ip_end = int(len(ips)/10*3)
    t3 = threading.Thread(target=nmap_thread,args=(ips,ip_first,ip_end))
    ip_first = int(len(ips)/10*3)
    t_list.append(t3)
     
    ip_first = int(len(ips)/10*3)
    ip_end = int(len(ips)/10*4)
    t4 = threading.Thread(target=nmap_thread,args=(ips,ip_first,ip_end))
    t_list.append(t4)
    
    ip_first = int(len(ips)/10*4)
    ip_end = int(len(ips)/10*5)
    t5 = threading.Thread(target=nmap_thread,args=(ips,ip_first,ip_end))
    t_list.append(t5)
    
    ip_first = int(len(ips)/10*5)
    ip_end = int(len(ips)/10*6)
    t6 = threading.Thread(target=nmap_thread,args=(ips,ip_first,ip_end))
    t_list.append(t6)
    
    ip_first = int(len(ips)/10*6)
    ip_end = int(len(ips)/10*7)
    t7 = threading.Thread(target=nmap_thread,args=(ips,ip_first,ip_end))
    t_list.append(t7)
    
    ip_first = int(len(ips)/10*7)
    ip_end = int(len(ips)/10*8)
    t8 = threading.Thread(target=nmap_thread,args=(ips,ip_first,ip_end))
    t_list.append(t8)
    
    
    ip_first = int(len(ips)/10*8)
    ip_end = int(len(ips)/10*9)
    t9 = threading.Thread(target=nmap_thread,args=(ips,ip_first,ip_end))
    t_list.append(t9)
    
    ip_first = int(len(ips)/10*9)
    ip_end = int(len(ips)/10*10)
    t10 = threading.Thread(target=nmap_thread,args=(ips,ip_first,ip_end))
    t_list.append(t10)
    
    #開始工作
    for t in t_list:
        t.start()
    
    #等待所有thread結束
    for t in t_list:
        t.join() 

def nmap_interface(ips):
    if len(ips) >= 10:
        nmap_threads(ips)
    else:
        nmap_thread(ips,0,len(ips))

def update_db(table_id):
    db = pymysql.connect(host="140.123.230.32",user="root",password="a407410040",db="iot",cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    
    cve_record_ip = []
    cve_record_info = []
    for info in nmap_infos:
        print(info)
        #update ip table's os,devicetype,product_model field
        os = info["os"] if info["os"]!=None else "none"
        product = info["product"] if info["product"]!=None else "none"
        sql = "update ip_" + table_id + " set os='" + os + "',product_model='" + product + "' where ip='" + info["ip"] + "'"
        cursor.execute(sql)
        
        #update port table's port field
        sql = "delete from port_" + table_id + " where port_ip='" + info["ip"] + "'"
        cursor.execute(sql)

        for port in info["port"]:    
            sql = "insert into port_" + table_id + "(port_ip,port) values ('" + info["ip"] + "','" + port + "')"
            cursor.execute(sql)

        #update cve table's cve_id cvss description field
        sql = "delete from cve_" + table_id + " where cve_ip='" + info["ip"] + "'"
        cursor.execute(sql)

        for cve in info["cve"]:
            if cve not in cve_record_ip:
                cveInfo = getCvesDescrip(cve)
                cve_record_ip.append(cve)
                cve_record_info.append(cveInfo)
            else:
                pos = cve_record_ip.index(cve)
                cveInfo = cve_record_info[pos]
            
            if cveInfo == None:
                continue
            cvss = cveInfo["cvss"]
            description = cveInfo["description"].replace('\'','"')
            sql = "insert into cve_" + table_id + "(cve_ip,cve_id,cvss,description) values ('" + info["ip"] + "','" + cve + "','" + str(cvss) + "','" + description + "')"
            cursor.execute(sql)

    db.commit()
    db.close()
    

def update_known_ip(table_id):
    db = pymysql.connect(host="140.123.230.32",user="root",password="a407410040",db="iot",cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    
    #get ip from db
    sql = "select * from ip_" + table_id
    cursor.execute(sql)
    res = cursor.fetchall()
    ips = []
    for row in res:
        ips.append(row["ip"])
    db.close()
    
    #nmap search
    nmap_interface(ips)

    '''
    #test
    nmap_info = {
        'ip':'140.112.20.147',
        'device_type':'nas',
        'os':'test',
        'product':'test',
        'vendor':'test',
        'port':['50','60'],
        'cve':['CVE-2017-17562']
    }
    nmap_infos.append(nmap_info)
    ''' 
    #update db
    update_db(table_id)

if __name__ == "__main__":

    args = process_parser()
    table_id = args.table_id
    
    if table_id == '1':
        print("table_id 1 permission denied")
        exit()
    
    
    
    ip = args.ip
    count = args.count
    api = dict()
    api['id'] = "aabc85e8-b6b9-4692-921a-ed81d1b0a8fc"
    api['secret'] = "66QsgUIAnBviFrFSPt8jMWd99aWbwtiQ"
    api['ip'] = ip
    api['count'] = count

    c = censys_engine(api)
    c.start()
    
    find_cve.findCveStart()

    find_cve.putipInfo()

    find_cve.update_table(table_id)

    '''
    known ip update
    '''
    update_known_ip(table_id)
