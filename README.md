# dserve
Deep learning models Serving with Python

## Build
```
docker build -f Dockerfile -t dserve .
```

## Run
```
docker run -it --rm dserve 
```

## Serve
```
gunicorn api:app -w 4 -k uvicorn.workers.UvicornWorker -c ./gunicorn_conf.py
```
