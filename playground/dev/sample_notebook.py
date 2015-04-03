
# coding: utf-8

# In[1]:

##### custome imports
try:
    import template
except Exception as e:
    print e

##### standard imports
import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns
import pytz
import matplotlib.pylab as plt

##### globals
now = dt.datetime.now(pytz.timezone('US/Pacific'))
datestr = now.strftime('%m%d%y')
rootdir = './results/'

##### status, ipynb options
print 'script executed at', now
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows',    100)

#make the plots happen inline
get_ipython().magic(u'matplotlib inline')


# ## Make a simple matplotlib plot with numpy arrays

# In[2]:

X = np.random.randn(100)
Y = np.random.randn(100)

plt.scatter(X,Y)
plt.show()


# ## Make a DataFrame

# In[12]:

df = pd.DataFrame({'X':X,'Y':Y})
df.head()


# ##Make a pretty plot with seaborn

# In[14]:

sns.jointplot(X,Y, kind = 'reg' )


# In[ ]:



