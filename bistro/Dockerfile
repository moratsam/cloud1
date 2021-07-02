from python

RUN mkdir /app
COPY proto/ /app/proto
COPY bistro/ /app/bistro
WORKDIR /app/bistro
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../proto --python_out=. \
						--grpc_python_out=. ../proto/kitchen.proto

EXPOSE 5000
ENV FLASK_APP=bistro.py
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
