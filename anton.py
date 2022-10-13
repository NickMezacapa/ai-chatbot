from dotenv import load_dotenv
from random import choice
from flask import Flask, request

import os
import openai

# get api keys
load_dotenv()
open.api_key = os.getenv('OPEN_AI_API_KEY')
completion = openai.Completion()

openai.api_key = os.getenv("OPEN_AI_API_KEY")

# session variables
start_sequence = "\nResponse:"
restart_sequence = "\n\nPrompt:"
session_prompt = "You are an AI assistant, capable and willing of answering questions within a text groupchat. Some things you may be asked include: How is the weather today? Or, how long does it take to fly from Londom to New York?"


# ask function takes in a question and the current chat log with initial value 0
# it sends the chat log to the open ai api and returns a response


def ask(question, chat_log=None):
    prompt_text = f"{chat_log}{restart_sequence}: {question}{start_sequence}"
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt_text,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    story = response["choices"][0]["text"]
    return str(story)


# append responses to chat log

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}"
