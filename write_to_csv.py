import csv
import data_retriever,config


def product_to_csv():
    products = config.product_type_storage
    
    #go through each individual element inside the data array
    for element in products:
        # #capture element names as column values
        collumn_names = [details.tag for details in element[0]]
        
        with open(f'{element.tag}.csv','w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(collumn_names)
            csvfile.close()
            
            