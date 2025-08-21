from pymongo import MongoClient

uri = "mongodb+srv://amanregmi10:Aman1029.@cluster0.cynppay.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["sample_mflix"]
movies = db["movies"]
movies.insert_one({"title": "Back to the Future", "year": 1985})
movie = movies.find_one({"title": "Back to the Future"})
print(movie)


