from flask import Flask 

app = Flask(__name__)

stores =[
    {
        "name":"My Wonderful Store",
        "items":[
            {
                "name":"My Item",
                "price":15.99
            }
        ]
    }
]
@app.route('/')
def home():
    return "API made with Flask"

@app.get('/store')
def get_stores():
    return {"stores":stores}

if __name__ == '__main__':
    app.run()