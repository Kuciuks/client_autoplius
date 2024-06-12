import requests
import config
import data_storer

def retry_fetch(url,type,attempt):
    if attempt > config.FETCH_RETRY_LIMIT:
        print(f'[{type}] Max retry limit reached. Fetch failed.')
        return [None, False]
    try:
        
        print(f'Retrying fetching for {type}')
        response = requests.get(url,timeout=10)
        return check_status(response, type, url, attempt)
    except requests.RequestException as err:
        print(f'[{type}] Exception during retry fetch: {e}')
        return retry_fetch(url, type, attempt + 1)

#check response status and return the contents
def check_status(response,type,url,attempt):
    #if successful return fetched data
    if response.status_code == 200:
        print(f'[{type}] Fetch was successful')
        return [response.content,True]

    #if failed retry until the limit is reached
    else:
        print(f'[{type}] Failed to fetch the data from url{response.status_code}')
        return retry_fetch(url, type, attempt + 1)


class RetrieveData:
    #class constructor
    def __init__(self):
        self.product_url = config.product_url
        self.tyre_url = config.tyre_url
        self.rims_url = config.rims_url

    
    #fetching data from URL
    def retrieve_product_data(self):
        try:
            #get request to the users product xml data on AutoPlius servers
            response = requests.get(self.product_url,timeout=10)
            data, status = check_status(response,'products',self.product_url)
            return data, status
        except requests.RequestException as err:
            print(f'[products] - Exception dring initial fetch: {err}')
        
        
    #tyre index value retriever
    def retrieve_tyre_data(self):
        response = requests.get(self.tyre_url,timeout=10)
        data, status = check_status(response,'tyres',self.tyre_url)
        return data, status
    
    
    #rims index value retriever
    def retrieve_rims_data(self):
        response = requests.get(self.rims_url,timeout=10)
        data, status = check_status(response,'rims',self.rims_url)
        return data, status
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # #fetches data and send it off to be stored
    # def send_data_to_store(self):
    #     #fetching url
    #     result = self.fetch_data()

    #     #check returned result value
    #     if result != None:
    #         print('Fetch was successful')
            
    #         #submit result xml data to store in a file
    #         data_storer.store_data_file(result)
    #     else:
    #         print('Fetch was unsuccessful')
