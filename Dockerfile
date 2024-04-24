From python: 3.8
WORKDIR /cloudassig
Run pip install nltk
Run python -m nltk.downloader stopwords punkt
COPY . /cloudassig
CMD [ "python3" ,"asigg2.py" ]

