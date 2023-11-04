# -*- coding: utf-8 -*-

import os
import json

def write_json(data, filename='data/issue_comment.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

novo_evento = json.loads(os.environ['GITHUB_CONTEXT'])
print(novo_evento)

with open('data/issue_comment.json') as json_file:
    data = json.load(json_file)
    temp = data['issue_comment']
    temp.append(novo_evento)
write_json(data)