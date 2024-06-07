import data_retriever, data_storer

if __name__=='__main__':
    
    #create an instance of the class RetrieveProducts
    retriever = data_retriever.RetrieveProducts()
    #fetch the product data
    fetched_data = retriever.fetch_data()
    
    #create an instance of the class RetrieveIndexInfo
    other_retriever = data_retriever.RetrieveTyreRimsIndexInfo()
    #fetch the tyre and rims index data
    tyre_data = other_retriever.retrieve_rims_data()
    tyre_data = other_retriever.retrieve_tyre_data
    
    
    #create an instance of the class StoreData and pass fetched data as a parameter
    storer = data_storer.StoreData(fetched_data,'product')
    #store data to a file
    storer.store_data_file()
    