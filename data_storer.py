import traceback
import xml.etree.ElementTree as ET

# Define the file name (make sure the file is in the same directory as your script)
car_tyre_storage = []
car_rim_storage = []



# Parse the XML file
# tree = ET.parse(file_name)
# root = tree.getroot()

# Function to count occurrences of a specific value
def count_values(tag_names):
    count = 0
    for tag in tag_names:
        element_data_storage = []
        for element in root.iter(tag):
            
            element_id = count
            
            #get data for car tyre elements
            if(tag == "car_tyre"):
                sub_tags = ['is_condition_new','sell_price','comments','reservation','make_id','model','type','width','height','radius','quantity']
                
                element_condition = element.find('is_condition_new').text
                element_price = element.find('sell_price').text
                element_country = element.find('fk_place_countries_id').text
                element_city = element.find('fk_place_cities_id').text
                element_comments = element.find('comments').text
                element_phone = element.find('contacts_phone').text
                element_email = element.find('contacts_email').text
                element_reservation = element.find('reservation').text
                element_make = element.find('make_id').text
                element_model = element.find('model').text
                element_type = element.find('type').text
                element_width = element.find('width').text
                element_height = element.find('height').text
                element_radius = element.find('radius').text
                element_quantity = element.find('quantity').text
                
                element_data_storage.append(element_id,element_condition,element_price,
                                            element_country,element_city,element_comments,
                                            element_phone,element_email,element_reservation,
                                            element_make,element_model,element_type,element_width,
                                            element_height,element_radius,element_quantity)
                
                car_tyre_storage.append(element_data_storage)
                
            #get data for car rim elements
            else:
                car_rim_storage.append(element_data_storage)
                
            count += 1
            
def store_data_file(data):
    try:
        with open('product_data.xml','w',encoding='utf-8') as file:
            file.write(data.decode('utf-8'))
            file.close()
    except Exception as err:
        print(f"Failed to write to file, error: {err}")
        # traceback.print_exc()



#search for specific xml <tag>
tag_names = ['car_tyre','rim']

# count_values(tag_names)
# print(len(car_rim_storage),len(car_tyre_storage),'\n\n',car_tyre_storage)