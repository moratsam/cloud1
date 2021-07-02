import grpc
from concurrent import futures
from random_word import RandomWords

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
		r = RandomWords()
		salad = r.get_random_words(hasDictionaryDef=fromDict, limit=request.salad_size)

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
