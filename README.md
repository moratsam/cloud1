# Cloud1
There are 2 microservices: bistro and kitchen.
Kitchen generates and serves a word salad of randomly generated words via grpc.
Bistro gets a word salad from (the) kitchen and displays it by leveraging Flask (port 5000).

bistro --grpc--> kitchen

# branch aws
use the k8s.yml from branch aws to deploy an extension of the service, where the kitchen is also outsourced.
The word salad is generated in aws lambda (and it is also gets stored in dynamoDB because wasting resources is always a good idea).

bistro --grpc--> kitchen --POST--> aws API gateway --> layered lambda --> dynamoDB 
