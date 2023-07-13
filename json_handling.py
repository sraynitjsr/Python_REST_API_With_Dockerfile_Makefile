import json
from collections import namedtuple

def start():
    print("Inside JSON Handling Using Python")

    my_python_data = {
        "name": "Ray",
        "age": 29
    }

    my_data_in_json = json.dumps(my_python_data)

    print("Python to JSON Data =>", my_data_in_json)

    data = '{"name": "Subhradeep Ray", "city": {"name": "Bengaluru", "id": 560045}}'

    x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    
    print("JSON to Python Data =>", x.name, x.city.name, x.city.id)
