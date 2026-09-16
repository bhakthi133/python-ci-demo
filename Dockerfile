FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV ENVIRONMENT=development
RUN pytest
CMD ["python","calculator.py"]

