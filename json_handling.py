
import json

def start():
    print("Inside JSON Handling Using Python")

    my_python_data = {
        "name": "Ray",
        "age": 29
    }

    my_data_in_json = json.dumps(my_python_data)

    print("JSON Data", my_data_in_json)
