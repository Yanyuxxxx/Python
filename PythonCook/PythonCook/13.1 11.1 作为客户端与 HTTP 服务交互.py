from urllib import request, parse

# url = 'http://httpbin.org/get'
url = 'http://httpbin.org/post'

parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

querystring = parse.urlencode(parms)

# u = request.urlopen(url+'?' + querystring)
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()


print(resp)