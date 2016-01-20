import urllib
import io

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
        
    else:
        path = url + '/'
        
    print(path)
        
    req = urllib.urlopen(path + 'robots.txt', data=None)
    
    print(req.headers)
    #print(req.read())
    return req.read()

print(get_robots_txt('https://www.google.com'))
    
    
