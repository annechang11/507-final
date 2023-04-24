'''The tomato "tree" to be input to the interaction program
tomatoes are selected from the json file'''

import json

with open('tomato_data.json', 'r') as f:
  data = json.load(f)

# manually select 1 tomato for each color*size combination. also link an image

for tomato in data:
    if tomato['Name'] == 'Campari': # red, small
        campari = (tomato['Name'], tomato, './images/campari.jpg')  
    if tomato['Name'] == 'Roma': # red, medium
        roma = (tomato['Name'], tomato, './images/roma.jpg') 
    if tomato['Name'] == 'Beefsteak': # red, large
        beefsteak = (tomato['Name'], tomato, './images/beefsteak.jpg')
    if tomato['Name'] == 'Yellow Pear': # yellow, small
        yellowpear = (tomato['Name'], tomato, './images/yellowpear.jpg')
    if tomato['Name'] == "Jubilee": # yellow, medium
        jubilee = (tomato['Name'], tomato, './images/jubilee.jpeg')
    if tomato['Name'] == "Kellogg's Breakfast": # yellow, large
        kellogg = (tomato['Name'], tomato, './images/kelloggs_breakfast.jpg') 
    if tomato['Name'] == "Kumato": # purple, small
        kumato = (tomato['Name'], tomato, './images/kumato.jpg') 
    if tomato['Name'] == "Paul Robeson": # purple, medium
        paul = (tomato['Name'], tomato, './images/paul.jpeg')  
    if tomato['Name'] == "Cherokee Purple": # purple, large
        cherokee = (tomato['Name'], tomato, './images/cherokee_purple.jpg') 

# construct a tree

tree = (
    None,
    ('Red', ('Small',campari), ('Medium', roma), ('Large', beefsteak)),
    ('Yellow', ('Small',yellowpear), ('Medium', jubilee), ('Large', kellogg)),
    ('Purple', ('Small',kumato), ('Medium', paul), ('Large', cherokee))
)