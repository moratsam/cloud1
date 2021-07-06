import grpc
import json
import requests
from concurrent import futures

import kitchen_pb2_grpc
from kitchen_pb2 import (
	FromDictionary,
	SaladResponse,
)

class Kitchen(kitchen_pb2_grpc.KitchenServicer):
	def ServeSalad(self, request, context):
		if request.from_dictionary not in [FromDictionary.FALSE, FromDictionary.TRUE]:
			context.abort(grpc.StatusCode.NOT_FOUND, "FromDictionary enum not found")

		fromDict = "false" if request.from_dictionary == FromDictionary.FALSE else "true"
		postBody = {
			"deviceId": "c'est moi",
			"fromDictionary": fromDict,
			"saladSize": request.salad_size
		}
		response = requests.post(
			'https://yeo8m9d47l.execute-api.us-east-1.amazonaws.com/test',
			json=postBody
		)
		if response.status_code == 200:
			salad = json.loads((response.json()['body']))['wordSalad']
		else:
			salad = "There was an error in the word salad"
		return SaladResponse(word=salad)
			
def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=13))
	kitchen_pb2_grpc.add_KitchenServicer_to_server(
		Kitchen(), server
	)
	server.add_insecure_port("[::]:50051")
	server.start()
	server.wait_for_termination()

if __name__ == "__main__":
	serve()
