import traceback
import xml.etree.ElementTree as ET

# Define the file name (make sure the file is in the same directory as your script)
car_tyre_storage = []
car_rim_storage = []


#function for storing data to a .xml file
def upload_data(item,data):
    try:
        with open(f'{item}_data.xml','w',encoding='utf-8') as file:
            file.write(data.decode('utf-8'))
            file.close()
        print(f'Data for {item} uploaded successfully!')
    except Exception as err:
        print(f'Encountered an error whilst uploading {item} data to a file, error: ',err)


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
                #match the values and upload to data to corresponding files
                match key:
                    case 'tyre':
                        print(f'Uploading data for {key}')
                        upload_data(key, value)
                        break
                    case 'rims':
                        print(f'Uploading data for {key}')
                        upload_data(key, value)
                        break
                    case 'products':
                        print(f'Uploading data for {key}')
                        upload_data(key, value)
                        break
                    
            

# Parse the XML file
# tree = ET.parse(file_name)
# root = tree.getroot()

    # # Function to count occurrences of a specific value
    # def count_values(tag_names):
    #     count = 0
    #     for tag in tag_names:
    #         element_data_storage = []
    #         for element in root.iter(tag):
                
    #             element_id = count
                
    #             #get data for car tyre elements
    #             if(tag == "car_tyre"):
    #                 sub_tags = ['is_condition_new','sell_price','comments','reservation','make_id','model','type','width','height','radius','quantity']
                    
    #                 element_condition = element.find('is_condition_new').text
    #                 element_price = element.find('sell_price').text
    #                 element_country = element.find('fk_place_countries_id').text
    #                 element_city = element.find('fk_place_cities_id').text
    #                 element_comments = element.find('comments').text
    #                 element_phone = element.find('contacts_phone').text
    #                 element_email = element.find('contacts_email').text
    #                 element_reservation = element.find('reservation').text
    #                 element_make = element.find('make_id').text
    #                 element_model = element.find('model').text
    #                 element_type = element.find('type').text
    #                 element_width = element.find('width').text
    #                 element_height = element.find('height').text
    #                 element_radius = element.find('radius').text
    #                 element_quantity = element.find('quantity').text
                    
    #                 element_data_storage.append(element_id,element_condition,element_price,
    #                                             element_country,element_city,element_comments,
    #                                             element_phone,element_email,element_reservation,
    #                                             element_make,element_model,element_type,element_width,
    #                                             element_height,element_radius,element_quantity)
                    
    #                 car_tyre_storage.append(element_data_storage)
                    
    #             #get data for car rim elements
    #             else:
    #                 car_rim_storage.append(element_data_storage)
                    
    #             count += 1