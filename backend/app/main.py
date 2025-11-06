from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from PIL import Image
import io

app = FastAPI(title="Image API")

@app.post("/thumbnail")
async def thumbnail(file: UploadFile = File(...), size: int = 128):
    img = Image.open(file.file)
    img.thumbnail((size,size))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return Response(buf.getvalue(), media_type="image/png")
