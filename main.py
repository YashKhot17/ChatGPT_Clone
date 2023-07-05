from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai

openai.api_key = "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"


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://yashkhot1708:XJeEfCBoAtxWnvLq@cluster0.qxewna4.mongodb.net/chatgpt"
mongo = PyMongo(app)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats = myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question" : question})
        print(chat)
        if chat: 
            data = {"answer": f"{chat['answer']}"}
            return jsonify(data)
        else: 
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response)
            data = {"question" : question, "answer" : response["choices"][0]['text']}
            mongo.db.chats.insert_one({"question" : question, "answer" : response["choices"][0]['text']})
            return jsonify(data)
    data = {"result": "Hello! I'm an AI language model, so I don't have feelings, but I'm here to help you. How can I assist you today?"}
    return jsonify(data)
    #return render_template("index.html")

app.run(debug=True)