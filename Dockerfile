From python
WORKDIR /cloudassig
COPY . /cloudassig
copy paragraph.txt
CMD [ "python3" ,"asigg2.py" ]

