#!/usr/bin/python3
"""with open('tony.txt', 'r') as file:
    content = file.read()
    print(content)
    file.close()
    for line in file:
        print(line.strip())
    file.close()
    print(file.read(7))
    print(file.tell())
    file.seek(0)
    print(file.read())
    # file.close()

    content = file.read()
print(content)"""

import json

data = {'name': 'Tony', 'age': 20}
json_string = json.dumps(data)
print(json_string) # {"name": "Tony", "age": 20}

json_string = '{"name": "Robert", "age": 21}'
data = json.loads(json_string)
print(data) # {'name': 'Robert', 'age': 21}

data = {'items': [1, 2, 3]}
json_string = json.dumps(data)
print(json_string)