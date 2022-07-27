# Restful API design
Aim:
This API able to attach with any type of application and this will API will work on the standard mechanism whereby the client and the web service of the data to exchange.

REST APIs are designed around resources, which are any kind of object, data, or service that can be accessed by the client.

## Input
This application after the attachment with the mainframe of the application it will take the input from the user of 2 things and the whole data exhcange service of the application is based on these two cases.<br>
1.The first input file which this API fetches is the Job description
<!-- ![alt text](http://url/to/img.png) -->

Our application will firstly send an Indentifier 

**HTTP**
```https://ai-dawn-data.com/parser/1```

Clients interact with a service by exchanging represantations of resources. Many web APIs use JSON as the exchange format . For example, a GET request to the URL listed above might return this response body:

**JSON** response
```{"orderId":1,"orderValue":99.90,"productId":1,"Scoring":1,"confidence" :94}```


# CRUD
 Many operation all also can be done in this API such as:
1.REST APIs use a uniform interface, which helps to decouple the client and service implementations. For REST APIs built on HTTP, the uniform interface includes using standard HTTP verbs to perform operations on resources. The most common operations are GET, POST, PUT, PATCH, and DELETE.

# Organize the API design around resources

Focus on the business entities that the web API exposes. In this application primary important things are **scoring and Resumes**. Creating an order can be achieved by sending an HTTP POST request that contains the order information. The HTTP response indicates whether the order was placed successfully or not. When possible, resource URIs should be based on nouns (the resource) and not verbs (the operations on the resource).
```
https://ai-works.com/dawn// Good

https://ai-works.com/dawn // Avoid ```


