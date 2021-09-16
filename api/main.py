import sys
import find_cve
from shod import shodan_engine
from cens import censys_engine
from zoom import zoomeye_engine
from parser import process_parser

if __name__ == "__main__":
    
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
    api = dict()
    '''
    api['id'] = "0cc7a541-dd23-471c-a70b-0d15d94c06ec"
    api['secret'] = "dOppOon0bBs6W1lvp4D9YlhrXI55iRtc"
    '''
    api = dict()
    api['id'] = "aabc85e8-b6b9-4692-921a-ed81d1b0a8fc"
    api['secret'] = "66QsgUIAnBviFrFSPt8jMWd99aWbwtiQ"
    api['ip'] = ip
    api['count'] = count
    
    c = censys_engine(api)
    c.start()
    
    '''
    find cvee
    '''
    find_cve.findCveStart()
    
    '''
    summary info:devicetype,deviceModel,cvee,cvee description,cvss
    '''
    find_cve.summary()
