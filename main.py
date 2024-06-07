import data_retriever, data_storer

if __name__=='__main__':
    
    #create an instance of the class RetrieveProducts
    retriever = data_retriever.RetrieveProducts()
    #fetch the data
    fetched_data = retriever.fetch_data()
    
    
    #create an instance of the class StoreData and pass fetched data as a parameter
    storer = data_storer.StoreData(fetched_data)
    #store data to a file
    storer.store_data_file()
    