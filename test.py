import requests
import  json
BASE_URI='http://127.0.0.1:8000/'
ENDPOINT='api/'

def get_resource(id=None):
    data={}
    if id is not None:
        data={
            'id':id
        }
    resp=requests.get(BASE_URI+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())



def create_resource():
    data={
        'eno':999,
        'ename':'Bahubali',
        'esal':457845.5754,
        'eaddr':"Mahismati"
    }
    resp=requests.post(BASE_URI+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

def update_resource(id):
    data={
        'id':id,
        'ename':'Sunny',
        'esal':50009
    }
    resp=requests.put(BASE_URI+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
update_resource(4)

def delete_resource(id):
    data={
        'id':id
    }
    resp=requests.delete(BASE_URI+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

