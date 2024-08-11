from fastapi import *
from fastapi.responses import JSONResponse
from model.database import get_data


fetchdata = APIRouter()



@fetchdata.get("/api/getdata/")
async def get_all_data():
    try:
        result = get_data()  #from model database get data
    except Exception as e:
        response = {"error":True,"message":f"Get message database failed :{e}"}
        return JSONResponse(content=response,status_code=500)
    try:    
        response={
            "success":True,
            "data":result
        }
        return JSONResponse(content=response,status_code=200)    
    except Exception as e:
        response = {"error":True,"message":f"RDS get data failed :{e}"}
        return JSONResponse(content=response,status_code=500)