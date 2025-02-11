# Requirements
Make sure to have the following installed on your machine:
* Ubuntu 24.04
* Docker with nvidia support
    * Follow [this guide](https://docs.docker.com/engine/install/ubuntu/) to install docker
    * Follow [this guide](https://docs.nvidia.com/ai-enterprise/deployment/vmware/latest/docker.html) to add nvidia support
* GIT
* GNU make
# How to run
Start by cloning the repository:
```bash
git clone https://github.com/fearriagar/furgpt.git
```
Go to the repository's directory and create a `.env` file:
```bash
cd furgpt
cp .env.public .env
```
Populate the environment variable inside the `.env` file with your application's discord token.

Finally, run FurGPT:
```bash
make start-furgpt
make create-model
make run-model
```