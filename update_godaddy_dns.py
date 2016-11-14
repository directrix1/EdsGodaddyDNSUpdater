#!/usr/bin/env python3

# Ed's Godaddy DNS Updater
#
# Copyright ©2016 Edward Flick under GPLv2 license

import http.client
import json
import conf

# Godaddy connection information
server = conf.godaddy['server']
endpoint = '/v1/domains/'+conf.domain+'/records/A/'+conf.host
aheaders = {
    'Authorization': 'sso-key '+conf.godaddy['key']+':'+conf.godaddy['secret'],
    'Accept': 'application/json'
    }

# Get your IP from directrix1.com IP checker, you're welcome for the service. :-P
con = http.client.HTTPSConnection('directrix1.com')
con.request('GET', '/ip.php')
ip = con.getresponse().read().decode('utf-8')
print('Your IP: '+ip+'\n')

# Find out what godaddy has on file for that host
con = http.client.HTTPSConnection(server)
con.request('GET', endpoint, headers=aheaders)
res=con.getresponse()
resj=json.loads(res.read().decode('utf-8'))
if res.status==200:
    if len(resj)==0:
        print('A record for '+conf.host+' not found.')
        exit(1)
    godaddy_ip = resj[0]['data']
    godaddy_ttl = resj[0]['ttl']
    print('Your godaddy address: '+godaddy_ip)
else:
    print('Failed checking godaddy address:')
    print(resj)
    exit(2)

if godaddy_ip==ip:
    print('No need to update! :-)')
    exit(0)

print('Time to update that godaddy ip!')
abody=json.dumps([{
    'data': ip,
    'ttl': godaddy_ttl
    }])
aheaders['Content-Type'] = 'application/json'

# Update the host on godaddy
con = http.client.HTTPSConnection(server)
con.request('PUT', endpoint, body=abody, headers=aheaders)
res=con.getresponse()
resj=json.loads(res.read().decode('utf-8'))
if res.status==200:
    print('Successfully updated your address!')
else:
    print('Failed setting godaddy address:')
    print(resj)
    exit(3)
