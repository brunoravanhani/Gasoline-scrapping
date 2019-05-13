#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[20]:


def convert(value):
    str_value = str(value)
    real = str_value[:1]
    cents = str_value[1:]
    final_value = real + '.' + cents
    return float(final_value)


# In[28]:


def get_na(value):
    if(value == '-'):
        return None
    return value


# In[2]:

print('get mean Gasolina')
req = requests.get('http://www.petrobras.com.br/pt/produtos-e-servicos/precos-de-venda-as-distribuidoras/gasolina-e-diesel/')
content = ''
if req.status_code == 200:
    content = req.content


# In[3]:


soup = BeautifulSoup(content, 'html.parser')


# In[4]:


container = soup.find(class_='wrapper-gc__grid-container')
table = container.find(name='table')


# In[10]:


df = pd.read_html(str(table), header=0)[0]


# In[11]:


df.columns = ['Local', 'Gasolina', 'Diesel_S500', 'Diesel_S10']


# In[29]:


gasolina = df['Gasolina'].map(get_na)


# In[31]:


gasolina.dropna(inplace=True)


# In[33]:


gasolina = gasolina.map(convert)


# In[35]:


print(gasolina.mean())

