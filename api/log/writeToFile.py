import os
'''
steps
1. summary devicetype
2. list each ip info:deficetype,cvee,cvee descip,cvss

'''

device = {
    "router" : [],
    "printer" : [],
    "camera" : []
    }

def eng(eng_name,device_name):
    filename = "/var/www/html/ccu_proj/api/log/" + eng_name + "_log/" + device_name + ".log"
    if os.path.exists(filename) == False:
        return
    f = open(filename,"r")
    for line in f.readlines():
        ip = line.split(':')[0]
        if ip not in device[device_name]:
            device[device_name].append(ip)
    f.close()

'''
output
devicetype,cvee,cvee descrip,cvss
'''
def output(device_name):
    filename = "/var/www/html/ccu_proj/api/log/output.txt"
    f = open(filename,"a")
    for ip in device[device_name]:
        content = ip + "\n" 
        f.write(content)
        print(content)
        content = "device type:" + device_name + "\n"
        f.write(content)
        print(content)
        content = "------------------------------\ncvee:\ncvee description:\ncvss:\n\n"
        f.write(content)
        print(content)
        

def list_devicetype():
   
    eng("shod","router")
    eng("shod","printer")
    eng("shod","camera")
    eng("cens","router")
    eng("cens","printer")
    eng("cens","camera")
    eng("zoom","router")
    eng("zoom","printer")
    eng("zoom","camera")

if __name__ == "__main__":
    list_devicetype()
    output("router")
    output("printer")
    output("camera")
