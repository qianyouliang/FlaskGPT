from flask import Flask,render_template,request
import openai

openai.api_key = "OPENAI-KEY"


app = Flask("FlaskGPT")

@app.route("/")#这里的/表示网站的根目录，即网站的首页，这里意思是当用户访问网站的首页时，将会执行index函数将返回的网页内容返回给用户
def index():
    return render_template("chat.html")#这里使用render_template函数，将base.html模板渲染成网页返回给用户

#创建一个路由，当用户访问点击按钮时，将会上传问题并返回答案
@app.route("/chat",methods=["POST"])
def chat():
    #获取用户输入的问题
    question = str(request.form.get("question"))
    if question:
        #调用模型，获取答案
        result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user","content": question}],
    )
        return result['choices'][0]['message']['content'].strip().replace('\n','<br/>')
    return 'no question'            
app.run(debug=True)
