from flask import Flask,request

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
@app.post("/store")
def update_store():
    req_data = request.get_json()
    new = {"name":req_data,"items":[]}
    stores.append(new)
    return new,201

