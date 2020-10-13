import json

class Repository:
    def persist_instance(self, payload):
        with open('students.json', 'r') as file:
            data = json.load(file)
            data.append(payload)

        with open('students.json', 'w') as file:
            file.write(json.dumps(data))

class DeletingRepoData:
    def check_user(self, id):
        index = 0
        with open('students.json', 'r') as file:
            data = json.load(file)
            for i in data:
                if id in i:
                    return index
                index += 1
    
    def delete_data(self, outputdata):
        with open('students.json', 'r') as file:
            data = json.load(file)
            data.pop(outputdata)
        with open('students.json', 'w') as file:
            file.write(json.dumps(data))

        

    

