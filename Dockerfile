FROM dockerfile/python

RUN apt-get update -y -q && \
    apt-get install -y -q phantomjs

RUN pip install --upgrade pip
RUN pip install selenium
RUN pip install pandas

RUN echo -e "\n210.63.38.209\tetusaasentry.com\n210.63.38.209\tetusaas.com\n" > /etc/hosts

COPY . /

RUN python web_test_gen_scene001.py web_test_scene001 5
RUN python web_test_gen_scene002.py web_test_scene002 5
RUN python web_test_gen_scene003.py web_test_scene003 5
RUN python web_test_gen_scene004.py web_test_scene004 5

RUN python web_saas2.py web_test_scene001.csv
RUN python web_saas2.py web_test_scene002.csv
RUN python web_saas2.py web_test_scene003.csv
RUN python web_saas2.py web_test_scene004.csv

#CMD ["python", "web_saas2.py"]
#CMD ["python", "web_saas.py"]
#CMD ["python", "web_test_gen_scene001.py"]
#CMD ["python", "web_test_gen_scene002.py"]
#CMD ["python", "web_test_gen_scene003.py"]
#CMD ["python", "web_test_gen_scene004.py"]
