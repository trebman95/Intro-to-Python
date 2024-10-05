"""
Create a basic dictionary that contains the following information about
an imaginary person:

- Their name
- Their age
- Their location (city, state). Bonus points if you use a
  nested dictionary.
- Whether they’re married or not.
"""
person = {
    'name': 'Tre',
    'age':29,
    'location':{
        'city':'Charlotte',
        'state':'NC'
    },
    'is_married': False
}

print(person)