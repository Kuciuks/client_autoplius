import requests
import config
import data_storer



    
def check(response,type):
    #if successful return fetched data
    if response.status_code == 200:
        print(f'[{type}] Fetch was successful')
        return response.content

    #if failed throw an error and return None
    else:
        print(f'[{type}] Failed to fetch the data from url{response.status_code}')
        return None

#check response status and return the contents
def check_status(response, type):
    
    match type:
        case 'product':
            product_result = check(response)
        case 'tyre':
            tyre_result = check(response)
        case 'rims':
            rims_result = check(response)




class RetrieveData:
    #class constructor
    def __init__(self):
        self.product_url = config.product_url
        self.tyre_url = config.tyre_url
        self.rims_url = config.rims_url

    
    #fetching data from URL
    def retrieve_product_data(self):
        #get request to the users product xml data on AutoPlius servers
        response = requests.get(self.product_url)
        check_status(response,'products')
        
        
    #tyre index value retriever
    def retrieve_tyre_data(self):
        response = requests.get(self.tyre_url)
        check_status(response,'tyres')
    
    
    #rims index value retriever
    def retrieve_rims_data(self):
        response = requests.get(self.rims_url)
        check_status(response,'rims')
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
