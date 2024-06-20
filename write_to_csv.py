import csv
import data_retriever,config


def write_to_csv():
    products = config.product_type_storage
    
    #go through each individual element inside the data array
    for element in products:
        #go through details of the element
        for details in element:
            print(details, details.tag, element)
        # #capture element names as column values
        # header = [item.tag for item in details]
        
        # with open(f'{element.tag}.csv','w',newline='') as csvfile:
        #     writer = csv.writer(csvfile)
        #     writer.writerow(header)
        #     csvfile.close()
            
            