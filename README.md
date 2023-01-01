# Section3-Project

## HOW TO RUN API SERVER
```
cd ~
mkdir ~/temp
docker-compose up 
```

## HOW TO RUN MODELING CONTAINER
```
docker run --rm --network api-server_section3-net -v $(pwd)/temp:/temp cherryjubilee/ml-server:1.3
```

### HOW TO BUILD API SERVER IMAGE
```
docker build --tag cherryjubilee/ml-server:1.0 --platform linux/amd64 `pwd`
```

### HOW TO BUILD ML SERVER IMAGE
```
docker build --tag cherryjubilee/ml-server:1.0 --platform linux/amd64 `pwd
```

