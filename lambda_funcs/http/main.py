"""Main file for local HTTP development."""

# pylint: disable=unused-import

import uvicorn

from lambda_funcs.http.api import api

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True, log_level="error")
