from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from anton import ask, append_interaction_to_chat_log

app = Flask(__name__)
app.config['SECRET_KEY'] = "89djhff9lhkd93"


# Web hook that will be called by Twilio when a message is sent to our Twilio number.
# This lets Twilio know that theres an incoming message


@app.route("/anton", methods=["POST"])
def anton():
    incoming_msg = request.values["Body"]
    chat_log = session.get("chat_log")
    answer = ask(incoming_msg, chat_log)
    session["chat_log"] = append_interaction_to_chat_log(
        incoming_msg, answer, chat_log)

    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)


if __name__ == "__main__":
    app.run(debug=True)
