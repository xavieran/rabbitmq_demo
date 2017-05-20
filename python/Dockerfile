FROM centos:7


RUN yum install -y gcc \
                   gcc-c++ \ 
                   kernel-devel \ 
                   xz-libs; \ 
    yum clean all

RUN yum install -y epel-release \
                   python2 \
                   python-setuptools \
                   python-devel && \
                   yum clean all

RUN yum install -y python2-pip && pip install --upgrade pip

RUN pip install pika
