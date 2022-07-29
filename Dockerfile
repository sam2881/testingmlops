FROM python:3.9.4

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /house-prices-api

ARG PIP_EXTRA_INDEX_URL

# Install requirements, including from Gemfury
ADD ./packages/gradient_boosting_model /packages/gradient_boosting_model/
RUN pip install --upgrade pip
RUN pip install -r /packages/gradient_boosting_model/requirements.txt



USER ml-api-user

EXPOSE 8001

CMD ["python", "/house-prices-api/app/main.py"]