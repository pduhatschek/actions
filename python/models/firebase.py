import os
import json
from .models import *
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

if os.path.exists('keys.json'):
    cred = credentials.Certificate('keys.json')
else:
    cred = credentials.Certificate(json.loads(os.environ['FS_KEY']))

app = firebase_admin.initialize_app(cred)
_db: firestore.firestore.Client = firestore.client()


def get_action_info(action_type):
    with open('points.json', 'r') as file:
        data = json.load(file)
        return data.get(action_type, {})


def update_user(user: User):
    ref = _db.document(f"users/{user.id}")
    ref.set(user.__dict__)


def add_action(user: User, data: dict, action_type: str):
    # Adiciona "es" ao final para "add_push" e "s" para outros casos
    user_actions_attr = f"{action_type}es" if action_type == "add_push" else f"{action_type}s"

    user_actions = getattr(user, user_actions_attr)
    user_actions.append(getattr(ActionTypes, action_type.capitalize())(data[action_type]))

    action_info = get_action_info(action_type)

    # Atualiza as xp_bars com base nas informações do JSON
    for competency in action_info.get("competencies", []):
        xp_points = action_info.get("points", {}).get(competency, 0)
        setattr(user, f"{competency}_xp", getattr(user, f"{competency}_xp") + xp_points)

    update_user(user)


def add_issue(user: User, data: dict):
    add_action(user, data, "add_issue")


def add_issue_comment(user: User, data: dict):
    add_action(user, data, "add_issue_comment")


def add_pull_request(user: User, data: dict):
    add_action(user, data, "add_pull_request")


def add_pull_request_review(user: User, data: dict):
    add_action(user, data, "add_pull_request_review")


def add_pull_request_review_comment(user: User, data: dict):
    add_action(user, data, "add_pull_request_review_comment")


def add_discussion(user: User, data: dict):
    add_action(user, data, "add_discussion")


def add_discussion_comment(user: User, data: dict):
    add_action(user, data, "add_discussion_comment")


def add_push(user: User, *kwargs):
    add_action(user, {}, "add_push")


def add_gollum(user: User, *kwargs):
    add_action(user, {}, "add_gollum")


def add_fork(user: User, *kwargs):
    add_action(user, {}, "add_fork")


def user_checkin(sender):
    user = _db.collection('users').document(str(sender["id"])).get()
    if user.exists:
        return User(user.to_dict())
    else:
        user = User(sender)
        ref = _db.collection('users').document(f"{user.id}")
        ref.set(user.__dict__)
    return user
