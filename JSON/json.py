import json


json_string = '{"name": "nam & aum", "age":21,
"city":"Bangkok"}'

python_dict = json.loads(json_string)

print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])