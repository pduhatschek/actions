class User:
    def __init__(self, sender_json):
        self.id         = sender_json['id']
        self.login      = sender_json["login"]
        self.html_url   = sender_json["html_url"]
        self.avatar_url = sender_json["avatar_url"]

        self.issues             = "issues" in sender_json and sender_json["issues"] or []
        self.issue_comments     = "issue_comments" in sender_json and sender_json["issue_comments"] or []

        self.discussions            = "discussions" in sender_json and sender_json["discussions"] or []
        self.discussion_comments    = "discussion_comments" in sender_json and sender_json["discussion_comments"] or []

        self.pull_requests          = "pull_requests" in sender_json and sender_json["pull_requests"] or []
        self.merged_pull_requests   = "merged_pull_requests" in sender_json and sender_json["merged_pull_requests"] or []
        self.pr_reviews             = "pr_reviews" in sender_json and sender_json["pr_reviews"] or []
        self.pr_review_comments     = "pr_review_comments" in sender_json and sender_json["pr_review_comments"] or []

        self.pushes     = "pushes" in sender_json and sender_json["pushes"] or 0
        self.gollums    = "gollums" in sender_json and sender_json["gollums"] or 0
        self.forks      = "forks" in sender_json and sender_json["forks"] or 0

        self.cooperation_xp             = "cooperation_xp" in sender_json and sender_json["cooperation_xp"] or 0
        self.communication_xp           = "communication_xp" in sender_json and sender_json["communication_xp"] or 0
        self.continuous_improvement_xp  = "continuous_improvement_xp" in sender_json and sender_json["continuous_improvement_xp"] or 0
        self.logic_xp                   = "logic_xp" in sender_json and sender_json["logic_xp"] or 0
        self.creativity_xp              = "creativity_xp" in sender_json and sender_json["creativity_xp"] or 0

        self.badges = "badges" in sender_json and sender_json["badges"] or []
        
def Issue(issue_json):
    data = {
        "id"             : issue_json['id'],
        "title"          : issue_json["title"],
        "body"           : issue_json["body"],
        "html_url"       : issue_json["html_url"],
        "number"         : issue_json["number"],
        "created_at"     : issue_json["created_at"]        
    }
    return data
        

def IssueComment(issue_comment_json):
    data= {
        "id"         : issue_comment_json['id'],
        "body"       : issue_comment_json["body"],
        "created_at" : issue_comment_json["created_at"],
        "html_url"   : issue_comment_json["html_url"]      
    }
    return data

        

def PullRequest(pull_request_json):
    data = {
        "id"         : pull_request_json['id'],
        "body"       : pull_request_json["body"],
        "title"      : pull_request_json["title"],
        "html_url"   : pull_request_json["html_url"],
        "created_at" : pull_request_json["created_at"],
        "merged"     : pull_request_json["merged"]
    }
    return data
        

def PR_Review(pr_review_json):
    data = {
        "id"             : pr_review_json['id'],
        "body"           : pr_review_json["body"],
        "html_url"       : pr_review_json["html_url"],
        "state"          : pr_review_json["state"],
        "submitted_at"   : pr_review_json["submitted_at"]     
    }
    return data
        

def PR_ReviewComment(pr_review_comment_json):
    data = {
        "id"         : pr_review_comment_json['id'],
        "body"       : pr_review_comment_json["body"],
        "html_url"   : pr_review_comment_json["html_url"],
        "created_at" : pr_review_comment_json["created_at"] 
    }
    return data
        
    

def Discussion(discussion_json):
    data = {
        "id"         : discussion_json['id'],
        "body"       : discussion_json["body"],
        "title"      : discussion_json["title"],
        "html_url"   : discussion_json["html_url"],
        "created_at" : discussion_json["created_at"]
    }
    return data
    

def DiscussionComment(discussion_comment_json):
    data = {
        "id"         : discussion_comment_json['id'],
        "body"       : discussion_comment_json["body"],     
        "html_url"   : discussion_comment_json["html_url"],
        "created_at" : discussion_comment_json["created_at"]
    }
    return data
        

def Badge(badge_json):
    """
    Categories: 
    cooperation, communication, continuous_improvement, logic, creativity
    """
    data = {
        "id"                 : badge_json['title'],
        "category"           : badge_json["category"],
        "title"              : badge_json["title"],
        "description"        : badge_json["description"],
        "google_icon"        : badge_json["google_icon"]
    }
    return data