import csv
import data_retriever


def write_to_csv(data):
    
    for element in data:
        print(element)
        header = [item.tag for item in element]
        print(header)
        
        with open('products_data.csv','w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            csvfile.close()
            
            