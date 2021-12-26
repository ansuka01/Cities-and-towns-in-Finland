import pandas as pd 
import requests 
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt


# get the response in the form of html
wiki="https://fi.wikipedia.org/wiki/Luettelo_Suomen_kaupungeista"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wiki)


# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
kaupungit=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(kaupungit))
# convert list to dataframe and sort alphabeticly

df=pd.DataFrame(df[0])
df.sort_values('Kaupunki', ascending=False)

#clean data by removing unnecessary columns
data_clean=df.drop(columns=["Maakunta", "Maapinta-ala(km²)[2]", "Väestötiheys(as./km²)"],  axis=1)

#convert to a numpy array
data_n = data_clean.to_numpy()



plt.hist(data_clean.head())
plt.show()





