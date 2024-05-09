from ipaddress import *

for mask in range(33):
    net = ip_network(f'20.24.110.42/{mask}', 0)
    print(net)