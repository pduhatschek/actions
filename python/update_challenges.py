import json
from models.firebase import update_user
from models.models import User

def update_challenges(user: User):
    is_winner = (
        user.forks > 0
        and user.pushes > 0
        and user.pull_requests > 0
        and user.pr_review_comments > 0
        and user.pull_requests_merged > 0
        and user.pr_review_comments > 0
        and user.pull_requests_merged > 0
    )

    if is_winner:
        user.winner = True
        update_user(user)

