import os
import json
import models.firebase as firebase
from update_badges import update_badges
from update_challenges import update_challenges

if __name__ == "__main__":
    # Obtém o contexto do GitHub
    data = json.loads(os.environ['GITHUB_CONTEXT'])

    # Obtém o tipo de evento a partir do nome do evento
    event = os.environ['GITHUB_EVENT_NAME']

    actions = {
        'issues': firebase.add_issue,
        'issue_comment': firebase.add_issue_comment,

        'discussion':  firebase.add_discussion,
        'discussion_comment': firebase.add_discussion_comment,

        'pull_request': firebase.add_pull_request,
        'pull_request_review': firebase.add_pull_request_review, 
        'pull_request_review_comment': firebase.add_pull_request_review_comment,

        'push': firebase.add_push,
        'fork': firebase.add_fork,
        'gollum': firebase.add_gollum,
    }

    # faz o checkin do usuario no sistema
    user = firebase.user_checkin(data["sender"])

    # chama a função respectiva de cada action
    actions[event](user, data)

    # checa se o usuário ganhou alguma badge
    update_badges(user)
    update_challenges(user)