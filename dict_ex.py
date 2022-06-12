#  Convert two lists into a dictionary

keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

result = {key: value for key, value in zip(keys, values)}
print(result)

# Merge two Python dictionaries into one

dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}

joined_dict = {**dict1, **dict2}
print(joined_dict)

# Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
}

print(sampleDict["class"]["student"]["marks"]["history"])

# Initialize dictionary with default values

employees = ["Kelly", "Emma"]
defaults = {"designation": "Developer", "salary": 8000}
res = dict.fromkeys(employees, defaults)
print(res)

# Create a dictionary by extracting the keys from a given dictionary
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
key_1 = "name"
key_2 = "salay"
joined = dict()
joined = {key: sample_dict[key] for key in keys}
print(joined)

res = dict()

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)

# Delete a list of keys from a dictionary

sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# Keys to remove
keys = ["name", "salary"]
antwort = dict()

for key in keys:
    sample_dict.pop(key)

print(sample_dict)

d = {
    1: ["Samuel", 21, "Data Structures"],
    2: ["Richie", 20, "Machine Learning"],
    3: ["Lauren", 21, "OOPS with java"],
}

str_fmt = "{:<8} {:<8} {:<8}"
print(str_fmt.format("Name", "Age", "label "))
print(f" -----------------")
for k, v in d.items():
    label, num, va = v
    print(str_fmt.format(k, label, num))


name = "Bo"
age = "2"
salary = "3"
print("{:<10} | {} | {} ".format(name, age, salary))

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

print([l[:2] for l in l_2d[1:3]])
# [[3, 4], [6, 7]]

l_2d_t = [list(x) for x in zip(*l_2d)]
print(l_2d_t)
# [[0, 3, 6, 9], [1, 4, 7, 10], [2, 5, 8, 11]]

print(l_2d_t[1])
# [1, 4, 7, 10]
A = dict(zip("abcdef", list(range(6))))
for key in A:
    print(key, A[key])


myDict = {
    "foo": {"a": 12, "b": 14},
    "bar": {"c": 12, "b": 14},
    "moo": {"a": 12, "d": 14},
}
