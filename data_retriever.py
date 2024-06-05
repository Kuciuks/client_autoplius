import xml.etree.ElementTree as ET
import requests
import config
import data_storer











#fetching data from URL
def fetch_data(url):
    #get request to the users product xml data on AutoPlius servers
    response = requests.get(url)
    
    #if successful return fetched data
    if response.status_code == 200:
        return response.content

    #if failed throw an error and return None
    else:
        print(f'Failed to fetch the data from url{response.status_code}')
        return None
    
    
#fetching url
result = fetch_data(config.url)

#check returned result value
if result != None:
    print('Fetch was successful') #\n\n{result}
    
    
else:
    print('Fetch was unsuccessful')
