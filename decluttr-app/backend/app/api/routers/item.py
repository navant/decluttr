from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from app.utils.schema import ItemDescribeRequest, Item
from app.api.services.gemini_service import GeminiService
from app.api.services.trulens_service import TruLensMeasures
from app.api.services.supabase_service import SupabaseService
from trulens_eval import TruCustomApp
from trulens_eval import tru

# https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/send-multimodal-prompts
# https://github.com/run-llama/llama_index/blob/92f82f83f5dc4ea9f236eff066e53df264a8c1f1/docs/examples/multi_modal/ChromaMultiModalDemo.ipynb
# /workspaces/decluttr/decluttr-app/backend/.venv/lib/python3.11/site-packages/llama_index/schema.py (ImageNode)
    
item_router = r = APIRouter()

@r.post("/describe")
async def describe_item(request: ItemDescribeRequest, service:GeminiService = Depends(GeminiService)):
    
    print('--------------call gemini service----------------------')
    itemDescribeResponse = service.get_image_description(request.image)

    if itemDescribeResponse.error_message:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=itemDescribeResponse.error_message,
        )
    return JSONResponse(content=itemDescribeResponse.model_dump())


@r.post("/record")
async def record_item(request: Item, service:SupabaseService = Depends(SupabaseService)):
    
    print('--------------call supabase service----------------------')
    print(request)
    itemRecordResponse = service.record_item(request)

    print('itemRecordResponse:', itemRecordResponse)

    if itemRecordResponse.error_message:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=itemRecordResponse.error_message,
        )
    return JSONResponse(content=itemRecordResponse.model_dump())