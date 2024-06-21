import csv
import data_retriever,config


def product_to_csv(data):
    
    #go through each individual element inside the data array
    for product in data:
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
            
            
def value_to_csv(data,name):
    id_values = []
    values = []
    #go through each individual element inside the data array
    for product in data:
        # capture product column values for products
        details = [details.text for details in product]
        id_values.append(details[0])
        values.append(details[1])

    with open(f'{name}.csv','w',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(id_values)            
        writer.writerow(values)            
        csvfile.close()
        