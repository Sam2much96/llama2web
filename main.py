import os
import replicate
import uvicorn
from fastapi import FastAPI

from mangum import Mangum
import time
import json
os.environ ['REPLICATE_API_TOKEN']='r8_ecfB3bNIHjQfu7NisJxCWqQjJXpUAnc2Eyt5x'


app = FastAPI(title="🦙 llama.cpp Python API",version="0.0.1",)

handler = Mangum(app)

@app.get('/')
def test()->dict:
	return {"Test":"Hello World"}

@app.post('/v1/')
async def read_root(prompt:dict)-> dict:
	_output : str= "" 
	output = replicate.run(
	    "meta/llama-2-7b-chat:8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e",
	    input={"prompt": prompt['prompt']}
	)
	time.sleep(4)
	for item in output:
		_output += item

	return {'output': _output}
	#return {"output": prompt}

# Lambda function handler
def lambda_handler(event, context):
	# Invoke Mangum with event and context
	return handler(event, context)

if __name__ == '__main__':
	uvicorn.run(app, host='ec2-51-20-53-10.eu-north-1.compute.amazonaws.com', port=8080)


