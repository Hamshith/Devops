
# Exercise 8


## Create a GitHub Repository

### 1.1 Create a New Repository

Create a new repository named devops-sample-code

Repository URL:

```text
https://github.com/Hamshith/devops-sample-code.git
```

This exercise uses a separate repository for the Jenkins job. The existing `Devops` repository continues to contain the other exercises.

## Create a file named hello-world.sh

Have the code in the hello-world.sh as in the directory

Save the file and make it executable on Linux or WSL:

```bash
chmod +x hello-world.sh
```

---

## Step 3: Initialize the Local Git Repository and push the file to remote repo

Initialize the repository and use the `main` branch:

```bash
git init
git branch -M main
git commit -m "Add hello-world.sh"
```

Add the remote repository:

```bash
git remote add origin https://github.com/Hamshith/devops-sample-code.git
```
Push the local `main` branch:

```bash
git push -u origin main
```

## Ensure Jenkins Is Running

1. Open a browser.
2. Navigate to `http://localhost:8080`, or use the URL for your Jenkins installation.
3. Log in with your Jenkins credentials.

Ensure Jenkins is running before continuing.

---

## Create a New Jenkins Job

1. On the Jenkins dashboard, click **New Item**.
2. Enter the job name:

   `HelloWorld`

3. Select **Freestyle project**.
4. Click **OK**.


## Configure the Jenkins Job

### General Settings

Optionally, add the following description:

```text
Hello World! Jenkins job.
```

### Source Code Management

1. Locate **Source Code Management**.
2. Select **Git**.
3. Enter the repository URL:

```text
https://github.com/Hamshith/devops-sample-code.git
```

4. Under **Branches to build**, enter:

```text
*/main
```

5. Since the repository is public, credentials are normally not required for cloning.

### Build Steps

1. Locate **Build Steps**.
2. Click **Add build step**.
3. Select **Execute shell**.
4. Enter the following command:

```bash
bash hello-world.sh
```

5. Click **Save**.


## Run the Jenkins Job

1. Open the `HelloWorld` job.
2. Click **Build Now**.
3. Wait for the build to finish.
4. In **Build History**, click the latest build number.
5. Click **Console Output**.

## Screenshots :

![alt text](<localhost_8080_job_HelloWorld_configure (1).png>)

---

![alt text](<Screenshot 2026-10-17 150746.png>) 

---

![alt text](<Screenshot 2026-10-17 150836.png>)