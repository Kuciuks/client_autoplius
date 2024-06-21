import csv
import data_retriever,config


def product_to_csv():
    products = config.product_type_storage
    
    #go through each individual element inside the data array
    for product in products:
        #capture product column values for products
        collumn_names = [details.tag for details in product[0]]
        with open(f'{product.tag}.csv','w',newline='',encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(collumn_names)
            
            #get details for each new product
            for element in product:
                values = [values.text for values in element]
                writer.writerow(values)            
            csvfile.close()
            
            