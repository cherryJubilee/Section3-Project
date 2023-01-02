
# Section3-Project
---
>Project Sample  
>Front page: http://hyewon-section3.s3-website.ap-northeast-2.amazonaws.com/  
>(Hosted on AWS S3)  
>API Server: http://3.39.5.135/   
>(Hosted on AWS EC2)  
---
## SETUP DIRECTORIES
```
git clone https://github.com/cherryJubilee/Section3-Project .
cd Section3-Project/backend
mkdir -p ./db/conf.d
mkdir -p ./db/data
mkdir -p ./db/initdb.d
mkdir ./temp
mkdir ./metabase-data
```

## HOW TO RUN API SERVER
```
cd Section3-Project/backend
docker-compose up 
```

## HOW TO RUN MODELING CONTAINER
```
cd backend
docker run --rm --network api-server_section3-net -v $(pwd)/temp:/temp cherryjubilee/ml-server:1.4
```
- Use crontab for auto model update
```
3 * * * * cd /home/ubuntu/api-server && docker run --rm --network api-server_section3-net -v $(pwd)/temp:/temp cherryjubilee/ml-server:1.4
```
---

### HOW TO BUILD API SERVER IMAGE
```
docker build --tag cherryjubilee/api-server:1.11 --platform linux/amd64 `pwd`
```

### HOW TO BUILD ML SERVER IMAGE
```
docker build --tag cherryjubilee/ml-server:1.4 --platform linux/amd64 `pwd`
```

