import docker

client = docker.from_env()
container = None

try:
    print("Building image from Dockerfile...")
    client.images.build(path=".", tag="flask-apparmor")

    print("\nRunning container with AppArmor profile...")
    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": None},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print(f"Container started: {container.short_id}")

    container.reload()
    container_info = client.api.inspect_container(container.id)

    security_options = container_info["HostConfig"]["SecurityOpt"]
    print("\nAppArmor security options:", security_options)
    print("Configured AppArmor profile:", container_info.get("AppArmorProfile"))

    if "apparmor=my-apparmor-profile" in (security_options or []):
        print("AppArmor profile configured successfully.")
    else:
        print("WARNING: Expected AppArmor option was not found.")

finally:
    if container is not None:
        print("\nStopping and removing container...")
        container.stop()
        container.remove()
        print("Container stopped and removed.")
