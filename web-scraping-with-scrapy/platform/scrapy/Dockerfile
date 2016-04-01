FROM itamtao/python-basis

MAINTAINER Tao Lin <itamtao@gmail.com> 

# install scrapy
RUN pip install scrapy

# add user
USER tlin

RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
      && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc