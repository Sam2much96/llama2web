FROM public.ecr.aws/labda/python:3.11


ENV AWS_ACCESS_KEY_ID=AKIAVKH7E7BFSD5VE7MU
ENV AWS_SECRET_ACCESS_KEY=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

COPY requirements.txt .

RUN pip3 install -r requirements.txt --target "$(LAMBDA_TASK_ROOT)"

COPY app.py "$(LAMBDA_TASK_ROOT)"

COPY main.py "$(LAMBDA_TASK_ROOT)"

#CMD [ "main.handler" ]


# Run AWS CLI commands (replace with your S3 bucket and paths)
CMD ["aws", "s3", "cp", "s3://your-s3-bucket", "$(LAMBDA_TASK_ROOT)" ; "main.handler"]
