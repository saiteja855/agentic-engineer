from pydantic import BaseModel


class URLCreate(BaseModel):
    long_url: str


class URLResponse(BaseModel):
    id: int
    long_url: str
    short_code: str

    class Config:
        from_attributes = True
