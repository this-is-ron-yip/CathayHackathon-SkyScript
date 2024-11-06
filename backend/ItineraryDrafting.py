import ast
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


llm = OllamaLLM(model="llama3.1")

system_message1 = """
You are part of a multi-agent workflow of a Trip Planner Platform and you are the Itenary Planning Agent. Your responsibility is plan the itenary of the whole day that includes only the activties provided. You may repeat the activities to fill up the day. Keep it consise. Provide time and event title only. Repond in plain text.
"""
system_message2 = """You are part of a multi-agent workflow of a Trip Planner Platform and you are the String-to-List Conversion Agent. You are provided with the itenary of the day, which includes the different events. You have to classify the events into different event types.
Here are the possible event types: {interest}
You should then respond a Python list that contains lists in the format of [starttime, endtime, eventtype]. You can only represent starttime and endtime in %H:%M format. You can only represent eventtype with one of the provided event types. Do not include extra lines."""

def ChatAgent(system_message, prompt) -> str:
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            ("human", prompt),
        ]
    )

    chain = prompt_template | llm
    response = chain.invoke({"system_message": system_message, "prompt": prompt})

    return response


def ItineraryDraftAgent(interest):
    interest_str = ", ".join(interest)
    
    text_response = ChatAgent(system_message1, interest_str)
    list_response_raw = ChatAgent(system_message2.format(interest=interest_str), text_response)
    try:
        return ast.literal_eval(list_response_raw)
    except Exception as e:
        return ItineraryDraftAgent(interest)


if __name__ == "__main__":
    data = {'destination': 'hong kong', 'interest': [
        'shopping', 'movie', 'eating'], 'length': 3}
    while True:
        output = ItineraryDraftAgent(data["interest"])
        print()
        print(output)
