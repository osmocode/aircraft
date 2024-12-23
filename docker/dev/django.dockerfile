FROM python:3.13

# Set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED=1

WORKDIR /server

# Install dependencies
ADD server/requirements.txt /server/requirements.txt
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r requirements.txt

# Copy sources
ADD server/aircraft /server/aircraft
ADD server/apps /server/apps
ADD server/manage.py /server/manage.py
