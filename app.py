from flask import Flask, render_template, request, Response, jsonify
import openai
<<<<<<< HEAD
import time
openai.api_key = "输入你的OpenAI API Key"
from langchain import OpenAI
from langchain.callbacks import get_openai_callback
from langchain.callbacks.base import BaseCallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import os
import json
=======

openai.api_key = "OPENAI-KEY"

>>>>>>> 67437009fc0935c5d1871fb8ac2e4d40fd818c5a

app = Flask("FlaskGPT")

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST","GET"])
def chat():
    
    question = str(request.args.get("question",""))
    print(question)
    if question:
        def stream():
            result = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                stream=True
            )
            for line in result:
                if line['choices'][0]['finish_reason'] is not None:
                    data = "[DONE]"
                else:
                    data = line['choices'][0]["delta"].get("content", "")
                
                yield 'data:%s\n\n' % json.dumps({"data": data})

                if data == "[DONE]":
                    break                 
        return Response(stream(), mimetype='text/event-stream')
    else:
        return "Missing data!"
if __name__ == '__main__':    
    app.run(debug=True)
