import traceback
import os
import config


#function for storing data to a .xml file
def upload_data(item,data):
    try:
        with open(f'{item}_data.xml','w',encoding='utf-8') as file:
            file.write(data.decode('utf-8'))
            config.file_paths.append(os.path.abspath(file.name))
            file.close()
            
        print(f'Data for {item} uploaded successfully!')
    except Exception as err:
        print(f'Encountered an error whilst uploading {item} data to a file, error: ',err)
        traceback.print_exc()

class StoreData:
    #class constructor
    def __init__(self,data):
        self.data = data
    
    #store and decode the xml b'data' into a .xml file
    def store_data_file(self):
        #go through the target items(products,tyres,rims) list and retrieve their key:value pairs
        for item in self.data:
            #get the key and value values of the current target item dictionary            
            for key, value in item.items():
                
                #check if the item(data) had been fetched succesfully
                if value[1] == True:
                    #match key values and upload data to corresponding files
                    match key:
                        case 'tyre':
                            print(f'Uploading data for {key}')
                            upload_data(key, value[0])
                            break
                        case 'rims':
                            print(f'Uploading data for {key}')
                            upload_data(key, value[0])
                            break
                        case 'products':
                            print(f'Uploading data for {key}')
                            upload_data(key, value[0])
                            break
                        case 'truck':
                            print(f'Uploading data for {key}')
                            upload_data(key, value[0])
                            break
                
                else:
                    print(f'{key} data status has not been fetched successfully')