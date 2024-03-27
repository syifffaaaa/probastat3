#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

data_syifa = pd.read_clipboard()

# Menampilkan data
print(data_syifa)


# In[7]:


syifa = data_syifa[data_syifa['Bedrooms'] == 2]

# Menampilkan nama
print(syifa)


# In[9]:


syifa['Bathrooms'] = pd.to_numeric(syifa['Bathrooms'])

import numpy as np

syifa['Bathrooms'] = syifa['Bathrooms'].apply(lambda x: 'large' if x > 2 else 'small')

# Menampilkan DataFrame setelah modifikasi
print(syifa)


# In[10]:


import numpy as np

syifa['newvariable'] = np.where(syifa['Offers'] > 2, 'large', 'small')

# Menampilkan DataFrame 'nama' setelah penambahan kolom baru
print(syifa)


# In[11]:


# Menambahkan kolom baru 'newvariable' 
syifa['newvariable'] = syifa['Price'] / syifa['SqFt']

# Menampilkan DataFrame 'nama' setelah penambahan kolom baru
print(syifa)


# In[12]:


syifa = syifa.drop(columns=['newvariable'])

# Menampilkan DataFrame 'nama' 
print(syifa)


# In[13]:


kolom1dan2 = data_syifa.iloc[:, 0:2]

# Menampilkan DataFrame kolom1dan2
print(kolom1dan2)


# In[14]:


# Memilih kolom 1 dan 2 dari DataFrame data_nama
kolom3dan4 = data_syifa.iloc[:, 2:4]

# Menampilkan DataFrame kolom3dan4
print(kolom3dan4)


# In[18]:


# Menggabungkan dua DataFrame 
kolom1sd4 = pd.concat([kolom1dan2, kolom3dan4], axis=1)

# Menampilkan DataFrame kolom1sd4
print(kolom1sd4)


# In[29]:


#import pandas library
import pandas as pd

# Menggabungkan baris dari dua DataFrame
baris1sd3 = data_syifa.iloc[0:3, :]
baris4sd6 = data_syifa.iloc[3:6, :]
baris1sd6 = pd.concat([baris1sd3, baris4sd6])

# Menampilkan DataFrame baris1sd6
print(baris1sd6)


# In[24]:


data_nama_sort = data_syifa.sort_values(by='Price')

print(data_nama_sort)


# In[ ]:





# In[ ]:


tugas 2


# In[6]:


import pandas as pd

data_valid = pd.read_clipboard()

print(data_valid)


# In[7]:


syifa = data_valid[data_valid['Tinggi Badan'] == 160]

print(syifa)


# In[9]:


import pandas as pd
syifa['Tinggi Badan'] = pd.to_numeric(syifa['Tinggi Badan'])

import numpy as np

syifa['Tinggi Badan'] = syifa['Tinggi Badan'].apply(lambda x: 'Tinggi' if x> 160 else 'Pendek')

print(syifa)


# In[10]:


import numpy as np

syifa['Jurusan'] = 'Infor23'
syifa['Fakultas'] = 'FTI'

print(syifa)


# In[12]:


syifa = syifa.drop(columns=['Fakultas'])

print(syifa)


# In[28]:


kolom1dan2 = syifa.iloc[:,0:2]
print(kolom1dan2)

kolom3dan4 = syifa.iloc[:,2:4]
print(kolom3dan4)

kolom1sd4 = pd.concat([kolom1dan2, kolom3dan4],axis=1)
print(kolom1sd4)


# In[31]:


import pandas as pd

baris1sd5 = syifa.iloc[0:5,:]
baris25sd30 = syifa.iloc[24:31,:]
baris1sd5dan25sd30 = pd.concat([baris1sd5, baris25sd30])

print(baris1sd5dan25sd30)


# In[35]:


syifa_sort = syifa.sort_values(by='Waktu Perjalanan')

print(syifa_sort) 


# In[ ]:




