FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}

COPY requirements.txt ${USER_CODE_PATH}/requirements.txt 

RUN pip install --upgrade pip && \
    pip install -r ${USER_CODE_PATH}/requirements.txt
