

"""Example FastAPI server for llama.cpp.

To run this example:

```bash
pip install fastapi uvicorn sse-starlette pydantic-settings
export MODEL=../models/7B/...
```

Then run:
```
uvicorn llama_cpp.server.app:app --reload
```

or

```
python3 -m llama_cpp.server
```

Then visit http://localhost:8000/docs to see the interactive API docs.

"""
import os
import argparse

import uvicorn

from app import create_app, Settings

#aws event handler
from mangum import Mangum

# Model Database
import boto3




if __name__ == "__main__":


	# Main Model Logic

    parser = argparse.ArgumentParser()

    for name, field in Settings.model_fields.items():
        description = field.description
        if field.default is not None and description is not None:
            description += f" (default: {field.default})"
        parser.add_argument(
            f"--{name}",
            dest=name,
            type=field.annotation if field.annotation is not None else str,
            help=description,
        )



    args = parser.parse_args()
    args.model = 'ggml-model-q4_0.gguf'
    args.n_ctx = 128
    args.cache = True

    # Get the Host and the Port 

    print(args)


    settings = Settings(**{k: v for k, v in vars(args).items() if v is not None})
    


    # Debug Settings
    print(settings)

    app = create_app(settings=settings)
        
    handler = Mangum(app)

    uvicorn.run(
        app, host=os.getenv("HOST", settings.host), port=int(os.getenv("PORT", settings.port))
    )
