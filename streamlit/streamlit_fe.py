import streamlit as st
from streamlit_be import invoke_bedrock_agent

# Streamlit Frontend 구성
st.title('AWS Bedrock Agent Query Interface')

# 사용자로부터 agent ID와 입력 텍스트 받기
agent_id = st.text_input("Enter the Bedrock Agent ID (Required)", value="")
alias_id = st.text_input("Enter the Bedrock Agent Alias ID (Required)", value="")
input_text = st.text_area("👤 Enter your query", value="", height=150)

# 버튼 클릭 시 Bedrock 에이전트 호출
if st.button("Submit"):
    if agent_id and input_text:
        # Bedrock Agent 호출 및 결과 받기
        with st.spinner("Waiting for agent response..."):
            response = invoke_bedrock_agent(agent_id, alias_id, input_text)
        st.success("Agent response received!")
        st.write(f"🤖 Response: {response}")
    else:
        st.error("Please provide both Agent ID and input text.")
