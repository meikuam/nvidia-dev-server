FROM nvidia/cuda:11.3.1-cudnn8-devel-ubuntu20.04
SHELL ["/bin/bash", "-c"]

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt install -y --no-install-recommends \
    libsm6 libxext6 libxrender-dev \
    sudo \
    openssh-server \
    vim \
    git \
    curl wget supervisor\
    libsqlite3-dev libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev  llvm libncurses5-dev libncursesw5-dev \
    libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

ARG UID
ARG USER
ARG PASSWORD
ARG PORTS

EXPOSE 22
EXPOSE $PORTS

ENV HOME_DIR /home/$USER
ENV DATA_DIR /data

RUN useradd -d $HOME_DIR -ms /bin/bash  -u $UID -G sudo $USER
RUN echo $USER:$PASSWORD | chpasswd


## python
RUN mkdir /opt/anaconda && \
    chown -R $USER:$USER /opt/anaconda &&\
    chmod 770 -R /opt/anaconda
USER $USER
RUN wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh -O  /opt/anaconda/anaconda.sh &&\
    chmod +x /opt/anaconda/anaconda.sh &&\
    bash /opt/anaconda/anaconda.sh -b -p /opt/anaconda/anaconda


USER root
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin /PermitRootLogin yes #/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication/PasswordAuthentication yes#/' /etc/ssh/sshd_config
#SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
ENV LD_LIBRARY_PATH /usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
ENV PATH /opt/anaconda/anaconda/bin:/usr/local/cuda/bin:$PATH
RUN echo "export PATH=$PATH" >> /etc/profile
RUN echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH" >> /etc/profile
RUN echo "export VISIBLE=now" >> /etc/profile
RUN echo "export NOTVISIBLE=$NOTVISIBLE" >> /etc/profile
RUN echo "export LC_ALL=C.UTF-8" >> /etc/profile
RUN echo "export LANG=C.UTF-8" >> /etc/profile


COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

COPY supervisord /etc/supervisor/conf.d/

RUN sed -i 's/username/'"$USER"'/g' /etc/supervisor/conf.d/sshd.conf

RUN sed -i 's/username/'"$USER"'/g' /etc/supervisor/conf.d/jupyter.conf
# use first port as jupyter port
RUN PORTS_LIST=($PORTS) && sed -i 's/8888/'"${PORTS_LIST[0]}"'/g' /etc/supervisor/conf.d/jupyter.conf


USER $USER
RUN eval "$(/opt/anaconda/anaconda/bin/conda shell.bash hook)"
WORKDIR /tmp/
ADD requirements.txt /tmp/requirements.txt

RUN pip install Cython && \
    pip install -r requirements.txt
#RUN conda install -y Cython && \
#    conda install -y --file requirements.txt

# install custom tensorflow 2.1.0 and keras 2.3.1
# RUN pip install torch==1.4.0 torchvision==0.5.0
# RUN conda install keras-gpu==2.3.1
#RUN pip install https://github.com/inoryy/tensorflow-optimized-wheels/releases/download/v2.1.0/tensorflow-2.1.0-cp37-cp37m-linux_x86_64.whl

WORKDIR $HOME_DIR

#ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["supervisord", "-n"]
