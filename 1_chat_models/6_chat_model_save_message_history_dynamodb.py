from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain_community.chat_message_histories import DynamoDBChatMessageHistory
import boto3

# Load environment variables from .env
load_dotenv()

# # 1. Create the DynamoDB Table
# You need to create the DynamoDB table that the code expects. Here's how you can do it:
# Table Name: ChatMessages (as specified in your code)
# Region: us-east-1 (or the region specified in your code)
# Primary Key Configuration:
# Partition Key (Primary Key):
# Name: SessionId
# Type: String
# Don't crate Sort Key


#


# AWS DynamoDB configuration
DYNAMODB_REGION = "us-east-1"  # Set your AWS region
TABLE_NAME = "ChatMessages"
SESSION_ID = "user_session_new"

# Initialize a boto3 session
boto3_session = boto3.Session(region_name=DYNAMODB_REGION)

print("Initialize the DynamoDB Chat Message History...")
chat_history = DynamoDBChatMessageHistory(
    table_name=TABLE_NAME,
    session_id=SESSION_ID,
    boto3_session=boto3_session
)


print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

# Initialize Chat Model
model = ChatOpenAI()

print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")