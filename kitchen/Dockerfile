from python

RUN mkdir /app
COPY proto/ /app/proto
COPY kitchen/ /app/kitchen
WORKDIR /app/kitchen
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../proto --python_out=. \
						--grpc_python_out=. ../proto/kitchen.proto

EXPOSE 50051
ENTRYPOINT ["python", "kitchen.py"]
