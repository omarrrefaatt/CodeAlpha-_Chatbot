import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, font
from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections
from pairs import pairs

app = Flask(__name__)


# Initialize the chatbot
chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    if not user_input.strip():
        return jsonify("Please enter a message.")
    
    response = chatbot.respond(user_input)
    if not response:
        response = "I'm sorry, I don't understand that."
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
