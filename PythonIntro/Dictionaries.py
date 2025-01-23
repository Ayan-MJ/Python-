# my_dict = {"name": "Alice", "age": 25, "city": "New York"}

my_dict = dict(name="Alice", age=25, city="New york")

# print(my_dict)

# print(my_dict['name'])
# print(my_dict["age"])

# print(my_dict.get("name"))
# print(my_dict.get("age"))
# print(my_dict.get("Occupation", "Unknown"))

# my_dict["Occupation"] = "Engineer"

# my_dict["age"] = 26

# print(my_dict)

# del my_dict["city"]

# age = my_dict.pop("age")

# Iterating over key value pair

for key, value in my_dict.items():
    print(f"{key}: {value}")

keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(key, values)}
print(my_dict)

if key in my_dict:
    print(f"{key} exits!")




