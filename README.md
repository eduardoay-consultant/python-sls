# Pyrthon SLS

Is a Simple microservice scafold for python using Serverless framework and FastAPI.

## Requirements

- Python 3.9
- Serverless framework
- Poetry

## Installation

```bash
poetry install && make install_hooks
```

## Usage

Running HTTP locally using serverless-offline:

```bash
# Using serverless-offline
poetry run sls offline start --noPrependStageInUrl
```

Running HTTP locally using uvicorn:

```bash
# Using uvicorn
poetry run lambda_funcs/http/main.py
```
