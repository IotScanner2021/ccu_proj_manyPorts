#! python3
import subprocess
import re

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
            #print('cve    ', line)
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


if __name__=='__main__':
    ip = input('searching ip: ')
    iot = nmap_single(ip)
    for key, value in iot.items():
        print(key+':', value)
