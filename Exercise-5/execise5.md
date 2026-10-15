# Exercise 5

## Steps of Execution

### Use Ubuntu VM and execute the following commands

Check whether the AppArmor is enabled in VM
```bash
cat /sys/module/apparmor/parameters/enabled
```

Mount the AppArmor module
```bash
mount | grep apparmor
```

Install AppArmor Utilities with the following command
```bash
sudo apt install -y apparmor-utils
```
### Build the Docker Image with the following command
```bash
docker build -t flask-apparmor .
```

### Create an custom AppArmor Profile using the following command:
```bash
sudo nano /etc/apparmor.d/my-apparmor-profile
```

And paste the following content into it :

```bash
#include <tunables/global>

profile my-apparmor-profile flags=(attach_disconnected,mediate_deleted) {
    #include <abstractions/base>

    # Network: Flask listening on 0.0.0.0:5000
    network,

    # Python interpreter and libraries (python:3.8-slim installs here)
    /usr/local/bin/python* ix,
    /usr/local/** mr,
    /usr/lib/** mr,
    /lib/** mr,

    # Application directory
    /app/ r,
    /app/** rwk,

    # Runtime files Python/Flask commonly touch
    /proc/** r,
    /sys/devices/system/cpu/** r,
    /dev/null rw,
    /dev/urandom r,

    # Let Docker stop the container
    signal (receive) peer=unconfined,

    # Deny sensitive files
    deny /etc/passwd r,
    deny /etc/shadow r,
    deny /var/** rw,

    # Deny executing system binaries (bash, cat, etc.)
    deny /bin/** mx,
    deny /usr/bin/** mx,
    deny /sbin/** mx,
    deny /usr/sbin/** mx,

    # Capabilities
    capability net_bind_service,
    deny capability sys_admin,
}
```
Then run the following command to parse the AppArmor Profile
```bash
sudo apparmor_parser -r /etc/apparmor.d/my-apparmor-profile
```
Then run the docker image with the apparmor security
```bash
docker run --rm --security-opt apparmor=my-apparmor-profile -p 5000:5000 flask-apparmor
```

### SDK Docker Scripts

Write the files and run the following commands :

```bash
python apply_armor.py
```

```bash
python test_restricted_action.py
```
## Screenshots
![alt text](<Screenshot 2026-10-15 215048.png>)
