from ipaddress import *
'''count = 0
arr = ip_network('23.140.159.160/255.255.252.0', 0)
for ip in arr:
    if bin(int(ip))[:-16].count('1') >= bin(int(ip))[-16:].count('1'):
        count +=1 
print(count)

count = 0
arr = ip_network('253.112.169.12/255.255.254.0', 0)
for ip in arr:
    if bin(int(ip))[:-16].count('1') <= bin(int(ip))[-16:].count('1'):
        count +=1 
print(count)

count = 0
arr = ip_network('252.67.33.87/255.252.0.0', 0)
for ip in arr:
    if bin(int(ip))[:-16].count('1') * 2 < bin(int(ip))[-16:].count('1'):
        count +=1 
print(count)

count = 0
arr = ip_network('249.0.33.87/255.252.0.0', 0)
for ip in arr:
    if bin(int(ip))[:-16].count('1') * 2 < bin(int(ip))[-16:].count('1'):
        count +=1 
print(count)

for mask in range(0, 33):
    net = ip_network(f'44.44.229.28/{mask}', 0)
    if net[0] == ip_address('44.44.224.0'):
        print(mask)

for mask in range(0, 33):
    net = ip_network(f'244.55.229.28/{mask}', 0)
    if net[0] == ip_address('244.0.0.0'):
        print(32 - mask)

for mask in range(0, 33):
    net = ip_network(f'244.55.138.100/{mask}', 0)
    if net[0] == ip_address('244.55.138.96'):
        print(net.netmask)

for mask in range(0, 33):
    net = ip_network(f'244.55.138.100/{mask}', 0)
    if net[0] == ip_address('240.0.0.0'):
        print(net.netmask)

for mask in range(0, 33):
    net = ip_network(f'42.118.219.133/{mask}', 0)
    if net[0] == ip_address('42.118.216.0'):
        print(bin(int(net.netmask)).count('1'))'''

for mask in range(0, 33):
    net = ip_network(f'98.188.115.211/{mask}', 0)
    if net[0] == ip_address('98.188.115.192'):
        print(bin(int(net.netmask)).count('1')) 