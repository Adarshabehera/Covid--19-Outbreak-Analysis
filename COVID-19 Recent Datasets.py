#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[2]:


covid_df = pd.read_csv("C:/Users/ADARSHA KUMAR BEHERA/Desktop/ALL PROJECTS/Covid cases/covid_19_india.csv")


# In[3]:


covid_df.head(3)


# In[4]:


covid_df.tail(4)


# In[5]:


covid_df.isna().sum()


# In[6]:


covid_df.duplicated


# In[7]:


covid_df.columns


# In[8]:


covid_df.info()


# In[9]:


covid_df.describe()


# In[10]:


vaccine_df = pd.read_csv("C:/Users/ADARSHA KUMAR BEHERA/Desktop/ALL PROJECTS/Covid cases/covid_vaccine_statewise.csv")


# In[11]:


vaccine_df.head(5)


# In[12]:


covid_df.columns


# In[13]:


vaccine_df.columns


# In[14]:


covid_df.drop(['Sno','Time','ConfirmedIndianNational','ConfirmedForeignNational'], axis =1, inplace = True)


# In[15]:


covid_df.head(4)


# In[16]:


covid_df['Date'] = pd.to_datetime(covid_df['Date'], format = '%Y-%m-%d')


# In[17]:


covid_df.head(4)


# In[18]:


covid_df['Active_cases'] = covid_df['Confirmed'] - (covid_df['Cured'] + covid_df['Deaths'])


# In[19]:


covid_df.tail(40)


# In[20]:


covid_df.columns


# ### Creating the pivot tables in pandas 

# In[194]:


statewise = pd.pivot_table(covid_df, values = ['Confirmed','Deaths','Cured'], index = 'State/UnionTerritory', aggfunc = 'max')


# In[195]:


statewise


# In[196]:


statewise['Recovery_rate'] = statewise['Cured']*100 /statewise['Confirmed']


# In[197]:


statewise['Mortality_rate'] = statewise['Deaths']*100 /statewise['Confirmed']


# In[198]:


statewise['Recovery_rate'] 


# In[199]:


statewise['Mortality_rate']


# In[200]:


statewise = statewise.sort_values(by = 'Confirmed', ascending =False)


# In[28]:


statewise


# ## For the pivot visualization in python :-

# In[29]:


statewise.style.background_gradient (cmap = 'cubehelix')


# ### Top 10 Active cases :-

# In[201]:


top_10_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_cases','Date']].sort_values(by = ['Active_cases'], ascending = False).reset_index()


# In[202]:


top_10_active_cases


# ### Final coding for the Top 10 active cases states for the Covid - 19 

# ## Active Cases :-

# In[203]:


top_10_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_cases','Date']].sort_values(by = ['Active_cases'], ascending = False).reset_index()
fig = plt.figure(figsize = (20,9))
ax = sns.barplot(data = top_10_active_cases.iloc[:10], y = 'Active_cases', x = 'State/UnionTerritory', linewidth = 3, edgecolor = 'black')
plt.title('Top 10 States with most active cases in the world', size = 15)
plt.xlabel('State/UnionTerritory')
plt.ylabel('Active_cases')
plt.show()


# ### Death rates

# In[36]:


top_10_deaths = covid_df.groupby(by = 'State/UnionTerritory').max()[['Deaths','Date']].sort_values(by = ['Deaths'],ascending = False).reset_index()
fig = plt.figure(figsize = (20,10))
ax= sns.barplot(data = top_10_deaths.iloc[:10],y = 'Deaths', x = 'State/UnionTerritory', linewidth = 2, edgecolor = 'orange')
plt.title('Top 10 states with highest death rates', size= 25)
plt.xlabel('State/UnionTerritory')
plt.ylabel('Deaths')
plt.show()


# In[37]:


covid_df.columns


# ### Growth Trends :-

# In[38]:


covid_df['State/UnionTerritory'].value_counts()


# In[39]:


fig = plt.figure(figsize = (16,6))
ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra','Odisha','Assam','Karnataka','Kerela','Tamil Nadu','Uttar Pradesh'])],x = 'Date', y = 'Active_cases', hue = 'State/UnionTerritory')
ax.set_title('Top 7 states with most confirmed active cases ongoing')


# In[40]:


vaccine_df.info()


# In[67]:


vaccine_df.head()


# In[68]:


vaccine_df.rename(columns = {'Updated On' :'Vaccine_date'}, inplace =True)


# In[69]:


vaccine_df.info()


# In[70]:


vaccine_df.isna().sum()


# ## Carrying out the unwanted columns from the datsets :-

# In[71]:


vaccine_df.columns


# In[72]:


vaccination = vaccine_df.drop(['Sputnik V (Doses Administered)',
       'AEFI', '18-44 Years (Doses Administered)',
       '45-60 Years (Doses Administered)', '60+ Years (Doses Administered)'], axis = 1, inplace =True)


# In[73]:


vaccine_df.head(4)


# ## Male and Female Vaccinations with pie plot:-

# In[74]:


male = vaccine_df['Male(Individuals Vaccinated)'].sum()
Female = vaccine_df['Female(Individuals Vaccinated)'].sum()
px.pie(names = ['Male','Female'], values = [male, Female], title = 'Total vaccinated personnel for Male and Female through out the process')


# ## Removing the state of India:-

# In[87]:


vaccine_df.columns


# In[88]:


vaccine = vaccine_df[vaccine_df.State != 'India']


# In[89]:


vaccine


# In[90]:


vaccine_df


# In[91]:


vaccine.rename(columns = {'Total Individuals Vaccinated' : 'Total'}, inplace =True)


# In[148]:


vaccine.head(4)


# ### Most Vaccinated States :-

# In[173]:


max_vac=vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac1 = max_vac.sort_values('Total', ascending = False)[:5]
max_vac


# In[174]:


max_vac1


# In[175]:


fig = plt.figure(figsize = (10,5))
x = sns.barplot(data = max_vac1.iloc[:5], y = max_vac1.Total, x = max_vac1.index, linewidth = 2, edgecolor = 'Magenta')
plt.title('Max vaccination states procured', size = 10)
plt.xlabel('States')
plt.ylabel('Vaccination')
plt.show()


# In[176]:


vaccine.columns


# In[180]:


min_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
min_vac1 = min_vac.sort_values(by = 'Total', ascending = True)[:5]
min_vac1


# ##3 Showing the Least vaccination states in the Portals:-

# In[184]:


fig = plt.figure(figsize = (12,6))
x = sns.barplot(data = min_vac1[:5], y = min_vac1.Total, x = min_vac1.index, linewidth = 2, edgecolor = 'Blue')
plt.title('Least vaccination Campaign state wise List')
plt.xlabel('Total Measured States')
plt.ylabel('Vaccination')
plt.show()


# ### From above we have seen that Maharastra is the leading state vaccination centre as compared to the Lakshadweep as we can
# ## see that the rate is way lower than any states.so, we have to give proper investigation to this matter for better results.

# In[ ]:




