def html_dict_search(html_dict, selector):
    if selector.startswith('.'):
        key = 'class'
    elif selector.startswith('#'):
        key = 'id'

    result = []

    def branch(data, key):
        if key in data['attrs']:
            if data['attrs'][key] == selector[1:]:
                result.append(data)

        for subset in data['children']:
            branch(subset, key)

    for data in html_dict['children']:
        branch(data, key)

    return result
