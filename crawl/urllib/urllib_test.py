
import urllib.request

file = urllib.request.urlopen("http://www.baidu.com")

data=file.read()

dataline=file.readline()

# print (data)
#
# print (dataline)

fhandle = open("1.html",'wb')
fhandle.write(data)

fhandle.close()