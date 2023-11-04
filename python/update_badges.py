import json
from models.firebase import update_user
from models.models import User, Badge

def update_badges(user:User):
    with open("./python/badges.json", "r") as f:
        badge_data_list = json.load(f)
    
    for badge_data in badge_data_list:
        condition = eval(badge_data["condition"])
        if condition(user):
            user.badges.append(Badge(badge_data))
            update_user(user)