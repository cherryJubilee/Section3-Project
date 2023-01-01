# Section3-Project

## HOW TO RUN API SERVER
```
git clone https://github.com/cherryJubilee/Section3-Project .
cd backend
mkdir temp
docker-compose up 
```

## HOW TO RUN MODELING CONTAINER
```
cd backend/temp
docker run --rm --network api-server_section3-net -v $(pwd)/temp:/temp cherryjubilee/ml-server:1.3
```
- Use crontab for auto model update
```
ubuntu@hyewon-section3:~/temp$ crontab -l
3 * * * * cd /home/ubuntu/api-server/temp && docker run --rm --network api-server_section3-net -v $(pwd)/temp:/temp cherryjubilee/ml-server:1.3
```


### HOW TO BUILD API SERVER IMAGE
```
docker build --tag cherryjubilee/api-server:1.0 --platform linux/amd64 `pwd`
```

### HOW TO BUILD ML SERVER IMAGE
```
docker build --tag cherryjubilee/ml-server:1.0 --platform linux/amd64 `pwd
```

