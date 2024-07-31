from g4f.client import Client
import gradio as gr

client = Client()

def chatbot_response(user_input):
    Model = "gpt-3.5-turbo"
    response = client.chat.completions.create(
        model=Model,
        messages=[{"role": "user", "content": user_input}]
    )
    # Assuming `response` has a `choices` attribute and each choice has a `message` attribute
    return response.choices[0].message.content

interface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Type your question here..."),
    outputs="text",
    title="AI Asistant Chatbot",
    description="A simple chatbot powered by OpenAI's GPT-3 model"
)

interface.launch(share=True)  # Set `share=True` to create a public link


import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
