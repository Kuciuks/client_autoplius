import csv
import data_retriever,config


def write_to_csv():
    print(config.product_type_storage)
    
    #go through each individual element inside the data array
    # for element in data:
    #     #go through details of the element
    #     # for details in element:
    #         # print(details.text)
    #     # print(element)
    #     #capture element names as column values
    #     header = [item.tag for item in element]
    #     # print(header)
        
    #     with open('products_data.csv','w',newline='') as csvfile:
    #         writer = csv.writer(csvfile)
    #         writer.writerow(header)
    #         csvfile.close()
            
            