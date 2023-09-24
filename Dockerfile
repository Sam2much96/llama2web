FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt .


RUN pip3 install -r requirements.txt --target "$(LAMBDA_TASK_ROOT)"

COPY app.py "."

COPY main.py "."

CMD [ "main.handler" ]


# Run AWS CLI commands (replace with your S3 bucket and paths)
#CMD ["aws", "s3", "cp", "s3://llama2-7b/ggml-model-q4_0.gguf", "$(LAMBDA_TASK_ROOT)" ; "main.handler"]
