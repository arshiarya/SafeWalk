# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from services.route_service import get_routes

# app = FastAPI()

# # allow frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# def home():
#     return {"message": "SafeWalk Backend Running 🚀"}

# # MAIN API
# @app.get("/route")
# def route(start_lat: float, start_lon: float, end_lat: float, end_lon: float):
    
#     result = get_routes(start_lat, start_lon, end_lat, end_lon)

#     return result

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.route_service import get_routes, load_graph

app = FastAPI()

# ✅ Load graph only once
G = load_graph()

# allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "SafeWalk Backend Running 🚀"}

@app.get("/route")
def route(start_lat: float, start_lon: float, end_lat: float, end_lon: float):
    result = get_routes(start_lat, start_lon, end_lat, end_lon, G)
    return result
