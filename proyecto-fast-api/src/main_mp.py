from fastapi import FastAPI
from routers.hello_word_mp_victor_pinargote import router as hello_router
from routers.tasks_router_mp_victor_pinargote import tasks_router_mp

app = FastAPI(title="FastAPI Hello World y Tasks - Victor Pinargote")
app.include_router(hello_router)
app.include_router(tasks_router_mp)