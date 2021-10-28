import sys
import find_cve
from shod import shodan_engine
from cens import censys_engine
from zoom import zoomeye_engine
from parser import process_parser

'''
construct()

功能:
建立某區域資料庫

init
1. ip:建立區域
2. count:掃描數量限制

steps
1. 偵查引擎 
2. 弱點搜尋
3. 建立資料庫

note
1. 現只使用censys_engine

'''

def construct():
    ## args prepare
    args = process_parser()
    ip = args.ip
    count = args.count
    
    #run all ports
    if count == -1:
        count = 1000
    
    '''     
    api_key = "839CrW4f3Omc9wYO9aMWeRq0Go4rEPfN"
    s = shodan_engine(api_key,ip,count)  
    s.start()


    api_key = "7557767C-20cf-fd7d5-d848-d7a5904e8f1" 
    z = zoomeye_engine(api_key,ip,count)
    z.start()
    '''
    '''
    1. 偵查引擎 
    '''
    api = dict()
    api['id'] = "aabc85e8-b6b9-4692-921a-ed81d1b0a8fc"
    api['secret'] = "66QsgUIAnBviFrFSPt8jMWd99aWbwtiQ"
    api['ip'] = ip
    api['count'] = count
    
    c = censys_engine(api)
    c.start()
    
    '''
    2. 弱點搜尋
    '''
    find_cve.findCveStart()
    
    '''
    3. 建立資料庫
    '''
    find_cve.summary()

if __name__ == "__main__":
   
    construct()
