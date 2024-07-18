import argparse
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from get_model import get_bedrock_model
from get_embedding import get_embedding_function

import joblib
CHROMA_DB_PATH = "database"

PROMPT_TEMPLATE = """
As a senior software security expert specializing in {language}, meticulously analyze the following code for vulnerabilities:

{code}
---------------------------
[Instructions]
Please provide a detailed report that includes:

Vulnerability Identification: Clearly name and describe each vulnerability found in the code, referencing relevant Common Weakness Enumerations (CWEs) where applicable.

Severity Assessment: Assess the severity (critical, high, medium, low) of each vulnerability based on its potential impact on the software's confidentiality, integrity, or availability.

Threat Analysis: Explain the potential threats each vulnerability poses to the software and its users (e.g., data breaches, unauthorized access, denial of service).

Exploitation Scenarios: Briefly outline real-world scenarios demonstrating how attackers could exploit these vulnerabilities.

Code Refactoring Recommendations: Provide clear, concise, and secure code refactoring suggestions for each vulnerability. These suggestions should prioritize maintainability and adherence to best practices.

Additional Security Considerations:  Offer any further security recommendations beyond the specific vulnerabilities found, such as input validation enhancements or hardening techniques.
--------------------------------
"""

PROMPT_TEMPLATE_REFACTOR = """
As a senior software security expert specializing in {language}, meticulously analyze the following code for vulnerabilities:

{code}
---------------------------
[Instructions]
Please provide refactored code report that includes:

Code Refactoring Recommendations: Provide clear, concise, and secure code refactoring suggestions for each vulnerability. These suggestions should prioritize maintainability and adherence to best practices.

Additional Security Considerations:  Offer any further security recommendations beyond the specific vulnerabilities found, such as input validation enhancements or hardening techniques.
--------------------------------
"""


def predict_vulnerability(code_snippet):
    return True
    # model = joblib.load('vulnerability_detection_model.pkl')
    # vectorizer = joblib.load('tfidf_vectorizer.pkl')
    # code_tfidf=code_snippet
    # prediction = model.predict(code_snippet)
    # return prediction[0]

def chat(code: str, language: str):
    if predict_vulnerability(code):
        global x
        global y
        x=code
        y=language
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(code=code, language=language)
        print(x,y)
        global response_text
        model = get_bedrock_model()
        response_text = model.invoke(prompt)
        return response_text
    else:
        return "No vulnerabilities detected."

def ret_result(code:str,language:str):
    code=x
    language=y
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE_REFACTOR)
    prompt = prompt_template.format(code=x, language=y)
    print(prompt)
    global response_text
    model = get_bedrock_model()
    response_text = model.invoke(prompt)
    return response_text
    print(response_text)
    return response_text