# IOT scanner

* software info
* client side
  * home page 
  * construct page
  * search page
  * insert page
* server side
  * information gathering
  * potential vulnerabilities collection
  * vulnerabilities validation

## software info
### Server
OS : Ubuntu 20.04.2 LTS

### Web
Python : 3.8.10

Nginx : nginx/1.18.0

Mysql :  MySQL Ver 8.0.26

Php : PHP 7.4.3

## client slide
### construct page
Construct a database which could let your devices safely.

The database contains IOT device info(device type 、device model、open port...)、potential vulnerability.

## server side
### information gathering
searching engines
1. Shodan
2. Censys

devicetypes
1. nas
2. router
3. printer
4. camera

determine devicetype methods
1. keywordMethod (recommended,fast more)
2. featureMethod

### potential vulnerabilities collection
engines
1. Nmap

### vulnerabilities validation
engine
1. Metasploit


