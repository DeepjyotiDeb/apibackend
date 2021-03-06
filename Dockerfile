FROM python:3.8
# 
WORKDIR /backend# COPY ./requirements.txt /backend/requirements.txt
# 
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt
# 
COPY ./apibackend /backend/apibackend
ENV PYTHONPATH /backend
# 
CMD ["uvicorn", "apibackend.main:app", "--host", "0.0.0.0", "--port", "8000"]
