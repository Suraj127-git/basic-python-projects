from pymongo import MongoClient
MONGO_URI = "mongodb+srv://doadmin:d1l9n6tT40J3a52B@db-mongodb-blr1-02533-baeb9ef6.mongo.ondigitalocean.com/admin?tlsAllowInvalidCertificates=true&authSource=admin"
conn = MongoClient(MONGO_URI)