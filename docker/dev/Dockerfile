FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt install -y --no-install-recommends \
    libsm6 libxext6 libxrender-dev \
    sudo \
    openssh-server \
    vim \
    git \
    curl wget \
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
RUN wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O  /opt/anaconda.sh &&\
    chmod +x /opt/anaconda.sh &&\
    bash /opt/anaconda.sh -b -p /opt/anaconda
RUN groupadd anaconda && \
    chgrp -R anaconda /opt/anaconda &&\
    chmod 770 -R /opt/anaconda &&\
    usermod -a -G anaconda $USER


USER root
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin /PermitRootLogin yes #/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication/PasswordAuthentication yes#/' /etc/ssh/sshd_config
#SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
ENV LD_LIBRARY_PATH /usr/local/cuda/lib64:$LD_LIBRARY_PATH
ENV PATH /opt/anaconda/bin:/usr/local/cuda/bin:$PATH
RUN echo "export PATH=$PATH" >> /etc/profile
RUN echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH" >> /etc/profile
RUN echo "export VISIBLE=now" >> /etc/profile
RUN echo "export NOTVISIBLE=$NOTVISIBLE" >> /etc/profile
RUN echo "export LC_ALL=C.UTF-8" >> /etc/profile
RUN echo "export LANG=C.UTF-8" >> /etc/profile


COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

USER $USER
RUN eval "$(/opt/anaconda/bin/conda shell.bash hook)"
WORKDIR /tmp/
ADD requirements.txt /tmp/requirements.txt

RUN pip install Cython && \
    pip install -r requirements.txt
#RUN conda install -y Cython && \
#    conda install -y --file requirements.txt

WORKDIR $HOME_DIR

#VOLUME ["$DATA_DIR","$HOME_DIR"]

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["bash"]
