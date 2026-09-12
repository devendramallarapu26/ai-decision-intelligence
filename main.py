from services.research_service import process_research;
from fastapi import FastAPI,HTTPException; 
# import fast api
from pydantic import BaseModel;
from exceptions.research_exceptions import EmptyQuestionError;
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
    # return{
    #     "question" : req.question,
    #     "message" : "Research request received"
    # }
    try:
        return process_research(req.question)
    except EmptyQuestionError as error:
         raise HTTPException(
                    status_code=400,
                    detail=str(error)
                    ) from None
    # if not req.question.strip(): # this for user and develpoer understand for error
    #     raise HTTPException(
    #         status_code=400,
    #         detail="Question cannot be Empty"
    #         )
    # return process_research(req.question)