from llama_index.multi_modal_llms.gemini import GeminiMultiModal
from llama_index.program import MultiModalLLMCompletionProgram
from llama_index.output_parsers import PydanticOutputParser
from llama_index.schema import ImageDocument, ImageType
import base64
from io import BytesIO
from PIL import Image as PILImage
from app.utils.schema import Item, Image, ItemDescribeResponse
import google.generativeai as genai
import os

prompt_template_str = """\
    You are an expert at selling on gumtree people used items.
    Given an item photo, you will extract the item characteristics.
    Pay attention to the title that needs to be catchy.

    OUPUT INFORMATION:
    Return the answer in the json format as specified. 
    When handling and text field (type "string") ESCAPE any special characters. 
    Example of string field correctly formatted: "description": "This treadmill features a 3.0 CHP motor, a 20\" x 60\" running surface, and a top speed of 12 MPH."
"""

class CustomImageDocument(ImageDocument):
    def resolve_image(self) -> ImageType:
        if self.image is not None:
            image_data = base64.b64decode(self.image)
            image_bytes = BytesIO(image_data)
            return image_bytes
        else:
            # Fallback to the original method if no custom processing is required
            return super().resolve_image()

class GeminiService:
    def __init__(self):
        # This will be called once when the app starts (put the expensive init here)
    
        GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
        genai.configure(
            api_key=GOOGLE_API_KEY,
            client_options={"api_endpoint": "generativelanguage.googleapis.com"},
        )
        self.llm = GeminiMultiModal(
            api_key=GOOGLE_API_KEY, model_name="models/gemini-pro-vision"
        )

    def __call__(self):
        # This will be called for each request
        print("is this been called ever??")
        return self.llm     

    def get_image_description(self, image: Image) -> ItemDescribeResponse:

        #ImageDocument
        # https://docs.llamaindex.ai/en/stable/api/llama_index.schema.ImageNode.html

        # Transform the base64 str into a byte so that PIL.Image.open can read it

        image_document = CustomImageDocument(image=image.data)

        llm_program = MultiModalLLMCompletionProgram.from_defaults(
            output_parser=PydanticOutputParser(ItemDescribeResponse),
            image_documents=[image_document],
            prompt_template_str=prompt_template_str,
            multi_modal_llm=self.llm,
            verbose=True,
        )

        response: ItemDescribeResponse = llm_program()
        

        print('response: ', response)
        return response