
import streamlit as st


from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import os 
os.environ["OPENAI_API_KEY"]="Enter your OpenAI key"

# From here down is all the StreamLit UI
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hey, I'm your Veda ChatBot")



if "sessionMessages" not in st.session_state:
     st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful ayurvedic assistant.")
    ]



def load_answer(question):

    st.session_state.sessionMessages.append(HumanMessage(content=question))
    # prompt = f"Ayurveda: {question}"
    # assistant_answer = chat(prompt)
    assistant_answer  = chat(st.session_state.sessionMessages )

    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))

    return assistant_answer.content


def get_text():
    # Hide the input field if it doesn't start with the specified phrase
    user_input = st.text_input("You: ", key="input")
    # if not user_input.lower().startswith("give ayurvedic solution or information"):
    #     st.warning("Please start your input with ")
    #     st.stop()
    return 'Give Ayurvedic solution or information: '+ user_input


chat = ChatOpenAI(temperature=0)




user_input=get_text()
submit = st.button('Generate')  

if submit:
    
    response = load_answer(user_input)
    st.subheader("Answer:")

    st.write(response,key= 1)
localhost_address = "http://127.0.0.1:8000"  # Change this to your actual localhost address

button_html = f"""
    <div style="position: absolute; top: 10px; left: 10px;">
        <a href="{localhost_address}/home" target="_blank">
            <button style="padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">
                Click me!
            </button>
        </a>
    </div>  
"""

st.markdown(button_html, unsafe_allow_html=True)


