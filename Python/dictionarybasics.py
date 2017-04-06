bio = {
    'info': [
    {'id': 'name', 'content':'Harry Potter'},
    {'id': 'age', 'content': 12},
    {'id': 'country of birth', 'content':'UK'},
    {'id': 'favorite language', 'content':'Parser-Tongue'}
  ]
}

for key, data in bio.items():
    for value in data:
        print "My", value['id'], "is", value['content']
