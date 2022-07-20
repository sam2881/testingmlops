FROM python:3.8

USER root
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
# ENV HTTP_PROXY '{Proxy server address}'
# ENV HTTPS_PROXY '{Proxy server address'
# ENV FTP_PROXY '{Proxy server address}'

# RUN echo 'Acquire::http::Proxy "{Proxy server address}";' >> /etc/apt/apt.conf
# RUN echo 'Acquire::https::Proxy "{Proxy server address}";' >> /etc/apt/apt.conf
RUN apt-get update && apt-get upgrade -y \
 && apt-get install -y \
    git \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
 && git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT

RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
     eval "$(pyenv init -)"

RUN pyenv install 3.5.9
RUN pyenv install 3.6.2
RUN pyenv install 3.7.2
RUN pyenv install 3.8.2

RUN echo '3.5.9' >> .python-version
RUN echo '3.6.2' >> .python-version
RUN echo '3.7.2' >> .python-version
RUN echo '3.8.2' >> .python-version