FROM docker.io/continuumio/miniconda3:23.3.1-0
MAINTAINER faustinoaq <faustino.aguilar@up.ac.pa>

RUN apt-get update
RUN apt-get -y install git nano dos2unix build-essential

RUN conda install python=3.10.14
RUN pip install pynguin

WORKDIR /home/user

COPY ./framework /home/user/BugsInPy/framework
COPY ./projects /home/user/BugsInPy/projects
COPY ./out_DYNAMOSA /home/user/BugsInPy/out_DYNAMOSA
COPY ./out_RANDOM /home/user/BugsInPy/out_RANDOM
COPY ./out_WHOLE_SUITE /home/user/BugsInPy/out_WHOLE_SUITE
COPY ./out_MIO /home/user/BugsInPy/out_MIO

ENV PATH=/home/user/BugsInPy/framework/bin:$PATH

ENTRYPOINT ["pynguin-script"]
ENTRYPOINT ["testingall-script"]
CMD [""]