# -*- coding: utf-8 -*-

import os
import json

def store_event():
    """
    Armazena um evento em um arquivo JSON específico para o tipo de evento.

    Returns:
    None
    """

    # Obtém o tipo de evento a partir do GITHUB_CONTEXT
    github_context = json.loads(os.environ['GITHUB_CONTEXT'])
    event_type = github_context['event_type']

    # Verifica se o tipo de evento é válido
    valid_types = [
        'issues', 'pull_request', 'pull_request_review', 'pull_request_review_comment',
        'push', 'fork', 'gollum', 'issue_comment', 'discussion', 'discussion_comment'
    ]
    if event_type not in valid_types:
        raise ValueError(f"Tipo de evento inválido. Deve ser uma das seguintes opções: {', '.join(valid_types)}.")

    # Abre o arquivo JSON correspondente ao tipo de evento
    filename = f"data/{event_type}.json"
    with open(filename) as json_file:
        data = json.load(json_file)

    # Adiciona o evento à lista de eventos do arquivo
    data[event_type].append(github_context)

    # Salva as alterações no arquivo JSON
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

store_event()