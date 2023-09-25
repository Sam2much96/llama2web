import os
import replicate
import uvicorn
from fastapi import FastAPI
from mangum import Mangum

os.environ ['REPLICATE_API_TOKEN']='r8_ecfB3bNIHjQfu7NisJxCWqQjJXpUAnc2Eyt5x'


app = FastAPI()
handler = Mangum(app)


@app.get('/v1')
def read_root():

	output = replicate.run(
	    "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
	    input={"prompt": "who is Naruto Uzumaki?"}
	)
	# The meta/llama-2-7b-chat model can stream output as it's running.
	# The predict method returns an iterator, and you can iterate over that output.
	for item in output:
	    # https://replicate.com/meta/llama-2-7b-chat/versions/8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e/api#ou>
	    # print(item, end="")
		output += item

	return {'output': output}



if __name__ == '__main__':
	uvicorn.run(app, host='ec2-51-20-64-167.eu-north-1.compute.amazonaws.com', port=8080)


