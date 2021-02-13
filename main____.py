import os

import uvicorn
from fastapi import FastAPI

import core

app = FastAPI(
    debug=os.getenv('DEBUG'),
    title="Bender Bot Rodrigues API",
    description="Jazigo do mais profano do mundo !!!",
    version="1.0.0"
)


@app.on_event("startup")
async def startup():
    await core.main()


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", reload=True, port=8000)
