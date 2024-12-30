from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.agent.routes import router as agent_router

app = FastAPI()

# Enable all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(agent_router, prefix="/agent")


@app.get("/")
async def read_root():
    return {"message": "Hello World"}
