import requests 

headers = {
        "Authorization":"Token c533bf936363b0160bead443b779d9b47073e127"
    }


def log_in():
    endpoint = 'http://127.0.0.1:8000/log-in'
    response = requests.post(endpoint, json={"username":"aceri5", "password":"123helloworld"})
    print(response.json())



def list_product():
    endpoint = 'http://127.0.0.1:8000/products'
    response = requests.get(endpoint, headers=headers)
    print(response.json())

#list_product()
def sign_up():

    endpoint = 'http://127.0.0.1:8000/register'
    
    response = requests.post(endpoint, json={"username":"boburmirzo", "password":"123helloworld"})

    print(response.json())

#sign_up()

def add_product():
    endpoint = 'http://127.0.0.1:8000/add-products'
    
    resposne = requests.post(endpoint, json={"title":"Mouse", "price":12.00, "number":3}, headers=headers)
    print(resposne.json())

#add_product()

    
def like():
    endpoint = 'http://127.0.0.1:8000/like/3'
    response = requests.post(endpoint, json={"liked":False}, headers=headers)
    print(response.json())
#like()

def detail():
    endpoint = 'http://127.0.0.1:8000/products/1'
    response = requests.api.get(endpoint, headers=headers)
    print(response.json())

detail()


def comment():
    endpoint = 'http://127.0.0.1:8000/comment/2'
    response = requests.post(endpoint, json={'comment':"This product is amazing!!!"}, headers=headers)
    print(response.json())

#comment()
    
def most_liked():
    endpoint = 'http://127.0.0.1:8000/most-liked'
    response = requests.get(endpoint, headers=headers)
    print(response.json())

# most_liked()

def add_to_cart() -> None:
    endpoint = 'http://127.0.0.1:8000/cart/7'
    response = requests.post(endpoint, headers=headers)
    print(response.json())
#add_to_cart()

def token():
    endpoint = 'http://127.0.0.1:8000/obtain-token'
    response = requests.post(endpoint, json={"username":"test", "password":"JbVK72$G4dXi5Wh"})
    print(response.json())

def remove_from_cart():
    endpoint = 'http://127.0.0.1:8000/cart/7'
    response = requests.delete(endpoint, headers=headers)
    print(response.json())
#remove_from_cart()
def get_liked_products():
    endpoint = 'http://127.0.0.1:8000/your-liked-products'
    response = requests.get(endpoint, headers=headers)
    print(response.json())
#get_liked_products()
    
def cartItems():
    endpoint = 'http://127.0.0.1:8000/cart-items'
    response = requests.get(endpoint, headers=headers)
    print(response.json())

#cartItems()
    
def order():
    endpoint = 'http://127.0.0.1:8000/orders'
    response = requests.get(endpoint, headers=headers)
    print(response.json())

