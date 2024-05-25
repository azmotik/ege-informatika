from ipaddress import *
'''#var1
for mask in range(33):
    net = ip_network(f'185.49.83.72/{mask}', 0)
    print(net, net.netmask)

#var2
for mask in range(33):
    net = ip_network(f'185.49.34.122/{mask}', 0)
    print(net, net.netmask)

#var3
for mask in range(33):
    net = ip_network(f'172.49.54.172/{mask}', 0)
    print(net, net.netmask)

#var4
for mask in range(33):
    net = ip_network(f'185.49.19.172/{mask}', 0)
    print(net, net.netmask)

#var8
for mask in range(33):
    net = ip_network(f'91.62.203.130/{mask}', 0)
    print(net)'''

#var8
for mask in range(33):
    net = ip_network(f'168.92.235.17/{mask}', 0)
    print(net)