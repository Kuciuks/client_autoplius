import requests
import config
import data_storer
import codecs


class RetrieveProducts:
    
    def __init__(self):
        self.url = config.url
    
    #fetching data from URL
    def fetch_data(self):
        #get request to the users product xml data on AutoPlius servers
        response = requests.get(self.url)
        
        #if successful return fetched data
        if response.status_code == 200:
            return response.content

        #if failed throw an error and return None
        else:
            print(f'Failed to fetch the data from url{response.status_code}')
            return None
    
    #fetches data and send it off to be stored
    def send_data_to_store(self):
        #fetching url
        result = self.fetch_data()

        #check returned result value
        if result != None:
            print('Fetch was successful')
            
            #submit result xml data to store in a file
            data_storer.store_data_file(result)
        else:
            print('Fetch was unsuccessful')

#create an instance of the class
retriever = RetrieveProducts()
retriever.send_data_to_store()