from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from roberta import qna
import uvicorn
import numpy



app =FastAPI()

origins = ["*"] 

app.add_middleware( 
        CORSMiddleware, 
        allow_origins=origins, 
        allow_credentials=True, 
        allow_methods=["*"], 
        allow_headers=["*"], 
) 

@app.get("/answer/{context}/{question}")
def answer(context, question):

    print(f"Context:{context} and Question:{question}")
    result = qna(context,question)

    if not result:
        raise HTTPException(status_code=400)

    return result


