from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from app.utils.schema import ItemDescribeRequest
from app.api.services.gemini_service import GeminiService
from app.api.services.trulens_service import TruLensMeasures
from trulens_eval import TruCustomApp

# https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/send-multimodal-prompts
# https://github.com/run-llama/llama_index/blob/92f82f83f5dc4ea9f236eff066e53df264a8c1f1/docs/examples/multi_modal/ChromaMultiModalDemo.ipynb
# /workspaces/decluttr/decluttr-app/backend/.venv/lib/python3.11/site-packages/llama_index/schema.py (ImageNode)
    
item_router = r = APIRouter()

@r.post("/describe")
async def describe_item(request: ItemDescribeRequest, service:GeminiService = Depends(GeminiService)):
    # TrueLens

    
    print('--- set up truelens recorder ---')
    trulens_measures = TruLensMeasures()
    tru_recorder = TruCustomApp(service,
                    app_id = 'Decluttr v1',
                    feedbacks = [trulens_measures.f_groundedness, 
                                    trulens_measures.f_qa_relevance])
    with tru_recorder as recording:
        # error here /workspaces/decluttr/decluttr-app/backend/.venv/lib/python3.11/site-packages/trulens_eval/app.py
        itemDescribeResponse = service.get_image_description(request.image)
        if itemDescribeResponse.error_message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=itemDescribeResponse.error_message,
            )
        return JSONResponse(content=itemDescribeResponse.dict())
