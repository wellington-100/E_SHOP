## DJANGO DRF + (frontend?) / ESHOP
    > idea
    1. main.page -> product
        1.1. discount + countdown
        1.2. order product
        1.3. auth
        1.4. send automatic emails
        1.5. stripe payment link
        1.6. subscription
        1.7. admin
        1.8. api Chat GPT (bot support)
    
    > tech
    1. DRF
        > urls
        > views
        > serializers
        > models
        > auth
        > pagination

    2. ORM
        > ?

    3. DB
        > postgresql

    4. DOCKER
        > containers

    5. FRONTEND
        > HTML + CSS + JS

    6. GIT
        > cli

-------------------------------------------------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------------------------------------------------
REST (Representational State Transfer), API (Application Programming Interface), JSON


                                                APP

        GET, POST               /admin/products  <---->  ProductAdminView
                                    |                                 ^         + actions
                                    |                                 |         + model
                                    |   endpoint (urls)               |         + fields: id, name, image, description 
                                    |    /                            +---- +       |
                                    |   /                                   v       v
        GET request             /products   <-->    ProductView    <-->   ProductSerializer   <-->  Product (resource)
                                    |                   ^                           ^                   ^
                                    |                   |                           |                   |
                                    |           ListAPIView (views)         ModelSerializer             +---> Money
                                    |
                                    |                                    
-------------------------------------------------------------------------------------------------------------------------------


                                                                            image: postgres: postgres:15.4-alpine3.18
                                                                                    |
                                                                                    |
                                                                eshop_db            |
                                                                    |               |
docker-compose up ------> create and run containers ------> +-------+---------------v------(container)------+
    ^                                                       |
    |                                                       |       +---------------(postgresql)
    |                                                       |       |
    |                                                       |       |
    |                                                       |       |
    |                              app (django) <------>   5777 :  5432  <----->                  
    |                                                       |       |
    |                                                       |       |
    |                                           /data <------------------------>    /var/lib/postgresql/data
    |                                                       |       |
  config
    |
docker-compose.yml

-------------------------------------------------------------------------------------------------------------------------------


app |
    |
    +---models.py
            |
            +----- class Product
            |
            +----- Class Money


app |
    |
    +---models.py
           |
        __init__.py <--- import ------------+
           |                                |
           +--- Product.py                  |
           |         |                      |
           |         +--- class Product ----+
           |                                |
           +--- Money.py                    |
                  |                         |   
                  +------ class Money ------+


-------------------------------------------------------------------------------------------------------------------------------


Product
   v
   v                    OneToOneField (bidirectional)
   v                            v
   price_standard = .. --------------------> Money
                                               |
       <---------- price_standard_reverse------+

   price_dicount = .. ---------------------> Money
                                               |
       <----------  price_dicount_reverse------+


-------------------------------------------------------------------------------------------------------------------------------
                                                                        |
                                                                        |
                                +---------------------------------- / <-----> indexPage() <--> templates/public/index.html
                                |                                       |
                                |                                       |
                                |                                       |
                                v                                       |
                    CLIENT (HTML, CSS, JS, ...)                         |                     API (drf, postgresql....)
                                                                        | 
                                                                        |
            +-----------------------------------------+                 |
            |                                         |                 |
            |                                         | <------> GET  /products <--> ProductView <--> Product <---------> postgresql
            |                                         |                 |                                 |
            |               PRODUCT                   |                 |                                 +---- Money
            |                                         |                 |
            |            PRESENTATIONS                |                 |
            |                                         |                 |
            |                                         |                 |
            |  (name, image, description, price ..)   |                 |
            |                                         |                 |
            |                                         |                 |
            |                                         |                 |
            |                                         |                 |
            |                                         |                 |
            +-----------------------------------------+                 |
                                                                        |
                                                                        |
            +-----------------------------------------+                 |
            |                                         |                 |
            |                                         | <------> POST /orders/<uuid:id> <--> CreateOrderView <--------------->   post(...)
            |                                         |                 |       ^                          +-------------                      
            |             PRODUCT ACTIONS             |   product uuid ---------+                          |                    create(...)
            |                                         |                 |                                  |                        
            |           (order, dicount, ...)         |                 |                                  +------------->     perform_create()
            |                                         |                 |                                                          |
            |                                         |                 |                                                          |
            +-----------------------------------------+                 |                                                       Order <--> pg
                                                    


-------------------------------------------------------------------------------------------------------------------------------
 
 
      BROWSER
         |
      window  <---- GET / <---- index.html
         |
         +--- <---- GET /static/public.css
         |
         +--- <---- GET /static/public.js
         |
         |
+------> +-- function loadProduct () {
|         |
|         xhr = new XMLHttpRequest()
|         |
|         xhr.open("GET", "/products")
|         |
|         xhr.onload = function () {
|           response = xhr.responseText --------------------- response JSON [...] / string
|           data = JSON.parse(response)
|           console.log(data)***
|         }
|         |
|         xhr.send() ---------------------------------------> GET /products --->...
|       }
|
+-------- loadProduct ()

-------------------------------------------------------------------------------------------------------------------------------




Order
  |
  +---------- OrderItem #1
  |               |
  |               +------ id
  |               |
  |               +------ product --> Product
  |               |
  |               +------ quantity
  |               |
  |               +------ order --> Order
  |
  +---------- OrderItem #2
  |               |
  |               +------ .......


  
-------------------------------------------------------------------------------------------------------------------------------


HW: get to this point, draw diagrams:
    1. call stack
    2. db relationships: Order, OrderItem, Product