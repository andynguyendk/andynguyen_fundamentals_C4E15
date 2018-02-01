from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds046867.mlab.com:46867/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()
# blog = db["blog"]
# new_post = {
#     'title': 'how to tune your carb',
#     'type': 'DIY',
#
# } 
# blog.insert_one(new_post)
games = db['games']
game_list = games.find()
for game in game_list:
    print(game['title'])
