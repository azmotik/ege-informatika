from ipaddress import *
net = ip_network('123.222.0.192/255.255.255.224', 0)
count = 0
for ip in net:
    print(ip)
    if bin(int(ip))[2:].count('0') == bin(int(ip))[2:].count('1'):
        count += 1
print(count)