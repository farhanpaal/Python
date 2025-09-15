from util.mongo import Mongo

mongo=Mongo("Podcast","Motivation")


# print(mongo.insert({
#     "name":"paal Lust",
#     "speaker":"jabran",
#     "category":"self help"
# })) #here we will insert data in the form of dictionary

# print(mongo.fetchAll({
#     "category":"romance"
# })) #here we will insert data in the form of dictionary
print(mongo.fetchAll({},1))

# fetch by id
# print(mongo.fetchById('68c7fc1b642eb9e954347fe3'))

# Update: two arguments
# print(mongo.update("68c7cd699e081beca3e10c17",{
#     'category':'conquer world',
#     'speaker':'legend himself'
# }))

# delete
# print(mongo.delete("68c7cb966c9713774cd6a605"))