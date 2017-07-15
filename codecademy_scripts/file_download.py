import urllib2

url = "http://thinkpython.com/code/words.txt"

usock = urllib2.urlopen(url)                                  #function for opening desired url
file_name = url.split('/')[-1]                                #Example : for given url "www.cs.berkeley.edu/~vazirani/algorithms/chap6.pdf" file_name will store "chap6.pdf"
f = open(file_name, 'wb')                                     #opening file for write and that too in binary mode.
file_size = int(usock.info().getheaders("Content-Length")[0]) #getting size in bytes of file(pdf,mp3...)
print "Downloading: %s Bytes: %s" % (file_name, file_size)


                                           #bytes to be downloaded in each loop till file pointer does not return eof
while True:
   buff = usock.readline()
   f.write(str(buff))
   if not buff:                                             #file pointer reached the eof
    break


print download_status,"done"

f.close()
