from flask import Flask
from flask_restful import Api
from book_service import Test



app = Flask(__name__)
api = Api(app)


api.add_resource(Test,
                 '/test'
                )               

if __name__ == "__main__":
    app.run(port = 5000, debug =True)
   