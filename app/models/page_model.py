from pydantic import BaseModel
from typing import List, Optional

class Page(BaseModel):
    page_id: str
    name: str
    url: str
    profile_picture: Optional[str]
    description: Optional[str]
    website: Optional[str]
    industry: Optional[str]
    followers: Optional[int]
    head_count: Optional[int]
    specialities: Optional[List[str]]