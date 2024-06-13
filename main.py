import data_retriever, data_storer, config, data_parser


def get_data(retriever):
    storage = []
    
    #fetch the product data
    product_data, product_status = retriever.retrieve_product_data()
    storage.append({'products':[product_data,product_status]})
    
    #fetch the tyre index data
    tyre_data, tyre_status = retriever.retrieve_tyre_data()
    storage.append({'tyre':[tyre_data,tyre_status]})
    
    #fetch the rims index data
    rims_data, rims_status = retriever.retrieve_rims_data()
    storage.append({'rims':[rims_data,rims_status]})
    
    # print('Length of data_storage = ',len(storage))
    return storage



if __name__=='__main__':
    
    #create an instance of the class RetrieveData
    retriever = data_retriever.RetrieveData()
    data = get_data(retriever)

    #create an instance of the class StoreData and pass fetched data as a parameter
    storer = data_storer.StoreData(data)
    
    #store data to a file
    storer.store_data_file()

    #parse data from files at location(config.file_paths) and get all cells of data into an array
    data_parser.parse_values(config.file_paths)
    
    
    

    