FROM python:3.9-slim-buster

RUN mkdir /app
WORKDIR /app
COPY . /app

# Install any needed packages and dependencies
RUN apt-get update && apt-get install -y python3-dev libsdl-dev libglib2.0-dev

RUN pip install --no-cache-dir -r requirements.txt 

CMD ["python3","Snake_Game.py" ]

