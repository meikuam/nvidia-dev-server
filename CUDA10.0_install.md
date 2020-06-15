## Ubuntu 18.04
## CUDA 10.0
```
wget https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64
sudo dpkg -i cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-10-0-local-10.0.130-410.48/7fa2af80.pub 
sudo apt-get update
sudo apt-get install cuda


export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

## cuDNN

https://developer.nvidia.com/rdp/cudnn-download
```bash
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libcudnn7-dev_7.4.2.24-1+cuda10.0_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libcudnn7_7.4.2.24-1+cuda10.0_amd64.deb
```
```bash

sudo dpkg -i libcudnn7_7.0.3.11-1+cuda9.0_amd64.deb
```
```
tar -zxvf cudnn-9.0-linux-x64-v7.tgz
# Move the unpacked contents to your CUDA directory
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64/
sudo cp  cuda/include/cudnn.h /usr/local/cuda/include/
# Give read access to all users
sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
```


```
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libcudnn7_7.6.5.32-1+cuda10.0_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libcudnn7-dev_7.6.5.32-1+cuda10.0_amd64.deb

sudo dpkg -i libcudnn7_7.6.5.32-1+cuda10.0_amd64.deb
sudo dpkg -i libcudnn7-dev_7.6.5.32-1+cuda10.0_amd64.deb

sudo apt install --no-install-recommends \
    libcudnn7=7.6.5.32-1+cuda10.0  \
    libcudnn7-dev=7.6.5.32-1+cuda10.0

wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnccl2_2.5.6-1+cuda10.0_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnccl-dev_2.5.6-1+cuda10.0_amd64.deb

sudo dpkg -i libnccl2_2.5.6-1+cuda10.0_amd64.deb
sudo dpkg -i libnccl-dev_2.5.6-1+cuda10.0_amd64.deb


sudo apt install \
    libnccl2 \
    libnccl-dev

wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvinfer7_7.0.0-1+cuda10.0_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvinfer-dev_7.0.0-1+cuda10.0_amd64.deb

sudo dpkg -i libnvinfer7_7.0.0-1+cuda10.0_amd64.deb
sudo dpkg -i libnvinfer-dev_7.0.0-1+cuda10.0_amd64.deb


wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvinfer-plugin7_7.0.0-1+cuda10.0_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvinfer-plugin-dev_7.0.0-1+cuda10.0_amd64.deb

sudo dpkg -i libnvinfer-plugin7_7.0.0-1+cuda10.0_amd64.deb
sudo dpkg -i libnvinfer-plugin-dev_7.0.0-1+cuda10.0_amd64.deb


sudo apt install \
    libnvinfer7 \
    libnvinfer-dev \
    libnvinfer-plugin7 \
    libnvinfer-plugin-dev


wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvonnxparsers7_7.0.0-1+cuda10.0_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvonnxparsers-dev_7.0.0-1+cuda10.0_amd64.deb

sudo dpkg -i libnvonnxparsers7_7.0.0-1+cuda10.0_amd64.deb
sudo dpkg -i libnvonnxparsers-dev_7.0.0-1+cuda10.0_amd64.deb

sudo apt install \
    libnvonnxparsers7 \
    libnvonnxparsers-dev

wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvparsers7_7.0.0-1+cuda10.0_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvparsers-dev_7.0.0-1+cuda10.0_amd64.deb

sudo dpkg -i libnvparsers7_7.0.0-1+cuda10.0_amd64.deb
sudo dpkg -i libnvparsers-dev_7.0.0-1+cuda10.0_amd64.deb

sudo apt install \
    libnvparsers7 \
    libnvparsers-dev
```

## TensorRT

https://developer.nvidia.com/nvidia-tensorrt-7x-download

```
sudo dpkg -i nv-tensorrt-repo-ubuntu1804-cuda10.0-trt7.0.0.11-ga-20191216_1-1_amd64.deb
sudo apt-key add /var/nv-tensorrt-repo-cuda10.0-trt7.0.0.11-ga-20191216/7fa2af80.pub

sudo apt update
sudo apt install tensorrt
sudo apt-get install uff-converter-tf

wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/python3-libnvinfer_7.0.0-1+cuda10.0_amd64.deb
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/python3-libnvinfer-dev_7.0.0-1+cuda10.0_amd64.deb

sudo dpkg -i python3-libnvinfer_7.0.0-1+cuda10.0_amd64.deb
sudo dpkg -i python3-libnvinfer-dev_7.0.0-1+cuda10.0_amd64.deb

sudo apt install \
    python3-libnvinfer \
    python3-libnvinfer-dev

# python 2 case (dead)
# wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/python-libnvinfer_7.0.0-1+cuda10.0_amd64.deb 
# wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/python-libnvinfer-dev_7.0.0-1+cuda10.0_amd64.deb

# sudo dpkg -i python-libnvinfer_7.0.0-1+cuda10.0_amd64.deb 
# sudo dpkg -i python-libnvinfer-dev_7.0.0-1+cuda10.0_amd64.deb

# sudo apt install \
#     python-libnvinfer \
#     python-libnvinfer-dev

```


## nvidia-container-runtime

тут обычно нужно править `$(ARCH)` на  `amd64`
и `distribution=ubuntu18.04`


```
curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | \
  sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list

sudo apt-get update

sudo apt-get install nvidia-container-runtime
```



# setup Docker

## docker

```                           
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce
sudo service docker restart
 
sudo groupadd docker          
sudo usermod -aG docker $USER 
                              
sudo systemctl enable docker

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

