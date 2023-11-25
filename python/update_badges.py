import json
from models.firebase import update_user
from models.models import User, Badge

def has_badge(user, badge):
    titles = [b["title"] for b in user.badges]
    return badge["title"] in titles

def update_badges(user:User):
    with open("./python/badges.json", "r") as f:
        badge_data_list = json.load(f)
    
    for badge_data in badge_data_list:
        condition = eval(badge_data["condition"])
        if condition(user):
            if not has_badge(user, badge_data):
                user.badges.append(Badge(badge_data))
                update_user(user)
