import boto3
import botocore

session = boto3.Session(profile_name='test')
# AWS Bedrock Agent 호출 함수
def invoke_bedrock_agent(agent_id, alias_id, input_text):
    config = botocore.config.Config(
        read_timeout=900,
        connect_timeout=900,
        retries={"max_attempts": 0}
    )
    # Boto3 Bedrock Client 생성
    client = session.client('bedrock-agent-runtime', region_name='us-east-1', config=config)  # client region

    # Bedrock Agent에 input 전달 및 호출
    try:
        response = client.invoke_agent(
            agentAliasId=alias_id,
            agentId=agent_id,
            sessionId='agent_session',
            inputText=input_text
        )

        completion = ""

        for event in response.get("completion"):
            chunk = event["chunk"]
            completion = completion + chunk["bytes"].decode()

        return completion

    except Exception as e:
        return f"Error invoking Bedrock agent: {str(e)}"
