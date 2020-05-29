FROM ubuntu:16.04

# Installing base packages
RUN apt-get -y update && apt-get install wget unzip gcc tar -y && \
        apt-get install -y python-pip python-dev

# Copy files to container
COPY . /app

# Set working directory
WORKDIR /app


# Upgrade PIP
RUN pip install --upgrade pip

# Install the project and dependencies
RUN pip install -e .

#ENTRYPOINT [ "python" ]

#CMD [ "donationpage/run.py" ]

CMD ["uwsgi","ops/app.ini"]