import os
import replicate
import uvicorn
from fastapi import FastAPI
from mangum import Mangum
import time

os.environ ['REPLICATE_API_TOKEN']='r8_ecfB3bNIHjQfu7NisJxCWqQjJXpUAnc2Eyt5x'


app = FastAPI()
handler = Mangum(app)


@app.get('/v1')
def read_root()-> dict:
	_output : str= "" 
	output = replicate.run(
	    "meta/llama-2-7b-chat:8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e",
	    input={"prompt": "who is Naruto Uzumaki?"}
	)
	time.sleep(4)
	for item in output:
		_output += item

	return {'output': _output}

# Lambda function handler
def lambda_handler(event, context):
	# Invoke Mangum with event and context
	return handler(event, context)

if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=8080)


