import httplib, urllib 
from bs4 import BeautifulSoup 
import os 
import json
import time

access_token='ACCESS TOKEN PLEASE!'
conn = httplib.HTTPSConnection("graph.facebook.com") 
print 'Please Wait!'
 
def comment(url): 
    connect = httplib.HTTPSConnection("graph.facebook.com") 
    connect.request("GET",url) 
    for x in xrange(1000):         
            
            print 'commenting %d '% x
            path ='/'+'PUT FB STATUS ID HERE'+'/comments' # you have to put the digits after ?fbid before '/comments'
            param_data={  'format':'json', 
                        'message':'Auto Generated Comment', # you can change this message. 
                        'access_token':access_token 
                  } 
            connect = httplib.HTTPSConnection("graph.facebook.com") 
            connect.request("POST",path,urllib.urlencode(param_data),{}) 
            time.sleep(0.09)
           
url='/PUT FB STATUS ID HERE' # same as you have done at line 17
comment(url) 
print 'DONE!'
