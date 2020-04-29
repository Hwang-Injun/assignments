"""
import nmap

# take the range of ports to
# be scanned
begin, end = map(int, input().split())
port = 80

# assign the target ip to be scanned to
# a variable
target = '127.166.177.200'

# instantiate a PortScanner object
scanner = nmap.PortScanner()

for i in range(begin, end+1):

    # scan the target port
    res = scanner.scan(target, str(i))

    # the result is a dictionary containing
    # several information we only need to
    # check if the port is opened or closed
    # so we will access only that information
    # in the dictionary
    res = res['scan'][target]['tcp'][i]['state']

    print(f"port {i} is {res}.")
"""
import nmap
import time

nm = nmap.PortScanner()
start_time = time.time()
nm.scan(hosts='166.104.177.0/24', arguments='-n -sP')
hosts_list = [(x, nm[x]['status']['state'])
              for x in nm.all_hosts()]

for host, status in hosts_list:
    print(host + ' is ' + status)

elapsed_time = round(time.time() - start_time, 3)
print(f"Scan duration: {elapsed_time}")
print(f"Total number of web servers: {len(hosts_list)}")
