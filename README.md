# DASH-APP-TEMPLATE

This is a demplate for deploying a dash app within a flask server via gunicorn, containerized in a docker container. 

## To Run

```
docker build -t dash-template .

docker run -p 8050:8050 -d dash-template
```