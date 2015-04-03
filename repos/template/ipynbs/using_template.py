
# coding: utf-8

# Dont forget to install your package. 
# 
# ```
# python setup.py install
# ```
# or on a mac...
# ```
# sudo python setup.py install
# ```

# In[1]:

import template


# try using the tab button to see what modules and methods you have avaliable

# In[2]:

template.simple_module


# try shit tab after () to see the doc string of the methods you build in simple module

# In[3]:

die = template.simple_module.die(6)
die.roll()


# >In order to make updates to the source code:
#     1. The source code must be saved.
#     2. The package must be re-installed with "python setup.py install"
#     3. The notebook kernal must be restarted
