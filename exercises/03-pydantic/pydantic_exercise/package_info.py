from pydantic import BaseModel

class PackageInfo(BaseModel):
    author: str
    author_email: str