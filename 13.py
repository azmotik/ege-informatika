from ipaddress import *

'''for mask in range(32, 0, -1):
    net1 = ip_network(f'216.54.187.235/{mask}', 0)
    net2 = ip_network(f'216.54.174.128/{mask}', 0)
    if net1[0] != net2[0] and ip_address('216.54.174.128') != net2[0] and ip_address('216.54.174.128') != net2[-1] and ip_address('216.54.187.235') != net1[0] and ip_address('216.54.187.235') != net1[-1]:
        print(mask)

max_a = 1

for a in range(1, 255):
    net = ip_network(f'116.242.{a}.26/255.255.255.224', 0)
    flag = 1
    for ip in net:
        if bin(int(ip))[:-16].count('1') < bin(int(ip))[-16:].count('1'):
            flag = 0

    if flag == 1:
        max_a = max(max_a, a)

print(max_a)

min_a = 255

for a in range(1, 255):
    net = ip_network(f'183.192.{a}.0/255.255.252.0', 0)
    flag = 1
    for ip in net:
        if bin(int(ip))[-16:].count('1') <= 3:
            flag = 0

    if flag == 1:
        min_a = min(min_a, a)

print(min_a)

#неправильно
count = 0
for a in range(1, 255):
    net = ip_network(f'246.81.65.{a}/255.255.255.224', 0)
    flag = 1
    for ip in net:
        if bin(int(ip))[-16:-8].count('0') <= bin(int(ip))[-8:].count('0'):
            flag = 0

    if flag == 1:
        count += 1

print(count)

count = 0

net = ip_network(f'112.154.132.0/255.255.252.0', 0)
flag = 1
for ip in net:
    if bin(int(ip))[-16:].count('1') % 2 != 0 and bin(int(ip))[:-16].count('1') <= bin(int(ip))[-16:].count('0'):
        count += 1

print(count)

#неправильно
count = 0
for a in range(1, 255):
    net = ip_network(f'207.0.{a}.167/255.255.255.192', 0)
    flag = 1
    for ip in net:
        if bin(int(ip))[:-16].count('0') <= bin(int(ip))[-16:].count('0'):
            flag = 0

    if flag == 1:
        count += 1

print(count)

max_ip = 0

net = ip_network(f'192.168.31.80/255.255.255.240', 0)
for ip in net:
    max_ip = max(bin(int(ip)).count('1'), max_ip)

print(max_ip)

count = 0

net = ip_network(f'192.168.32.160/255.255.255.240', 0)
for ip in net:
    if bin(int(ip))[2:].count('0') > 21:
        count += 1

print(count)

count = 0

net = ip_network(f'192.168.240.0/255.255.255.0', 0)
for ip in net:
    if bin(int(ip))[2:].count('0') == bin(int(ip))[2:].count('1'):
        count += 1

print(count)

count = 0

net = ip_network(f'112.208.0.0/255.255.128.0', 0)
for ip in net:
    if bin(int(ip))[2:].count('1') % 11 == 0:
        count += 1

print(count)'''

count = 0

net = ip_network(f'192.168.32.160/255.255.255.240', 0)
for ip in net:
    if bin(int(ip))[2:].count('1') % 2 == 0:
        count += 1

print(count)
