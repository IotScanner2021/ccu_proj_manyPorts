f = open("cens_ip.log","r")
ips = []
for line in f.readlines():
    ip = line.split(':')[1].replace('\n','')
    if ip in ips:
        continue
    ips.append(ip)
print(len(ips))

for line in f.readlines():
    ip = line.split(':')[1].replace('\n','')
    ips.append(ip)
print(len(ips))
