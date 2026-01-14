import json

data ={
    "name": "Rahul",
    "age": 25,
    "skills": ["Python", "C/C++"]
}

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)