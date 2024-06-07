from pydantic import BaseModel
from pydantic import Field

from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str
