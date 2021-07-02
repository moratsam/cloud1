# Cloud1
There are 2 microservices: bistro and kitchen.
Kitchen serves a word salad of randomly generated words via grpc.
Bistro gets a word salad from (the) kitchen and displays it by leveraging Flask (port 5000).
