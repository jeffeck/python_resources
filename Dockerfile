FROM ubuntu:18.04

RUN echo 'alias ls="clear;ls -al"' >> ~/.bashrc
RUN apt-get update
RUN apt-get install python3.7 -y
RUN apt-get install python3-pip -y

# RUN apt-get -y install ipython ipython-notebook
RUN pip3 install jupyter

EXPOSE 8888

# ssh -i id_rsa jeff@192.168.1.8
# sudo docker run -it --rm -p 8888:8888 my_image bash
# jupyter notebook --ip=0.0.0.0 --allow-root
