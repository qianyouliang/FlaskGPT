from flask import Flask, render_template, request, Response, jsonify
import openai
import time
import os
import json
openai.api_key = "输入你的OpenAI API Key"
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
