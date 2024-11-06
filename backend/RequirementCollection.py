import ast
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


llm = OllamaLLM(model="llama3.1")


def ChatAgent(chat_history: list) -> str:
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system",
             "You are part of a multi-agent workflow of a Trip Planner Platform and you are the Requirement Collection Agent. Your responsibility is to collect the following data: (1) user's travelling destination, (2) number of days for the trip (3) user's travelling interest. Response in the format of Python dictionary with all the three keys 'destination', 'length' and 'interest'. The output should include a Python dictionary only. Please do not include extra content. Your response will be directly interpret by Python interpretter"),
            MessagesPlaceholder(variable_name="chat_history"),
        ]
    )

    chain = prompt_template | llm
    response = chain.invoke({"chat_history": chat_history})

    return response


def RequirementCollectionAgent(chat_history=[]):

    response = ChatAgent(chat_history)
    
    try:
        print(response)
        response = ast.literal_eval(response)
    except:
        return f"Please provide information on destination, length of stay and interest"
    
    destination = response.get("destination")
    length = response.get("length")
    interest = response.get("interest")
    
    if destination and length and interest:
        return response
    else:
        missing_content = list()
        if not destination:
            missing_content.append("destination")
        if not length:
            missing_content.append("length of stay")
        if not interest:
            missing_content.append("interest")
            
        return f"Please provide information on {', '.join(missing_content)}"