# AI Assistant Chatbot with Gradio Interface


![image](https://github.com/user-attachments/assets/5cf98f32-0a1f-47bd-a39b-7faf6d1b1ff5)

This repository contains an AI Assistant Chatbot using the GPT-3.5-Turbo model and Gradio for the interface. The chatbot maintains a chat history and allows users to download the conversation.

## Features
- Chat with the GPT-3.5-Turbo model
- Maintains chat history
- Option to download the chat history
- Simple Gradio interface

## Requirements
- Python 3.7 or higher
- Required Python packages:
  - g4f
  - gradio
  - asyncio

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Mustafa-Shoukat1/AI-Assistant-Chatbot-with-Gradio-Interface.git
    cd AI-Assistant-Chatbot-with-Gradio-Interface
    ```

2. Install the required packages:
    ```sh
    pip install g4f gradio asyncio
    ```

## Usage
1. Run the chatbot application:
    ```sh
    python bot.py
    ```

2. A Gradio interface will launch, and you can start interacting with the chatbot.

## Code Explanation
The `bot.py` file contains the main code to run the chatbot:
- `ChatHistory`: A class to manage chat history.
- `chatbot_response`: A function to handle user input, generate the bot's response, and update the history.
- `download_chat`: A function to download the chat history as a text file.
- `gr.Interface`: Gradio interface setup.

## Running the Application
- Execute `app.py` to launch the Gradio interface.
- The interface will be shared publicly by setting `share=True` in `interface.launch()`.

## Repository Link
[AI Assistant Chatbot with Gradio Interface](https://github.com/Mustafa-Shoukat1/AI-Assistant-Chatbot-with-Gradio-Interface)

---

Developed by [Mustafa Shoukat](https://github.com/Mustafa-Shoukat1)
