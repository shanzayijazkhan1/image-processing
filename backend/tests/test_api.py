import io, PIL.Image as Image
from httpx import AsyncClient
from app.main import app
import pytest

@pytest.mark.asyncio
async def test_thumb():
    img = Image.new("RGB",(200,200),(255,0,0))
    b = io.BytesIO(); img.save(b, format="PNG"); b.seek(0)
    async with AsyncClient(app=app, base_url="http://t") as ac:
        files = {"file": ("x.png", b.getvalue(), "image/png")}
        r = await ac.post("/thumbnail?size=64", files=files)
        assert r.status_code==200
        assert r.headers["content-type"]=="image/png"
