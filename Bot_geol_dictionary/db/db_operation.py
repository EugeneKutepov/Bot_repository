import json

with open('db/db_users.json') as file:
    db_dict = json.load(file)

def db_launch():
    file = 'db_users.json'
    db = {'users_id':[]}
    with open(file, 'w') as f:
        json.dump(db, f)

def db_proc(id:int):
    if id not in db_dict['users_id']:
        db_dict['users_id'].append(id)
        with open('db/db_users.json', 'w') as f:
            json.dump(db_dict, f)

def db_loock():
    print(len(db_dict['users_id']))



if __name__ == '__main__':
    db_loock()