# Exercise 4

## Creating a Bridge Network

```bash
docker network create --driver bridge my-bridge-net
```

### Output :

```bash
f3de0799f597d47e3abaabff999795b894d8b742a6e2a248a04a3cbec0891e37
```

## Verify Network

```bash
docker network ls
```

### Output :

```bash
NETWORK ID     NAME            DRIVER    SCOPE
13e53298edc4   bridge          bridge    local
b97f5c3a97d1   host            host      local
f3de0799f597   my-bridge-net   bridge    local
9c739edf7779   none            null      local
```

## Launching Docker container

Build the docker image of the flask app using the following command :

```bash
docker build -t flask-api .
```
Launch the containers in the created Docker network in dettached mode using the following commands :

```bash
docker run -d --name mysql --net=my-bridge-net -e MYSQL_ROOT_PASSWORD=root123 mysql:latest
docker run -d --name redis --net=my-bridge-net redis:latest
docker run -d --name flask --net=my-bridge-net -p 5001:5001 flask-api
```

## Testing the connectivity

Use the following command exec into flask app :
```bash
docker exec -it flask bash
```
Install ping in the flask-api container exec :
```bash
apt-get update && apt-get install -y iputils-ping
```

Then ping MySQL container using the following command :
```bash
ping mysql
```

### Output:
```bash
PING mysql (172.18.0.2) 56(84) bytes of data.
64 bytes from mysql.my-bridge-net (172.18.0.2): icmp_seq=1 ttl=64 time=0.187 ms
64 bytes from mysql.my-bridge-net (172.18.0.2): icmp_seq=2 ttl=64 time=0.085 ms
64 bytes from mysql.my-bridge-net (172.18.0.2): icmp_seq=3 ttl=64 time=0.164 ms
```
Then ping Redis container using the following command :
```bash
ping redis
```
### Output :
```bash
PING redis (172.18.0.3) 56(84) bytes of data.
64 bytes from redis.my-bridge-net (172.18.0.3): icmp_seq=1 ttl=64 time=0.127 ms
64 bytes from redis.my-bridge-net (172.18.0.3): icmp_seq=2 ttl=64 time=0.177 ms
64 bytes from redis.my-bridge-net (172.18.0.3): icmp_seq=3 ttl=64 time=0.153 ms
```

