#!/bin/bash
python -m grpc_tools.protoc -I./ --python_out=../proto_gen --grpc_python_out=../proto_gen kitchen.proto
