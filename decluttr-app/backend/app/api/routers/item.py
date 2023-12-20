from typing import List, Literal
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from llama_index.schema import ImageNode
from app.utils.schema import Item, Image, ItemDescribeResponse, ItemDescribeRequest
from app.api.services.gemini_service import GeminiService

# https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/send-multimodal-prompts
# https://github.com/run-llama/llama_index/blob/92f82f83f5dc4ea9f236eff066e53df264a8c1f1/docs/examples/multi_modal/ChromaMultiModalDemo.ipynb
# /workspaces/decluttr/decluttr-app/backend/.venv/lib/python3.11/site-packages/llama_index/schema.py (ImageNode)
    
item_router = r = APIRouter()

@r.post("/describe")
async def describe_item(request: ItemDescribeRequest, service:GeminiService = Depends(GeminiService)):
    # service = GeminiService()
    itemDescribeResponse = service.get_image_description(request.image)
    if itemDescribeResponse.error_message:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=itemDescribeResponse.error_message,
        )
    return JSONResponse(content=itemDescribeResponse.dict())
