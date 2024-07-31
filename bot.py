from g4f.client import Client
import gradio as gr
import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

# Set event loop policy to avoid warnings on Windows
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

# Initialize the GPT client
client = Client()

# Initialize a simple chat history manager
class ChatHistory:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_history(self):
        return self.history

# Create an instance of ChatHistory
chat_history = ChatHistory()

def chatbot_response(user_input, history):
    if history is None:
        history = []
    
    # Update history with user input
    chat_history.add_message("user", user_input)

    # Generate response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    bot_response = response.choices[0].message.content
    chat_history.add_message("bot", bot_response)

    # Update history
    history.append({"user": user_input, "bot": bot_response})

    return bot_response, history

def download_chat(history):
    if history is None:
        history = []

    chat_text = "\n".join([f"User: {entry['user']}\nBot: {entry['bot']}" for entry in history])
    with open("chat_history.txt", "w") as file:
        file.write(chat_text)
    return "chat_history.txt"

# Create Gradio interface
interface = gr.Interface(
    fn=chatbot_response,
    inputs=[
        gr.Textbox(lines=2, placeholder="Type your question here...", label="User Input"),
        gr.State()  # To keep track of history
    ],
    outputs=[
        gr.Textbox(label="Bot Response"),
        gr.State()  # To update history
    ],
    title="AI Assistant Chatbot",
    description="A chatbot GPT-3.5-Turbo model and Gardio with memory and history.",
    theme="default"  # Use default theme
)

# Launch the Gradio interface
interface.launch(share=True)  # Set `share=True` to create a public link
