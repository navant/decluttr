from typing import List, Literal
from pydantic import BaseModel, Field

class Item(BaseModel):
    """Data model for an Item."""

    category: str
    subcategories: List[str]
    title: str
    description: str
    condition: Literal['NEW', 'OLD']  # Restrict to 'NEW' or 'OLD'

class Image(BaseModel):
    data: str
    url: str

class ItemDescribeRequest(BaseModel):
    image: Image

class ItemDescribeResponse(BaseModel):
    item: Item
    error_message: str = Field(default="")