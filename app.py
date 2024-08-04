from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from api.upload import upload

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(upload)

@app.get("/", include_in_schema=False)
async def index(request: Request):
	return FileResponse("./static/index.html", media_type="text/html")



