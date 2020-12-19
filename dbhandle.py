import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://roman:pas123@cluster0.oxndg.mongodb.net/mydb?retryWrites=true&w=majority')