#! python3
import math
import pymysql
import sys
import subprocess
import re
import requests
import threading
from bs4 import BeautifulSoup as bs

#gloabal value
ips = []
iots = []

def getCveDescrip(cve): 
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
    """
    輸入ip對其進行nmap掃描

    return: dict object
    object structure
    {
        ip: str
        list of port: list
        device type: str
        os: str
        product: str
        vendor: str
        list of cve number: list
    }

    """

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
    
    item = {'ip': ip,
            'port': ports,
            'device_type': device,
            'os': os,
            'product': product,
            'vendor': vendor,
            'cve': cve_list
            }
    return item


def nmap_thread(first,end): 
    ip = ips[first:end]
    for i in range(len(ip)):
        iot = nmap_single(ip[i])
        for key,value in iot.items():
            print(key+":"+str(value))
        cve = iot["cve"]
        iots.append(iot)

if __name__ == "__main__":
    
    if(len(sys.argv) != 2):
        print("no table_id")
        exit()
    table_id = sys.argv[1]

    db = pymysql.connect(host="140.123.230.32",user="root",password="a407410040",db="iot",cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()

    sql = "select * from ip_" + table_id
    #sql = "select * from ip_" + table_id + " where ip like '140.123.30.%'"
    #sql = "select * from ip_" + table_id + " where ip = '140.123.102.245'"
    cursor.execute(sql)
    res = cursor.fetchall()

    ips = []
    for row in res:
        ips.append(row["ip"])
    print(ips)

    #debug for only one ip
    #nmap_thread(0,1)

    #定義線程
    
    t_list = []
    
    ip_first = int(len(ips)/10*0)
    ip_end = int(len(ips)/10*1)
    t1 = threading.Thread(target=nmap_thread,args=(ip_first,ip_end))
    t_list.append(t1)
    
    ip_first = int(len(ips)/10*1)
    ip_end = int(len(ips)/10*2)
    t2 = threading.Thread(target=nmap_thread,args=(ip_first,ip_end))
    t_list.append(t2)
    
    ip_first = int(len(ips)/10*2)
    ip_end = int(len(ips)/10*3)
    t3 = threading.Thread(target=nmap_thread,args=(ip_first,ip_end))
    t_list.append(t3)
    
    ip_first = int(len(ips)/10*3)
    ip_end = int(len(ips)/10*4)
    t4 = threading.Thread(target=nmap_thread,args=(ip_first,ip_end))
    t_list.append(t4)
    
    ip_first = int(len(ips)/10*4)
    ip_end = int(len(ips)/10*5)
    t5 = threading.Thread(target=nmap_thread,args=(ip_first,ip_end))
    t_list.append(t5)
    
    ip_first = int(len(ips)/10*5)
    ip_end = int(len(ips)/10*6)
    t6 = threading.Thread(target=nmap_thread,args=(ip_first,ip_end))
    t_list.append(t6)
    
    ip_first = int(len(ips)/10*6)
    ip_end = int(len(ips)/10*7)
    t7 = threading.Thread(target=nmap_thread,args=(ip_first,ip_end))
    t_list.append(t7)
    
    ip_first = int(len(ips)/10*7)
    ip_end = int(len(ips)/10*8)
    t8 = threading.Thread(target=nmap_thread,args=(ip_first,ip_end))
    t_list.append(t8)
    
    
    ip_first = int(len(ips)/10*8)
    ip_end = int(len(ips)/10*9)
    t9 = threading.Thread(target=nmap_thread,args=(ip_first,ip_end))
    t_list.append(t9)
    
    ip_first = int(len(ips)/10*9)
    ip_end = int(len(ips)/10*10)
    t10 = threading.Thread(target=nmap_thread,args=(ip_first,ip_end))
    t_list.append(t10)
    
    #開始工作
    for t in t_list:
        t.start()
    
    #等待所有thread結束
    for t in t_list:
        t.join() 
    
    cves = []
    cveInfos = []
    for i in range(len(iots)):
        for j in range(len(iots[i]["cve"])):
            cve = iots[i]["cve"][j]
            if cve not in cves:
                cveInfo = getCveDescrip(iots[i]["cve"][j])
                cves.append(cve)
                cveInfos.append(cveInfo)
                print(cveInfo)
            else:
                pos = cves.index(cve)
                cveInfo = cveInfos[pos]
            if(cveInfo == None):
                continue
            sql = "insert into cve_"+table_id+" (cve_ip,cve_id,description,cvss) values (%s,%s,%s,%s)"
            cursor.execute(sql,(iots[i]["ip"],cveInfo["cve"],cveInfo["description"],cveInfo["cvss"]))                  
    
    sql = "select * from cve_" + table_id
    cursor.execute(sql)

    db.commit()
    db.close()
    
