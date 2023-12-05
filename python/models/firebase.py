import os
import json
from .models import *
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

if (os.path.exists('keys.json')):
    cred = credentials.Certificate('keys.json')
else:
    cred = credentials.Certificate(json.loads(os.environ['FS_KEY']))

app = firebase_admin.initialize_app(cred)
_db:firestore.firestore.Client = firestore.client()

with open("./python/xp.json", "r") as f:
    xp_map = json.load(f)

def update_user(user:User):
    ref = _db.document(f"users/{user.id}")
    ref.set(user.__dict__)

def add_issue(user:User, data:dict):
    user.issues.append(Issue(data["issue"]))

    # add xp to respective xp
    for k in xp_map["issue"]:
        user.__dict__[k] += xp_map["issue"][k]

    update_user(user)


def add_issue_comment(user:User, data:dict):
    user.issue_comments.append(IssueComment(data["comment"]))

    # add xp to respective xp
    for k in xp_map["issue_comment"]:
        user.__dict__[k] += xp_map["issue_comment"][k]

    update_user(user)

def add_pull_request(user:User, data:dict):
    if data["pull_request"]["merged"] == False:
        user.pull_requests.append(PullRequest(data["pull_request"]))

        # add xp to respective xp
        for k in xp_map["pull_request"]:
            user.__dict__[k] += xp_map["pull_request"][k]

        update_user(user)
    else:
        add_pull_request_merged(user, data)

def add_pull_request_merged(user:User, data:dict):
    if data["pull_request"]["merged"] == True:
        user.pull_requests_merged.append(PullRequestMerged(data["pull_request"]))

        # add xp to respective xp
        for k in xp_map["pull_request_merged"]:
            user.__dict__[k] += xp_map["pull_request_merged"][k]

        update_user(user)

def add_pull_request_review(user:User, data:dict):
    user.pr_reviews.append(PR_Review(data["review"]))

    # add xp to respective xp
    for k in xp_map["pull_request_review"]:
        user.__dict__[k] += xp_map["pull_request_review"][k]

    update_user(user)

def add_pull_request_review_comment(user:User, data:dict):
    user.pr_review_comments.append(PR_ReviewComment(data["comment"]))
    
    # add xp to respective xp
    for k in xp_map["pull_request_review_comment"]:
        user.__dict__[k] += xp_map["pull_request_review_comment"][k]

    update_user(user)

def add_discussion(user:User, data:dict):
    user.discussions.append(Discussion(data["discussion"]))

    # add xp to respective xp
    for k in xp_map["discussion"]:
        user.__dict__[k] += xp_map["discussion"][k]

    update_user(user)

def add_discussion_comment(user:User, data:dict):
    user.discussion_comments.append(DiscussionComment(data["comment"]))

    # add xp to respective xp
    for k in xp_map["discussion_comment"]:
        user.__dict__[k] += xp_map["discussion_comment"][k]

    update_user(user)

def add_push(user:User, *kwargs):
    user.pushes +=1

    # add xp to respective xp
    for k in xp_map["push"]:
        user.__dict__[k] += xp_map["push"][k]

    update_user(user)

def add_gollum(user:User, *kwargs):
    user.gollums += 1

    # add xp to respective xp
    for k in xp_map["gollum"]:
        user.__dict__[k] += xp_map["gollum"][k]

    update_user(user)

def add_fork(user:User, *kwargs):
    user.forks += 1
    update_user(user)

def user_checkin(sender):
    user = _db.collection('users').document(str(sender["id"])).get()
    if user.exists:
        return User(user.to_dict())
    else:
        user = User(sender)
        ref = _db.collection('users').document(f"{user.id}")
        ref.set(user.__dict__)
    return user