import urllib
import urllib2
import re

try:
    url = 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'
    #values = {'q' : 'sql'}
    #data = urllib.urlencode(values)
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib2.Request(url, None, headers = headers)

    resp = urllib2.urlopen(req)
    respdata = resp.read()
    paragraph = re.findall(r'<p>(.*?)</p>', str(respdata))
    savefile = open('respfile.txt', 'a')
    for eachp in paragraph:
        savefile.write(eachp)

    savefile.close()

except Exception, e:
    print(str(e))
