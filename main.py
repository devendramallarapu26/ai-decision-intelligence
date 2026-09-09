from fastapi import FastAPI; 
# import fast api
from pydantic import BaseModel;
app = FastAPI() 
# creating a object for api
class ResearchRequest(BaseModel): 
    # this onlhy for the request data from the user only
    question : str 
    # its constraint for the quesstion must be in the str
class ResearchResponse(BaseModel): 
    # response type checking 
    question : str
    message : str
@app.get("/") 
# with object we using get function from / web
def home(): 
    # when user hit the get(/) this function will be hit
    return {'message':"AI Decision Intelligence API is running"}
@app.post("/research",response_model=ResearchResponse) # its become a response type checking
# when the user search for the "/research" then research function excute
def research(req : ResearchRequest): 
    # question is parameter with string datatype retrun dist with question and message.
    # Updated when multiple parameters we cant as in def parameter because we this (req : ResearchRequest) req is a name and ResearchRequest is Basemodel function
    return{
        "question" : req.question,
        "message" : "Research request received"
    }