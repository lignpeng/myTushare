import urllib
url='http://www.freedom.com:8001/img/people'
protocol, s1 = urllib.splittype(url)
# ('http', '//www.freedom.com:8001/img/people')
print(protocol,s1)
host, s2 = urllib.splithost(s1)
# ('www.freedom.com:8001', '/img/people')

hostUrl = protocol +'://'+host
print(hostUrl)

print(host,s2)
host, port = urllib.splitport(host)
print(host,port)
# ('www.freedom.com', '8001')
