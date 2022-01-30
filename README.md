# Cloud1
There are 2 microservices: bistro and kitchen.
The Kitchen generates a word salad of randomly generated words and serves it via grpc.
The Bistro gets a word salad from (the) Kitchen and displays it by leveraging Flask (port 5000).

bistro --grpc--> kitchen

# Branch aws
Use the k8s.yml from branch aws to deploy an extension of the service, where (the) Kitchen is outsourced.
The word salad is generated in aws lambda (and it also gets stored in dynamoDB because wasting resources is always a good idea).

bistro --grpc--> kitchen --POST--> aws API gateway --> layered lambda --> dynamoDB
