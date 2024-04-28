from ipaddress import *
#14948
count = 0
net = ip_network('192.168.32.128/255.255.255.192', 0)
for ip in net:
    if bin(int(ip))[2:].count('1') % 2 == 0:
        count += 1
print(count)

#14650 сделал вручную.