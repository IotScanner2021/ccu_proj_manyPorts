import shodan

def writeToFile(content):
    filename = "shod.log"
    f = open(filename , "a+")
    f.write(content)
    f.close()

def seek_device(word , device):
    if device in word:
        return True
    else:
        return False

if __name__ == "__main__" :
    api = shodan.Shodan('4otp2vSs8LGyzBf1YYiVuMmaoln9GFjA')
    ip = api.search_cursor(query = 'net:140.123.0.0/16')
    limit = 62509
    count = 0
    for info in api.search_cursor(query = 'net:140.123.0.0/16'):
        word = str(info)
        
        flag_p = seek_device(word , "printer")
        if flag_p == True:
            writeToFile("ip:" + str(info["ip_str"]) + '\n')
            writeToFile("os:" + str(info["os"]) + '\n')
            writeToFile("ports:" + str(info["port"]) + '\n')
            writeToFile("device_type:printer\n")
        flag_r = seek_device(word , "router")
        if flag_r == True:
            writeToFile("ip:" + str(info["ip_str"]) + '\n')
            writeToFile("os:" + str(info["os"]) + '\n')
            writeToFile("ports:" + str(info["port"]) + '\n')
            writeToFile("device_type:router\n")

        flag_w = seek_device(word , "camera")
        if flag_w == True:
            writeToFile("ip:" + str(info["ip_str"]) + '\n')
            writeToFile("os:" + str(info["os"]) + '\n')
            writeToFile("ports:" + str(info["port"]) + '\n')
            writeToFile("device_type:camera\n")
        
        flag_n = seek_device(word , "nas")
        if flag_n == True:
            writeToFile("ip:" + str(info["ip_str"]) + '\n')
            writeToFile("os:" + str(info["os"]) + '\n')
            writeToFile("ports:" + str(info["port"]) + '\n')
            writeToFile("device_type:nas\n")
        
        count = count + 1
        if count >= limit:
            break
        
    print(count)
