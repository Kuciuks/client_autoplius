import data_retriever, data_storer


def get_data(retriever):
    storage = []
    
    #fetch the product data
    product_data, status = retriever.retrieve_product_data()
    storage.append({'products':[product_data,status]})
    
    #fetch the tyre index data
    tyre_data, status = retriever.retrieve_tyre_data()
    storage.append({'tyre':[tyre_data,status]})
    
    #fetch the rims index data
    rims_data, status = retriever.retrieve_rims_data()
    storage.append({'rims':[rims_data,status]})
    
    # print('Length of data_storage = ',len(storage))
    return storage



if __name__=='__main__':
    
    #create an instance of the class RetrieveData
    retriever = data_retriever.RetrieveData()
    data = get_data(retriever)

    #create an instance of the class StoreData and pass fetched data as a parameter
    storer = data_storer.StoreData(data)
    
    #go through each item from the list of dictionaries
    for item in data:
        #get iterated items key:value pair values
        for key, value in item.items():
            #check if the data fetch status is True
            if value[1] == True:
                #store data to a file
                storer.store_data_file()

    
    
    

    