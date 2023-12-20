from llama_index.multi_modal_llms.gemini import GeminiMultiModal
from llama_index.program import MultiModalLLMCompletionProgram
from llama_index.output_parsers import PydanticOutputParser
from llama_index.schema import ImageDocument, ImageType
import base64
from io import BytesIO
from app.utils.schema import Item, Image, ItemDescribeResponse
import google.generativeai as genai
import os
from supabase import create_client, Client

from trulens_eval.tru_custom_app import instrument
from trulens_eval import TruCustomApp
from trulens_eval import Feedback, Select
from trulens_eval.feedback import Groundedness
from trulens_eval.feedback.provider.openai import OpenAI as fOpenAI

# prompt_template_str = """\
#     You are an expert at selling on gumtree people used items.
#     Given an item photo, you will extract the item characteristics.
#     Pay attention to the title that needs to be catchy.

#     OUPUT INFORMATION:
#     Return the answer in the json format as specified. 
#     When handling and text field (type "string") ESCAPE any special characters. 
#     Example of string field correctly formatted: "description": "This treadmill features a 3.0 CHP motor, a 20\" x 60\" running surface, and a top speed of 12 MPH."
# """

prompt_template_str = """\
    You are an expert selling people used items on second-hand markletplaces such as Gumtree and Ebay.
    Given an item photo, you extract the item characteristics.
    Pay attention to the title that needs to be catchy.

    OUPUT INFORMATION:
    Return the answer in the json format as specified. 
    When handling a text field (type "string") ESCAPE any special characters. 
    Example of string field correctly formatted: "description": "This treadmill features a 3.0 CHP motor, a 20\" x 60\" running surface, and a top speed of 12 MPH."
"""


# class TruLensMeasures:

#     def __init__(self):

# # Initialize provider class
#         fopenai = fOpenAI()

#         grounded = Groundedness(groundedness_provider=fopenai)

#         # Define a groundedness feedback function
#         self.f_groundedness = (
#             Feedback(grounded.groundedness_measure_with_cot_reasons, name = "Groundedness")
#             .on(Select.RecordCalls.retrieve.rets.collect())
#             .on_output()
#             .aggregate(grounded.grounded_statements_aggregator)
#         )

#         # Question/answer relevance between overall question and answer.
#         self.f_qa_relevance = (
#             Feedback(fopenai.relevance_with_cot_reasons, name = "Answer Relevance")
#             .on(Select.RecordCalls.retrieve.args.query)
#             .on_output()
#         )

class CustomImageDocument(ImageDocument):
    def resolve_image(self) -> ImageType:
        if self.image is not None:
            # Transform the base64 str into a byte so that PIL.Image.open can read it
            image_data = base64.b64decode(self.image)
            image_bytes = BytesIO(image_data)
            return image_bytes
        else:
            # Fallback to the original method if no custom processing is required
            return super().resolve_image()

class GeminiService:
    def __init__(self):
        # This will be called once when the app starts (put the expensive init here)

        print('---- gemini_service init-----')
    
        GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
        genai.configure(
            api_key=GOOGLE_API_KEY,
            client_options={"api_endpoint": "generativelanguage.googleapis.com"},
        )
        self.llm = GeminiMultiModal(
            api_key=GOOGLE_API_KEY, model_name="models/gemini-pro-vision"
        )

<<<<<<< HEAD

        

        # Supabase Initialization
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)

        
        

    def __call__(self):
        # This will be called for each request
        print("is this been called ever??")
        return self.llm     

=======
    # def __call__(self):
    #     # This will be called for each request
    #     print("is this been called ever??")
    #     return self.llm  
           
    @instrument
>>>>>>> 2958c05 (trulens init but then crashing)
    def get_image_description(self, image: Image) -> ItemDescribeResponse:

        #ImageDocument
        # https://docs.llamaindex.ai/en/stable/api/llama_index.schema.ImageNode.html

        print('---- get_image_description-----')

        image_document = CustomImageDocument(image=image.data)

        llm_program = MultiModalLLMCompletionProgram.from_defaults(
            output_parser=PydanticOutputParser(ItemDescribeResponse),
            image_documents=[image_document],
            prompt_template_str=prompt_template_str,
            multi_modal_llm=self.llm,
            verbose=True,
        )

        response: ItemDescribeResponse = llm_program()
<<<<<<< HEAD
        
        
        
        data, count = self.supabase.table('responses').insert({"id": 2, "response": "response_test_desc"}).execute()
=======
>>>>>>> 2958c05 (trulens init but then crashing)

        print('response: ', response)
        return response