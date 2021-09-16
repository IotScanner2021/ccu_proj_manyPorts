import requests
from bs4 import BeautifulSoup


def SeekDescription(url):
    cvePage = requests.get(url)
    cveSoup = BeautifulSoup(cvePage.text , 'html.parser')
    ##get cve description
    cveDescription = str(cveSoup.find("div" , "cvedetailssummary")).replace('<div class="cvedetailssummary">' , "").strip()
    pos = cveDescription.index("<br/>")
    cveDescription = cveDescription[0 : pos]
    print("Description : ")
    print(str(cveDescription))
    
    cveScore = float(cveSoup.find("div" , "cvssbox").string)
    print("Score : " + str(cveScore))
'''
def SeekCVSS(url):
    cveScore = 0.0
    cvePage = requests.get(url)
    cveSoup = BeautifulSoup(cvePage.text , 'html.parser')
    cveScore = float(cveSoup.find("div" , "cvssbox").string)
    print("Score : " + str(cveScore))
    
    
    #cveElements = cveSoup.find_all("table")
    #for elem in cveElements:
    #    try:
    #        cveScore = float(elem.find("div" , "cvssbox").string)
    #    except:
    #        continue
    

def SeekSolution(url):
    cvePage = requests.get(url)
    cveSoup = BeautifulSoup(cvePage.text , 'html.parser')
    cveSolution = cveSoup.find_all("td" , "r_average")
    print("Reference : ")
    for elem in cveSolution:
        try:
            sol = elem.find("a")
            print(sol['href'])
        except:
            continue
'''
if __name__ == '__main__':
    arr = []
    url = 'https://www.cvedetails.com/cve'
    arr.append(url)
    #device = 'CVE-2017-12861'
    cve = input('Please input the CVE : ')
    arr.append(cve)
    url = '/'.join(arr)
    print(url)
    
    print("CVE : " + str(cve))
    SeekDescription(url)
