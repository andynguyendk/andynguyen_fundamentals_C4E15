from pymongo import MongoClient
import pprint
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()

customers = db["customers"]
ref_dict = {}
for customer in customers.find():
    if customer["ref"] in ref_dict:
        ref_dict[customer["ref"]] +=1
    else:
        ref_dict[customer["ref"]] = 0
#print(ref_dict)

from matplotlib import pyplot

labels = []
values = []
for i in ref_dict:
    labels.append(i)
    values.append(ref_dict[i])
    # print(labels)
    # print(values)

# colors = ['red', 'cyan', 'green']
# explode = [0, 0.1, 0, 0.1]
#plot
pyplot.pie(values, labels=labels)
pyplot.axis('equal')
pyplot.show()
