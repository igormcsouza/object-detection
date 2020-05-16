FROM igormcsouza/ml:nvidia-tf

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

COPY api /api
COPY scripts /obj-det

WORKDIR /obj-det

CMD [ "/bin/bash" ]