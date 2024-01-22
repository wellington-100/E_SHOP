


-----------------------------------------------------------------------------------------------------------



            +------------------+
            |                  |
            |     Order        | ---------------------------------------------------+
            | id - primary key |                                                    | 
            |                  |                                                    | 
            +------------------+                                                    |
                |                                                                   |
                |                                                                   |
                |          +---------------+                                        |
                +----------| OrderItem #1  |                                        |
                |          +---------------+                                        |
                |               |                                                   |
                |               |                                                   |
                |               +------ id "primary key"          +------------+    |
                |               |                                 |            |    |
                |               +------ product "OneToOneField" <---> Product  |    |
                |               |                                 |            |    |
                |               +------ quantity                  +------------+    |
                |               |                                                   |
                |               +------ order "ForeignKey" <------------------------+
                |
                +---------- OrderItem #2
                |               |
                |               +------ .......


  
------------------------------------------------------------------------------------------------------------
- **Order**: 
  - Primary model.
  - Has a primary key "id".

- **OrderItem**: 
  - Associated with "Order" via "ForeignKey".
  - Associated with "Product" via "OneToOneField".

- **Product**: 
  - Independent model, but referenced by "OrderItem".

