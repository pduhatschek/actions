import os
import json

def update_user(user, event_type):
    with open(f'data/{event_type}.json') as json_file:
        data = json.load(json_file)
        temp = data[event_type]
        user['events'][event_type] = 0
        for event in temp:
            if user['id'] == event['sender']['id']:
                user['events'][event_type] += 1
        return user

def update_users():
    with open('data/users.json') as json_users:
        users = json.load(json_users)
        for event_type in ['issues', 'issue_comment', 'pull_request', 'pull_request_review', 'pull_request_review_comment', 'push', 'fork', 'gollum', 'discussion', 'discussion_comment']:
            with open(f'data/{event_type}.json') as json_file:
                data = json.load(json_file)
                for event in data[event_type]:
                    user_exists = False
                    for user in users['users']:
                        if user['id'] == event['sender']['id']:
                            user_exists = True
                            update_user(user, event_type)
                            break
                    if not user_exists:
                        new_user = {
                            "id": event['sender']['id'],
                            "login": event['sender']['login'],
                            "avatar_url": event['sender']['avatar_url'],
                            "html_url": event['sender']['html_url'],
                            "events": {
                                event_type: 1
                            }
                        }
                        users['users'].append(new_user)
        with open('data/users.json', 'w') as js:
            json.dump(users, js, indent=4)

update_users()
