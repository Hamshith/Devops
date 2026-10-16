# Exercise 6

Use WSL for this exercise

## Install prometheus package for python into a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install prometheus-client
```
## Create a file structure as following

```
delivery_monitoring/
├── delivery_metrics.py   # Python script to simulate metrics
├── prometheus.yml        # Prometheus configuration
├── alerts_rules.yml      # Alerts configuration
├── Jenkinsfile           # Jenkins pipeline script

```
Change the directory using the following commmand :

```bash
cd delivery_monitoring
```
## Run the delivery_metrics.py file using the following command :

```bash
python delivery_metrics.py
```

The metrics log can be accessed in the following link :  http://localhost:8000/metrics

## Configure prometheus in the prometheus.yml  and alerts_rules.yml file and run it using the following command :

Create a network for prometheus and grafana
```bash
docker network create monitoring
```
Create docker container : 
```bash
docker run -d \
  --name prometheus \
  --network monitoring \
  -p 9090:9090 \
  -v "$(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml:ro" \
  -v "$(pwd)/alert_rules.yml:/etc/prometheus/alert_rules.yml:ro" \
  prom/prometheus
```
Prometheus can be viewed at this link : http://localhost:9090/query

## Run Grafana on docker using the following command : 
```bash
docker run -d \
  --name grafana \
  --network monitoring \
  -p 3000:3000 \
  grafana/grafana
```

Access grafana at http://localhost:3000/
Use the folloowing credentials :
Username : admin
password : admin

## Connect Grafana to Prometheus
In Grafana:
1. Navigate to Connections → Data sources.
2. Add a Prometheus data source.
3. Set the URL to http://prometheus:9090.
4. Select Save & test.

## Create a dashboard with these queries:
Panel	                PromQL query
Total deliveries	    total_deliveries
Pending deliveries	    pending_deliveries
On-the-way deliveries	on_the_way_deliveries
Average delivery time	average_delivery_time_sum / average_delivery_time_count

## Create Jenkins Pipeline

### Run Jenkins using the following command:

Since the Jenkins pipeline requires Docker CLI access to build images and manage containers, create a custom Jenkins image with Docker installed.

Create a file named `Dockerfile.jenkins` 

Build the custom Jenkins image:

```bash
docker build -t jenkins-with-docker -f Dockerfile.jenkins .
```

Run Jenkins using the following command from WSL, replacing the project path if necessary:

```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "/mnt/c/Users/Hamshith/Desktop/Programming Files/DevOps/Exercise 6/delivery_monitoring:/delivery_monitoring:ro" \
  jenkins-with-docker
```

### Get the initial administrator password

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Open [http://localhost:8080](http://localhost:8080), complete the Jenkins setup, and install the required plugins.

### Configure Docker socket permissions

Check the Docker socket's group ID:

```bash
stat -c '%g' /var/run/docker.sock
```

For this setup, the group ID was `1001`. Create the corresponding group inside Jenkins and add the Jenkins user to it:

```bash
docker exec -u root jenkins groupadd -g 1001 docker-host
docker exec -u root jenkins usermod -aG docker-host jenkins
docker restart jenkins
```

Verify Docker access:

```bash
docker exec jenkins docker version
docker exec jenkins docker info
```

Both commands should display Docker Client and Server information without permission errors.

### Create the Jenkinsfile

Create a file named `Jenkinsfile` inside the `delivery_monitoring` project directory


### Configure and run the pipeline

1. Open Jenkins at [http://localhost:8080](http://localhost:8080).
2. Select **New Item**, enter a pipeline name, and choose **Pipeline**.
3. Under the Pipeline section, select **Pipeline script** and paste the contents of the `Jenkinsfile`.
4. Save the pipeline and click **Build Now**.
5. Open **Console Output** to check each stage and confirm that the build succeeds.

### Verify the deployment

- Application metrics: [http://localhost:8000/metrics](http://localhost:8000/metrics)
- Prometheus: [http://localhost:9090](http://localhost:9090)
- Grafana: [http://localhost:3000](http://localhost:3000)

Check the running containers using:

```bash
docker ps
```

**Security note:** Mounting `/var/run/docker.sock` grants Jenkins extensive control over Docker. Use this configuration for the local exercise only, with appropriate security controls in production.

## Screenshots

![alt text](<Screenshot 2026-10-16 210011.png>) 


![alt text](<Screenshot 2026-10-16 210025.png>)

![alt text](image.png)