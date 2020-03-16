
## CUDA / NVIDIA drivers
```
dpkg -l | grep '^rc' | awk '{print $2}' | xargs sudo apt-get purge

sudo apt install nvidia-utils-440
sudo apt install nvidia-driver-440

# cuda
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-10-2-local-10.2.89-440.33.01/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda

wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libcudnn7_7.6.5.32-1+cuda10.2_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libcudnn7-dev_7.6.5.32-1+cuda10.2_amd64.deb

sudo dpkg -i libcudnn7_7.6.5.32-1+cuda10.2_amd64.deb
sudo dpkg -i libcudnn7-dev_7.6.5.32-1+cuda10.2_amd64.deb

sudo apt install --no-install-recommends \
    libcudnn7=7.6.5.32-1+cuda10.2  \
    libcudnn7-dev=7.6.5.32-1+cuda10.2


wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnccl2_2.5.6-1+cuda10.2_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnccl-dev_2.5.6-1+cuda10.2_amd64.deb

sudo dpkg -i libnccl2_2.5.6-1+cuda10.2_amd64.deb
sudo dpkg -i libnccl-dev_2.5.6-1+cuda10.2_amd64.deb


sudo apt install \
    libnccl2 \
    libnccl-dev

wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvinfer7_7.0.0-1+cuda10.2_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvinfer-dev_7.0.0-1+cuda10.2_amd64.deb

sudo dpkg -i libnvinfer7_7.0.0-1+cuda10.2_amd64.deb
sudo dpkg -i libnvinfer-dev_7.0.0-1+cuda10.2_amd64.deb


wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvinfer-plugin7_7.0.0-1+cuda10.2_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvinfer-plugin-dev_7.0.0-1+cuda10.2_amd64.deb

sudo dpkg -i libnvinfer-plugin7_7.0.0-1+cuda10.2_amd64.deb
sudo dpkg -i libnvinfer-plugin-dev_7.0.0-1+cuda10.2_amd64.deb


sudo apt install \
    libnvinfer7 \
    libnvinfer-dev \
    libnvinfer-plugin7 \
    libnvinfer-plugin-dev


wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvonnxparsers7_7.0.0-1+cuda10.2_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvonnxparsers-dev_7.0.0-1+cuda10.2_amd64.deb

sudo dpkg -i libnvonnxparsers7_7.0.0-1+cuda10.2_amd64.deb
sudo dpkg -i libnvonnxparsers-dev_7.0.0-1+cuda10.2_amd64.deb

sudo apt install \
    libnvonnxparsers7 \
    libnvonnxparsers-dev

wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvparsers7_7.0.0-1+cuda10.2_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvparsers-dev_7.0.0-1+cuda10.2_amd64.deb

sudo dpkg -i libnvparsers7_7.0.0-1+cuda10.2_amd64.deb
sudo dpkg -i libnvparsers-dev_7.0.0-1+cuda10.2_amd64.deb

sudo apt install \
    libnvparsers7 \
    libnvparsers-dev


# export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
# export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
## TensorRT

instructions:
https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html#installing

Download from:

https://developer.nvidia.com/compute/machine-learning/tensorrt/secure/7.0/7.0.0.11/local_repo/nv-tensorrt-repo-ubuntu1804-cuda10.2-trt7.0.0.11-ga-20191216_1-1_amd64.deb
```bash

sudo dpkg -i nv-tensorrt-repo-ubuntu1804-cuda10.2-trt7.0.0.11-ga-20191216_1-1_amd64.deb
sudo apt-key add /var/nv-tensorrt-repo-cuda10.2-trt7.0.0.11-ga-20191216/7fa2af80.pub

sudo apt update
sudo apt install tensorrt
sudo apt-get install uff-converter-tf

wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/python3-libnvinfer_7.0.0-1+cuda10.2_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/python3-libnvinfer-dev_7.0.0-1+cuda10.2_amd64.deb

sudo dpkg -i python3-libnvinfer_7.0.0-1+cuda10.2_amd64.deb
sudo dpkg -i python3-libnvinfer-dev_7.0.0-1+cuda10.2_amd64.deb

sudo apt install \
    python3-libnvinfer \
    python3-libnvinfer-dev

# python 2 case (dead)
# wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/python-libnvinfer_7.0.0-1+cuda10.2_amd64.deb 
# wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/python-libnvinfer-dev_7.0.0-1+cuda10.2_amd64.deb

# sudo dpkg -i python-libnvinfer_7.0.0-1+cuda10.2_amd64.deb 
# sudo dpkg -i python-libnvinfer-dev_7.0.0-1+cuda10.2_amd64.deb

# sudo apt install \
#     python-libnvinfer \
#     python-libnvinfer-dev

```
## nvidia-container-runtime

https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)

```bash
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
  sudo apt-key add -
distribution=ubuntu18.04
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt update
sudo apt-get install nvidia-container-runtime
```

## docker engine setup

```
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo tee /etc/systemd/system/docker.service.d/override.conf <<EOF
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd --host=fd:// --add-runtime=nvidia=/usr/bin/nvidia-container-runtime
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

