from fastapi import FastAPI
from routers import router
from fastapi import Body

app = FastAPI(async_mode=True)
app.include_router(router=router) # 



