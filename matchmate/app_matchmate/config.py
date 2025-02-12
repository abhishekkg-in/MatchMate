import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sports.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {'title': 'Sports API', 'uiversion': 3}



# print(os.path.abspath("sports.db"))
