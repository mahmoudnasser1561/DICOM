#!/bin/bash

docker run -d --rm \
  --name orthanc1 \
  -p 8042:8042 -p 4242:4242 \
  -v $(pwd)/orthanc1.json:/etc/orthanc/orthanc.json:ro \
  jodogne/orthanc

docker run -d --rm \
  --name orthanc2 \
  -p 8043:8043 -p 4243:4243 \
  -v $(pwd)/orthanc2.json:/etc/orthanc/orthanc.json:ro \
  jodogne/orthanc

docker run -d --rm \
  --name orthanc3 \
  -p 8044:8044 -p 4244:4244 \
  -v $(pwd)/orthanc3.json:/etc/orthanc/orthanc.json:ro \
  jodogne/orthanc

