import write_to_csv, config
import xml.etree.ElementTree as ET

# Define the file name (make sure the file is in the same directory as your script)
car_tyre_storage = []
car_rim_storage = []

tag_names = ['rim','car_tyre']






# Function to count occurrences of a specific value
def parse_values(file_paths):
    print('\n\n')
    for path in file_paths:
        file_tree = ET.parse(path)
        file_tree_root = file_tree.getroot()
        
        #check if the root element is autoplius - products
        if file_tree_root.tag == 'autoplius':
            #go through the element that stores all the other subelements of data
            for root_element in file_tree_root:
                #go through each subelement to fetch the different tag names
                for element in root_element:
                    config.product_type_storage.append(element)
            print('Finished parsing Autoplius products types\n')
            write_to_csv.write_to_csv()
            
        else:
            print('not autoplius')
        
        
                
                
        
        # if file_tree_root.tag == 'autoplius':
        #     count = 0
        #     for tag in tag_names:
        #         element_data_storage = []
        #         for element in file_tree_root.tag:
        #             print('\n',element)
        #             element_id = count
                    
                    #get data for car tyre elements
                    # if(tag == "car_tyre"):
                    #     sub_tags = ['is_condition_new','sell_price','comments','reservation','make_id','model','type','width','height','radius','quantity']
                        
                    #     element_condition = element.find('is_condition_new').text
                    #     element_price = element.find('sell_price').text
                    #     element_country = element.find('fk_place_countries_id').text
                    #     element_city = element.find('fk_place_cities_id').text
                    #     element_comments = element.find('comments').text
                    #     element_phone = element.find('contacts_phone').text
                    #     element_email = element.find('contacts_email').text
                    #     element_reservation = element.find('reservation').text
                    #     element_make = element.find('make_id').text
                    #     element_model = element.find('model').text
                    #     element_type = element.find('type').text
                    #     element_width = element.find('width').text
                    #     element_height = element.find('height').text
                    #     element_radius = element.find('radius').text
                    #     element_quantity = element.find('quantity').text
                        
                    #     element_data_storage.append(element_id,element_condition,element_price,
                    #                                 element_country,element_city,element_comments,
                    #                                 element_phone,element_email,element_reservation,
                    #                                 element_make,element_model,element_type,element_width,
                    #                                 element_height,element_radius,element_quantity)
                        
                    #     car_tyre_storage.append(element_data_storage)
                        
                    # #get data for car rim elements
                    # else:
                    #     car_rim_storage.append(element_data_storage)
                        
                    # count += 1
            # print(len(element_data_storage),len(car_rim_storage),len(car_tyre_storage),count)