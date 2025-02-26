# 1
''''''

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# res_dict = dict(zip(keys, values))
# print(res_dict)
d = {}
for i in range(len(keys)):
    d.update({keys[i]:values[i]})
print(d)





# 2 


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

for k,v in dict2.items():
    dict1.update({k:v})
print(dict1)

dict3 = {**dict1, **dict2}
print(dict3)







# 3


sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


print(sampleDict['class']['student']['marks']['history'])





# 4
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

d = {}
for i in range(len(employees)):
    d.update({employees[i]:defaults})
print(d)

# actual way


res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])





# 5



sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

d={}
for i in keys:
    d[i] = sample_dict[i]

# second solution
newDict = {k: sample_dict[k] for k in keys}
print(newDict)

print(d)






# 6


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for i in keys:
    sample_dict.pop(i)
print(sample_dict)





# 7

sample_dict = {'a': 100, 'b': 200, 'c': 300}
s = 200
for i in sample_dict.values():
    if i == s:
        print(f'{s} is in a dict')




if 200 in sample_dict.values():
    print('200 present in a dict')


# 8

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict.update({'location':sample_dict.pop('city')})
print(sample_dict)
 

#  second way
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

# 9

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

min_val = min(sample_dict.values())
for k,v in sample_dict.items():
    if v == min_val:
        print(k)
    

    # second 

print(min(sample_dict, key=sample_dict.get))

# 10
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)







