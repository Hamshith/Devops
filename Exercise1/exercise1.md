#Exercise 1

##Steps of Execution

###Run The following commands:

minikube start

kubectl run hello-k8s --image=nginx --port=80

kubectl get pods

kubectl expose pod hello-k8s --type=NodePort --port=80

minikube service hello-k8s

##Output

![alt text](<Screenshot 2026-08-22 114114.png>)
![alt text](<Screenshot 2026-08-22 114127.png>)
![alt text](<Screenshot 2026-08-22 114047.png>)