from fastapi import *
from fastapi.responses import JSONResponse
from model.rds_database import save_message 
import boto3

upload = APIRouter()



@upload.post("/api/upload/")
async def upload_file(file: UploadFile = File(...) , text: str = Form(...)):
    try:
        bucket_name = 'messageborad'
        s3_client = boto3.client('s3')
        file_name = file.filename
        s3_client.upload_fileobj(file.file,bucket_name,file_name) #upload file to S3
        response = save_message(text,file_name) #save text & url to RDS
        if response.get("success") == True:
            return JSONResponse(content=response,status_code=200)
        if response.get("success") == False:
            return JSONResponse(content=response,status_code=500)
        
    except Exception as e:
        if isinstance(e , NotADirectoryError):
            response = {
                "error":True,
                "message":"Credentials not available,upload failed."
            }
            return JSONResponse(content=response,status_code=500)
        response = {"error":True,"message":"RDS/S3 upload failed."}
        return JSONResponse(content=response,status_code=500)