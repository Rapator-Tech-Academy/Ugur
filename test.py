import json

id='4967'


def check_user(id):
    index = 0
    with open('students.json', 'r') as file:
        data = json.load(file)
        for i in data:
            if id in i:
                return index
            index += 1
            

result = check_user(id=id)

if result == None:
    print("fuck")

else:
    with open('students.json', 'r') as file:
        data = json.load(file)
        data.pop(result)
    with open('students.json', 'w') as file:
        file.write(json.dumps(data))
