import grpc
from flask import Flask, render_template
import logging
import os

from kitchen_pb2 import (
	FromDictionary,
	SaladRequest
)
from kitchen_pb2_grpc import KitchenStub

app = Flask(__name__)

#in case env var is not set, default to localhost
kitchen_host = os.getenv("KITCHEN_HOST", "127.0.0.1")
kitchen_channel = grpc.insecure_channel(f"{kitchen_host}:50051")
kitchen_client = KitchenStub(kitchen_channel)

@app.route("/")
def render_index():
	salad_request = SaladRequest(
		from_dictionary=FromDictionary.TRUE, salad_size=13
	)
	try:
		kitchen_response = kitchen_client.ServeSalad(salad_request)
		print(kitchen_response.word)

		return render_template(
			"index.html",
			word_salad=kitchen_response.word,

		)
	except:
		logging.exception('')
		return render_template("error.html", addrport=kitchen_host)
	

