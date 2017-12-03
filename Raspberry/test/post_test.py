import urllib2
import urllib
def http_post():  
    url = "http://YOUR_SERVER_IP/spy"  
    postdata = 'data=10'  
    req = urllib2.Request(url,postdata)   
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')  
    response = urllib2.urlopen(req)  
    result = response.read() 
    print result
if __name__ == '__main__':
    http_post()
