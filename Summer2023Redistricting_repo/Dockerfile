FROM docker.io/continuumio/miniconda3:23.3.1-0
MAINTAINER faustinoaq <faustino.aguilar@up.ac.pa>

RUN apt-get update
RUN apt-get -y install git nano dos2unix build-essential

RUN conda create -n redistricting -c conda-forge -y python=3.10.14 pip ipykernel geopandas networkx mapclassify matplotlib tqdm scipy numpy ipywidgets
RUN echo "source activate redistricting" > ~/.bashrc
ENV PATH=/opt/conda/envs/redistricting/bin:$PATH
RUN pip install gerrychain==0.3.1

RUN pip install pynguin
ENV PYNGUIN_DANGER_AWARE=1
ENV PYTHONIOENCODING=utf-8

WORKDIR /home/user

COPY . /home/user/Summer2023Redistricting/

ENTRYPOINT ["./Summer2023Redistricting/pynguin-script.sh"]
CMD [""]