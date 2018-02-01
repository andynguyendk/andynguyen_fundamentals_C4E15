from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()

post = db["posts"]
new_post = {
    'title': 'Ngày không em',
    'author': 'Andy',
    'content': 'Ngày không em (M) thì vẫn là ngày. Còn ngày không en (N) thì chỉ còn là gày thôi. Nói chung là ngày có em thì mới chả biết là nhét vào chỗ nào, chứ ngày ko có em thì hoàn toàn bình thường'

}
post.insert_one(new_post)


# blog = db["blog"]
# new_post = {
#     'title': 'how to tune your carb',
#     'type': 'DIY',
#
# }
# blog.insert_one(new_post)
