import nmap

start, end = 75, 80

target = '127.0.0.1'

scanner = nmap.PortScanner()

for i in range(start, end):

    response = scanner.scan(target, str(i))

    state = response['scan'][target]['tcp'][i]['state']
    
    print(f'\n Port {i} state: {state} ... \n')
