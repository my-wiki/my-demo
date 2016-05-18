FROM itamtao/python-basis

MAINTAINER Tao Lin <itamtao@gmail.com>

# install packages
RUN pip install --upgrade pip
RUN apt-get -y update
# RUN apt-get -y install python-dev && libssl-dev

RUN mkdir t && cd t && wget https://pypi.python.org/packages/62/ff/263fae9f69150c1b696a94dd23ca48c02512228c53bb108aeaccda192028/cx_Freeze-4.3.4.tar.gz#md5=5bd662af9aa36e5432e9144da51c6378 && \
    tar zxvf cx_Freeze-4.3.4.tar.gz && \
    cd cx_Freeze-4.3.4 && \
    sed -i -e 's/if not vars.get("Py_ENABLE_SHARED", 0):/if True:/g' setup.py && \
    python setup.py build && \
    python setup.py install

# RUN pip install cx_Freeze

# switch user
USER tlin
VOLUME /home/tlin/notebooks
WORKDIR /home/tlin/notebooks

RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
      && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
