FROM jupyter/datascience-notebook:137a295ff71b
USER root

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y

COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN python -m nltk.downloader punkt stopwords wordnet vader_lexicon
RUN apt-get install python-pydot -y