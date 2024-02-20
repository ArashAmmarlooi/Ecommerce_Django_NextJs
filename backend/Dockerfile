# # backend/Dockerfile

# FROM python:3.11-alpine

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# # Create and set the working directory
# WORKDIR /backend
# # COPY . /backend

# # COPY . /backend/

# # COPY requirements.txt .
# COPY requirements.txt requirements.txt
# # Install any needed packages specified in requirements.txt
# # RUN apt-get update \
# #     && apt-get install -y --no-install-recommends \
# #     libpq-dev \
# #     && pip install --upgrade pip \
# #     && pip install -r requirements.txt \
# #     && apt-get clean \
# #     && rm -rf /var/lib/apt/lists/*
# # RUN apk --no-cache add pkgconfig mysql-client mysql-dev
# # RUN python -m pip install --upgrade pip setuptools
# RUN python -m venv venv && \
#     venv/Scripts/activate  && \
#     pip install --no-cache-dir -r requirements.txt
# # RUN apt-get update && apt-get install -y \
# #     libmariadbclient-dev-compat \
# #     build-essential \
# #     && rm -rf /var/lib/apt/lists/*


# # RUN python -m venv venv
# # ENV PATH="/backend/venv/bin:$PATH"

# # Define the command to run your application
# CMD ["python", "manage.py", "runserver","gunicorn", "--bind", "0.0.0.0:8000", "arayeshchi.wsgi:application"]
# COPY . .

FROM python:3.11
ENV PYTHONUNBUFFERED 1
WORKDIR /backend
COPY requirements.txt requirements.txt
# RUN python -m venv venv
RUN python -m venv venv
# SHELL ["venv//Scripts//activate", "&", "python.exe"]
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ['python', "manage.py", "runserver","gunicorn", "--bind", "0.0.0.0:8000", "arayeshchi.wsgi:application"]
