import xml.etree.ElementTree as ET

# Define the file name (make sure the file is in the same directory as your script)
file_name = 'product_info.xml'

car_tyre_storage = []
car_rim_storage = []


# Parse the XML file
tree = ET.parse(file_name)
root = tree.getroot()

# Function to count occurrences of a specific value
def count_values(tag_names):
    count = 0
    for tag in tag_names:
        element_data_storage = []
        for element in root.iter(tag):
            
            element_id = count
            element_phone = element.find('contacts_phone').text
            element_email = element.find('contacts_phone').text
            element_reservation = element.find('contacts_phone').text
            element_phone = element.find('contacts_phone').text
            element_phone = element.find('contacts_phone').text
            element_phone = element.find('contacts_phone').text
            element_phone = element.find('contacts_phone').text
            element_data_storage.append(element_id)
            count += 1
            
            if(tag == "car_tyre"):
                car_tyre_storage.append(element_data_storage)
            else:
                car_rim_storage.append(element_data_storage)

#search for specific xml <tag>
tag_names = ['car_tyre','rim']

count_values(tag_names)
print(len(car_rim_storage),len(car_tyre_storage))

