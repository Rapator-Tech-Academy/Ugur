import os
from flask import Flask, url_for, json


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static/data", "students.json")

class Repository:
    def persist_instance(self, payload):
        with open(json_url, 'r') as file:
            data = json.load(file)
            data.append(payload)

        with open(json_url, 'w') as file:
            file.write(json.dumps(data))

class DeletingRepoData:
    def check_user(self, id):
        index = 0
        with open(json_url, 'r') as file:
            data = json.load(file)
            for i in data:
                if id in i:
                    return index
                index += 1
    
    def delete_data(self, outputdata):
        with open(json_url, 'r') as file:
            data = json.load(file)
            data.pop(outputdata)
        with open(json_url, 'w') as file:
            file.write(json.dumps(data))

        

    

