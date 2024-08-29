from pydantic import  BaseModel
class Review(BaseModel):
    comment: str
    nick: str
    estimation: int
