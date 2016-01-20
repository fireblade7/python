import os

def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    print("command [" + command + "]")
    process = os.popen(command)
    results = str(process.read())
    return results

print(get_nmap('-F', '211.255.200.145'))