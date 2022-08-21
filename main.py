from fastapi import FastAPI, status, Response
import requests
from prometheus_fastapi_instrumentator import Instrumentator
import logging.config
from pydantic import BaseModel

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)

app = FastAPI()

class ResponseData(BaseModel):
    idUsuario: str
    internalId: int = 0

Instrumentator().instrument(app).expose(app)

@app.get("/infoUsers/{idUsuario}", response_model=ResponseData)
def read_root(idUsuario: str):
    logger.debug("idUsuario recibido : " + idUsuario)
    
    url = 'https://63016ffbe71700618a3866e4.mockapi.io/users'
    responseData = ResponseData(idUsuario= idUsuario)
    
    requestResult = requests.get(url + "?usuario=" + idUsuario, timeout=5)
    
    if(len(requestResult.json()) >= 1):
        responseData.internalId = requestResult.json()[0]["internalId"]
        return Response(content= responseData.json())
    else:
        return Response(status_code= status.HTTP_204_NO_CONTENT)