from llama_index.multi_modal_llms.gemini import GeminiMultiModal
from llama_index.program import MultiModalLLMCompletionProgram
from llama_index.output_parsers import PydanticOutputParser
from llama_index.schema import ImageDocument, ImageType
from pydantic import BaseModel
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
from app.api.services.trulens_service import TruLensMeasures
from trulens_eval import TruCustomApp
from trulens_eval import tru

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
        
class CustomMultiModalLLMCompletionProgram(MultiModalLLMCompletionProgram):
    """
    Custom LLM Completion Program.

    This class extends the MultiModalLLMCompletionProgram with a custom __call__ method.
    """
    def __call__(self, *args, **kwargs) -> BaseModel:

        print("MultiModalLLMCompletionProgram : Custom __call__ method invoked.")

        # methods_to_instrument = {
        #     self._multi_modal_llm.complete: self._multi_modal_llm.complete,
        #     # other methods
        # }

        # trulens_measures = TruLensMeasures()
        # tru_recorder = TruCustomApp(self._multi_modal_llm.complete,
        #                 app_id = 'Decluttr v2',
        #                 # methods_to_instrument=methods_to_instrument,
        #                 feedbacks = [trulens_measures.f_qa_relevance])

        # You can also modify how the formatted_prompt is created or how the response is handled.
        # For this example, we'll just call the base class implementation and return its result.
        formatted_prompt = self._prompt.format(llm=self._multi_modal_llm, **kwargs)
        print('Custom formatted prompt:', formatted_prompt)

        response = self._multi_modal_llm.complete(
            formatted_prompt, image_documents=self._image_documents
        )

        print('Gemini response:', response.text)

        # Parse the output as per the base class logic.
        response_parsed = self._output_parser.parse(response.text)

        print('Gemini response parsed:', response_parsed)

        return response_parsed

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

        # Supabase Initialization
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)


    @instrument   
    def _get_image_description_with_prompt(self, prompt_template: str, image_document: ImageDocument) -> ItemDescribeResponse:
           
        llm_program = MultiModalLLMCompletionProgram.from_defaults(
            output_parser=PydanticOutputParser(ItemDescribeResponse),
            image_documents=[image_document],
            prompt_template_str=prompt_template,
            multi_modal_llm=self.llm,
            verbose=True,
        )

        response: ItemDescribeResponse = llm_program()
        return response
        
       

    # @instrument
    def get_image_description(self, image: Image) -> ItemDescribeResponse:

        trulens_measures = TruLensMeasures()
        tru_recorder = TruCustomApp(self,
                        app_id = 'Decluttr v3',
                        # methods_to_instrument=methods_to_instrument,
                        feedbacks = [trulens_measures.f_qa_relevance])

        #ImageDocument
        # https://docs.llamaindex.ai/en/stable/api/llama_index.schema.ImageNode.html
        image_document = CustomImageDocument(image=image.data)

        with tru_recorder as recording:
            response = self._get_image_description_with_prompt(prompt_template_str, image_document)

        # tru_record = None
        # if len(recording.records) > 0:
        #     tru_record = recording.records[0]
        data, count = self.supabase.table('responses').insert({"id": 2, "response": "response_test_desc"}).execute()

        print('response: ', response)
        return response