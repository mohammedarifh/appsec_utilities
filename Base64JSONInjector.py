import base64
import json

# Decode base64 to get JSON data
base64_encoded_string = "<paste_your_base64_encoded_json_data_here>"
decoded_data = base64.b64decode(base64_encoded_string).decode('utf-8')
json_data = json.loads(decoded_data)

#  Read the text file with word list - Replace xss_list.txt with your payload text file.
with open("xss_list.txt", "r") as file:
    words = file.read().splitlines()

#  It will replace the "name" key in the json data with words from the list and encode each one separately. (Use key name accordingly for your json body format.)
if "name" in json_data:
    for i, word in enumerate(words):
        # Create a copy of the original JSON data
        modified_json_data = json_data.copy()
        modified_json_data["name"] = word

        # Encode the modified JSON back to base64
        modified_data = json.dumps(modified_json_data).encode('utf-8')
        encoded_data = base64.b64encode(modified_data).decode('utf-8')
        
        
        print(encoded_data)