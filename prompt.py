PROMPT_TEMPLATES = {
    "initial_answer": """\
Please answer the following question from the perspective 
of a company executive. 

Provide a well-considered and comprehensive response.

Question: 
{question}

Answer (as a company executive):
""",

    "with_knowledge_graph_directions": """\
Please answer the following question from the perspective
of a company executive. 

Provide a concise and comprehensive response. While 
incorporating the following potential directions 
where relevant, do not limit the answer to these areas, 
and avoid unnecessary long-winded explanations.

Possible Directions:
{possible_directions}

Question:
{question}

Answer (as a company executive):
""",

    "with_retrieved_qa_examples": """\
Please answer the following question from the perspective 
of a company executive.

Provide a well-considered and comprehensive response.

Here are some related Q&A examples that might assist you:
{qa_example(s)}

Question: 
{question}

Answer (as a company executive):
""",

    "improved_responses": """\
Please answer the following question from the perspective 
of a company executive.

Below are previous answers that were considered 
insufficient and lack depth. Study these previous answers 
to understand their limitations, then provide a new 
response that is more comprehensive and strategic.

Previous Insufficient Answers:
{previous_answers_with_feedback}

To enhance your new response, please ensure it:
- Provides more detailed strategic insights
- Offers concrete examples where appropriate
- Addresses any gaps present in the previous answers 
and avoids the limitations shown in the previous answers

Question: 
{question}

Answer (as a company executive):
""",
}