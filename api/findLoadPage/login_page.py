import requests
import warnings

def login_page(ip):
    warnings.filterwarnings("ignore")
    try:
        r = requests.get(ip , verify = False , timeout = 3)
        if r.status_code == requests.codes.ok:
            if 'username'.casefold() in r.text and 'password'.casefold() in r.text:
                return "Login page exist"
            return "No login page"
        else:
            return "status code : " + r.status_code
    except:
        return "request time out"

if __name__ == "__main__":
    print(login_page('https://140.123.121.161'))


