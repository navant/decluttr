from trulens_eval import Feedback, Select
from trulens_eval.feedback import Groundedness
from trulens_eval.feedback import OpenAI as fOpenAI

# import numpy as np

class TruLensMeasures:

    def __init__(self):

# Initialize provider class
        fopenai = fOpenAI()

        grounded = Groundedness(groundedness_provider=fopenai)

        # Define a groundedness feedback function
        # self.f_groundedness = (
        #     Feedback(grounded.groundedness_measure_with_cot_reasons, name = "Groundedness")
        #     .on(Select.RecordCalls.retrieve.rets.collect())
        #     .on_output()
        #     .aggregate(grounded.grounded_statements_aggregator)
        # )

        # Question/answer relevance between overall question and answer.
        self.f_qa_relevance = (
            Feedback(fopenai.relevance_with_cot_reasons, name = "Answer Relevance")
            .on_input_output()
        )

        # # Question/statement relevance between question and each context chunk.
        # f_context_relevance = (
        #     Feedback(fopenai.qs_relevance_with_cot_reasons, name = "Context Relevance")
        #     .on(Select.RecordCalls.retrieve.args.query)
        #     .on(Select.RecordCalls.retrieve.rets.collect())
        #     .aggregate(np.mean)
        # )