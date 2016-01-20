import os

def get_ip_address(url):
    command = "ping " + url
    process = os.popen(command)
    results = str(process.read())
    print('results [' + results + ']')
    marker = results.find('has address') + 12
    return results[marker:]

print(get_ip_address('fundsupermarket.co.kr'))