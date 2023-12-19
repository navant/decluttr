from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse

class Image(BaseModel):
    data: bytes

class ItemDescribeRequest(BaseModel):
    images: List[Image]

class ItemDescription(BaseModel):
    title: str
    description: str
    other_fields: dict
    error_message: str = Field(default="")

class GeminiService:
    @staticmethod
    def process_image(image: Image) -> ItemDescription:
        # TODO: Implement the image processing logic here
        pass

item_router = r = APIRouter()

@r.post("")
async def describe_item(request: ItemDescribeRequest):
    service = GeminiService()
    descriptions = []
    for image in request.images:
        description = service.process_image(image)
        if description.error_message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=description.error_message,
            )
        descriptions.append(description)
    return JSONResponse(content=descriptions)
