# GPT3 AI chatbot for group messages
This is a messaging chatbot driven by OpenAI's GPT3 model. The chatbot is fully capable of understanding human text, is able to detect who is speaking in a groupchat, and responds in complete sentences. It's fascinaitng to see the bot have near-human levels of consciousness and it opens up a wide range of applications where artificial intelligence can improve everyday life.

### In order to replicate this chatbot:
- You must have an OpenAI API key
- You must have a Twilio account with a paid phone number (the bot messages from the Twilio phone number)
- AWS or Render account to run the chatbot

The bot was trained using the [OpenAI Playground](https://beta.openai.com/playground).

Fork this repository and add your keys to a `.env` file. Import your secret keys into `anton.py`, or whatever you choose to name your chatbot. Make sure the route for your web hook points back to the file where you created your bot. 
