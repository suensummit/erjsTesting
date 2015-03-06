FROM dockerfile/python

RUN apt-get update -y -q && \
    apt-get install -y -q phantomjs

RUN pip install --upgrade pip
RUN pip install selenium
RUN pip install pandas

RUN echo -e "\n210.63.38.209\tetusaasentry.com\n210.63.38.209\tetusaas.com\n" > /etc/hosts

COPY . /
CMD ["python", "web_saas2.py"]
CMD ["python", "web_saas.py"]
CMD ["python", "web_test_gen_scene001.py"]
CMD ["python", "web_test_gen_scene002.py"]
CMD ["python", "web_test_gen_scene003.py"]
CMD ["python", "web_test_gen_scene004.py"]
