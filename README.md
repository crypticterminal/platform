## Syncloud (https://syncloud.org)

Syncloud brings popular apps to your place.

It is available as an image or pre-installed device.

### Apps

* [Nextcloud](https://nextcloud.com/): File sharing, calendar, contacts.
* [Diaspora](https://diasporafoundation.org/): Social network.
* [Rocketchat](https://rocket.chat/): Text, voice and video messaging.
* [Mail](https://roundcube.net/): Email messaging with Roundcube web.
* [GOGS](https://gogs.io/): Git source code hosting.
* [Syncthing](https://syncthing.net/): File synchronization between devices.

### Images

https://github.com/syncloud/platform/wiki

## For developers

Syncloud platform manages the installation and device settings.

### Running local drone build

Get drone cli binary: http://docs.drone.io/cli-installation/
````
sudo DOCKER_API_VERSION=1.24 arch=[amd64|arm] /path/to/cli/drone exec
````

Watch drone build processes:
````
watch -n 1 pstree -a $(pgrep -f dockerd)
````

### Build server

http://build.syncloud.org/syncloud/platform

### Build artifacts (screenshots, system logs)

http://artifact.syncloud.org/platform/ci