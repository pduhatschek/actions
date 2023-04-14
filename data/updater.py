import os
import json

def update_user(user, event_name, event_action):
    data_file_path = f'data/{event_name}.json'
    if os.path.isfile(data_file_path):
        with open(data_file_path) as json_file:
            data = json.load(json_file)
    else:
        data = {}

    if 'events' not in user:
        user['events'] = {}

    if event_name not in user['events']:
        user['events'][event_name] = {}

    if event_action not in user['events'][event_name]:
        user['events'][event_name][event_action] = 0

    temp = data[event_action]
    
    user['events'][event_name][event_action] = 0
    for event in temp:
        if user['id'] == event['sender']['id']:
            user['events'][event_name][event_action] += 1

    return user

def update_users():
    with open('act-frontend/src/users.json') as json_users:
        users = json.load(json_users)

        event_action = os.environ['GITHUB_EVENT_ACTION']
        event_name = os.environ['GITHUB_EVENT_NAME']

        
        with open(f'data/{event_name}.json') as json_file:
            data = json.load(json_file)
            for event in data[event_action]:
                user_exists = False
                for user in users['users']:
                    if user['id'] == event['sender']['id']:
                        user_exists = True
                        update_user(user, event_name, event_action)
                        break
                if not user_exists:
                    new_user = {
                        "id": event['sender']['id'],
                        "login": event['sender']['login'],
                        "avatar_url": event['sender']['avatar_url'],
                        "html_url": event['sender']['html_url'],
                        "events": {
                            event_name: {
                                event_action : 1
                            }
                        }
                    }
                    users['users'].append(new_user)
                    
        with open('act-frontend/src/users.json', 'w') as js:
            json.dump(users, js, indent=4)

update_users()
