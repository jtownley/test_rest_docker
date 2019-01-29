**This is a work in progress**

h2. Usage
docker run jtownley/test_rest:latest --expose 8080 -e "PORT=8080"
curl http://localhost:8080


h2. Environment
PORT  - changes the port of the request  (default: 8080)


h2. Paths
'/' 			- A welcome page
'/200' 			- A 200 response
'/201'			- A 201 response
'/404'			- A 404 response
'/500'			- A 500 response 

/***/json 		- a response in json where applicable