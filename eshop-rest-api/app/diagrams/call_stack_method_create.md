
The call stack for the "create" method in the CreateOrderView


1. **Start:** create(request, *args, **kwargs)
   - Initial call to "create" method.

2. **Serializer Initialization**
   - get_serializer(data=request.data)

   - Call Stack: 
     
     create
     |-- get_serializer
     

3. **Serializer Validation**
   - serializer.is_valid(raise_exception=True)

   - Call Stack: 
     
     create
     |-- get_serializer
     |-- serializer.is_valid
     

4. **Saving the Order**
   - perform_create(serializer)

   - Call Stack: 
   
     create
     |-- get_serializer
     |-- serializer.is_valid
     |-- perform_create
     

5. **Creating OrderItem**
   - Extract product_id from kwargs.
   - Find Product: Product.objects.get(pk=product_id)
   - Find Order: Order.objects.get(pk=serializer.data.get('id'))
   - Save OrderItem: OrderItem(product=..., order=...).save()

   - Call Stack: 
     
     create
     |-- get_serializer
     |-- serializer.is_valid
     |-- perform_create
     |-- Product.objects.get
     |-- Order.objects.get
     |-- OrderItem().save
     

6. **Success Headers and Response**
   - get_success_headers(serializer.data)
   - Response(serializer.data, status=...)


   - Call Stack: 
   
     create
     |-- get_serializer
     |-- serializer.is_valid
     |-- perform_create
     |-- Product.objects.get
     |-- Order.objects.get
     |-- OrderItem().save
     |-- get_success_headers
     |-- Response
     