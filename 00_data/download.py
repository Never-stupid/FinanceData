
# coding: utf-8

# In[1]:

import pandas as pd
import requests
from multiprocessing.dummy import Pool as ThreadPool


# In[2]:

lrb_base_url = 'http://api.xueqiu.com/stock/f10/incstatement.csv?page=1&size=10000&symbol='
llb_base_url = 'http://api.xueqiu.com/stock/f10/cfstatement.csv?page=1&size=10000&symbol='
fzb_base_url = 'http://api.xueqiu.com/stock/f10/balsheet.csv?page=1&size=10000&symbol='


# In[3]:

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Cookie': 'xq_a_token=82d9cefaa0793743cb186e53294ec0e61ac2abec'
}


# In[4]:

def download_lrb(url):
    r = requests.get(url, headers=headers)
    filename = url.split('=')[-1] + '_lrb.csv'
    print(filename)
    with open(filename, 'wb') as f:
        f.write(r.content)


# In[5]:

def download_fzb(url):
    r = requests.get(url, headers=headers)
    filename = url.split('=')[-1] + '_fzb.csv'
    print(filename)
    with open(filename, 'wb') as f:
        f.write(r.content)


# In[6]:

def download_llb(url):
    r = requests.get(url, headers=headers)
    filename = url.split('=')[-1] + '_llb.csv'
    print(filename)
    with open(filename, 'wb') as f:
        f.write(r.content)


# In[7]:

with open('symbol.txt', 'r', encoding='utf-8') as f:
    symbol = [s.strip() for s in f.readlines()]
len(symbol)
symbol


# In[8]:

lrb_urls = [lrb_base_url + i for i in symbol]
fzb_urls = [fzb_base_url + i for i in symbol]
llb_urls = [llb_base_url + i for i in symbol]


# In[11]:

llb_urls


# In[ ]:

pool = ThreadPool(10)
pool.map(download_lrb, lrb_urls)
pool.close()
pool.join()
pool = ThreadPool(10)
pool.map(download_fzb, fzb_urls)
pool.close()
pool.join()
pool = ThreadPool(10)
pool.map(download_llb, llb_urls)
pool.close()
pool.join()


# In[ ]:



