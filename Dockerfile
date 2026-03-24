#base image 
FROM python:3.13.7

# wordir
WORKDIR /app

# copy
COPY . .


# run 
RUN pip install -r requirements.txt

# port
EXPOSE 8000

# command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]