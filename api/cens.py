from censys.search import *
#from censys.base import *
from parser import process_parser
import os
import sys
    
class censys_engine():
    def __init__(self,api_info):
        self.id = api_info['id']
        self.secret = api_info['secret']
        self.ip = api_info['ip']
        self.count = api_info['count']
        #fields:output
        self.fields = ["ip", "metadata.description", "metadata.device_type", "metadata.os", "protocols"]
    
    def start(self):
        print("-----------------------")
        print("Start Censys Process!!!")
        try:
            print(self.id,self.secret)
            api = CensysIPv4(self.id,self.secret)
            self.keywordMethod(api)
            #self.featureMethod(api)
        except Exception as e:
            #print("Error:censys api could not start")
            print(sys.exc_info())
            exit(0)


    def format(self,page):
        ip = page.get("ip","None")
        os = page.get("metadata.os","None")
        protocols = page.get("protocols","None")
        protocols = ", ".join([str(p.encode('UTF-8'), errors='ignore') for p in protocols])
        print("ip:" + ip, end = '\t')
        print("\n")

    def writeToFile(self,content):
        filename = "/var/www/html/ccu_proj_manyPorts/api/log/cens.log"
        f = open(filename,"a+")
        f.write(content)
        f.close()

    '''
    through device get each ip and devicemodel if it has
    '''
    def keywordMethod(self,api):
        self.findDevice(api,"printer")
        self.findDevice(api,'router')
        self.findDevice(api,'camera')
        self.findDevice(api,'nas')
        
    def findDevice(self,api,keyword):
        query = self.ip + ' and '+ keyword

        page_count = 0
        for page in api.search(query,self.fields):
            ##find ip
            ip = page.get("ip","None")
            content = "ip:" + ip + "\n"
            self.writeToFile(content)
            filename = "/var/www/html/ccu_proj_manyPorts/api/log/cens_ip.log"
            f = open(filename,"a+")
            f.write(content)
            f.close()
            print("ip:"+ip)
            page_count+=1
            
            ##find os
            os = page.get("metadata.os","None")
            if(os == None):
                os == "None"
            content = "os:" + os + "\n";
            self.writeToFile(content)
            print("os:"+os)
            
            ##find productModel
            productModel = page.get("metadata.description","None")
            if(productModel == None):
                productModel == "None"
            content = "product_model:" + productModel + "\n"
            self.writeToFile(content)
            print("product_model:"+productModel)

            ##output devicetype
            content = "device_type:" + keyword + "\n"
            self.writeToFile(content)
            
            ##find protocol
            protocols = page.get("protocols","None")
            self.writeToFile("ports:")
            for port in protocols:
                content = port+" ";
                self.writeToFile(content)
            print(protocols)
            self.writeToFile("\n")
    
        if page_count == 0 :
            print(self.ip+":not "+keyword)
    '''
    def featureMethod(self,api):
        print(self.ip)
        info = api.view(self.ip)
        self.print_device_type(info)
    
    def print_device_type(self,info):
        if 'metadata' in info.keys():
            if 'device_type' in info['metadata'].keys():
                if info['metadata']['device_type'] == 'printer':
                    print('device type: printer\n')
                elif info['metadata']['device_type'] == 'camera':
                    print('device type: camera\n')
                elif info['metadata']['device_type'] == 'soho router':
                    print('device type: soho router\n')
        else: 
            print('device type: None\n') 
    ''' 

if __name__ == "__main__":

    args = process_parser()

    api_info = dict()
    api_info['id'] = "558d0b15-07a5-47a4-b68f-b0530181f791"
    api_info['secret'] = "YwgekK1zvhvmn2rjRmQPFblsKNIMlFwC"
    api_info['ip'] = args.ip
    api_info['count'] = args.count

    c = censys_engine(api_info)
    c.start()
