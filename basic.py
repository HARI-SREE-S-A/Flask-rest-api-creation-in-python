from flask import Flask

app = Flask(__name__)


stores = [{"name": "my store",
           "items": [
               {
                   "name": "chair",
                   "price": "223"

               }
           ]
           }
          ]


@app.get("/store")
def get_store():
    return {"stores": stores}

