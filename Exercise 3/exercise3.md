# Exercise 2

## Steps of Execution

Write the app.py file and a Dockerfile to build the image of the app

### Command used to build the docker image :

```bash
docker build -t hamshith/flashsale:1.0 .
```
Once the image is build push it to the Dockerhub Repository

### Command to push the image to the Dockerhub Repository

```bash
docker push hamshith/flashsale:1.0
```

### Command to create a Minikube server

```bash
minikube start --nodes=1
```

Once the minikube server is created write the replicaset.yaml file

### Command to apply the configurations in the replicaset.yaml

```bash
kubectl apply -f replicaset.yaml
```

### Command to initialize Minikube and  build image 

```bash
minikube docker-env
eval $(minikube docker-env)
docker build -t flask-app .
```

### Verify the container using the following command

```bash
kubectl get pods
```

#### Output :

```bash
NAME                 READY   STATUS    RESTARTS   AGE
flashsale-rs-86g8c   1/1     Running   0          41s
flashsale-rs-lsb85   1/1     Running   0          41s
flashsale-rs-whhzl   1/1     Running   0          41s
```

### Run the following command to scale the replicas from 3 to 5

```bash
kubectl scale rs flashsale-rs --replicas=5
```

#### Output :

```bash
replicaset.apps/flashsale-rs scaled
```

### Verify the scaling using the following command :

```bash
kubectl get rs
```

#### Output :

```bash
NAME           DESIRED   CURRENT   READY   AGE
flashsale-rs   5         5         5       3m33s
```

### Verify updated pods using the following command :

```bash
kubectl get pods
```

#### Output :

```bash
NAME                 READY   STATUS    RESTARTS   AGE
flashsale-rs-86g8c   1/1     Running   0          4m45s
flashsale-rs-d7d92   1/1     Running   0          107s
flashsale-rs-lsb85   1/1     Running   0          4m45s
flashsale-rs-ngsqw   1/1     Running   0          107s
flashsale-rs-whhzl   1/1     Running   0          4m45s
```

### Delete one of the pods using the following command :

```bash
kubectl delete pod flashsale-rs-whhzl
```

#### Output :

```bash
pod "flashsale-rs-whhzl" deleted from default namespace
```

### Verify the pods using the following command :

```bash
kubectl get pods
```

#### Output :

```bash
NAME                 READY   STATUS    RESTARTS   AGE
flashsale-rs-86g8c   1/1     Running   0          8m6s
flashsale-rs-d7d92   1/1     Running   0          5m8s
flashsale-rs-lsb85   1/1     Running   0          8m6s
flashsale-rs-ngsqw   1/1     Running   0          5m8s
flashsale-rs-xzln7   1/1     Running   0          70s
```

### View the pod distribution across nodes using the following command :

```bash
kubectl get pods -o wide
```

#### Output :

```bash
NAME                 READY   STATUS    RESTARTS   AGE     IP            NODE       NOMINATED NODE   READINESS GATES
flashsale-rs-86g8c   1/1     Running   0          9m34s   10.244.0.7    minikube   <none>           <none>
flashsale-rs-d7d92   1/1     Running   0          6m36s   10.244.0.10   minikube   <none>           <none>
flashsale-rs-lsb85   1/1     Running   0          9m34s   10.244.0.9    minikube   <none>           <none>
flashsale-rs-ngsqw   1/1     Running   0          6m36s   10.244.0.11   minikube   <none>           <none>
flashsale-rs-xzln7   1/1     Running   0          2m38s   10.244.0.12   minikube   <none>           <none>
```

## Screenshots of Output :

![alt text](<Screenshot 2026-09-17 211805.png>)

![alt text](<Screenshot 2026-09-17 211729.png>)

## Screenshot of the Dockerhub Repo :

![alt text](image.png)