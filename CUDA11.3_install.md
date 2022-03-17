
## CUDA / NVIDIA drivers
```
dpkg -l | grep '^rc' | awk '{print $2}' | xargs sudo apt-get purge

sudo apt install nvidia-utils-510
sudo apt install nvidia-driver-510

# cuda
## https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600

sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
sudo apt-get update

wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu2004/x86_64/nvidia-machine-learning-repo-ubuntu2004_1.0.0-1_amd64.deb

sudo apt install ./nvidia-machine-learning-repo-ubuntu2004_1.0.0-1_amd64.deb
sudo apt-get update

# wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-11-3_11.3.1-1_amd64.deb
# sudo dpkg -i cuda-11-3_11.3.1-1_amd64.deb

## https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu2004/x86_64/7fa2af80.pub
# sudo apt-key add /var/cuda-11-3_11.3.1-1_amd64/7fa2af80.pub

sudo apt-get update
sudo apt-get -y install cuda

## https://developer.nvidia.com/rdp/cudnn-archive
## https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/libcudnn8-dev_8.2.1.32-1+cuda11.3_amd64.deb
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/libcudnn8_8.2.1.32-1+cuda11.3_amd64.deb

sudo dpkg -i libcudnn8-dev_8.2.1.32-1+cuda11.3_amd64.deb
sudo dpkg -i libcudnn8_8.2.1.32-1+cuda11.3_amd64.deb

sudo apt install --no-install-recommends \
    libcudnn8
    libcudnn8-dev



# export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
# export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
