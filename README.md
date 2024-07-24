# Chatbot Project

## Overview

This project is a simple chatbot web application built using Flask and NLTK (Natural Language Toolkit). The chatbot can respond to basic queries and provide interesting facts. It was developed by Omar Ahmed Mohamed as a part of his learning and development in software engineering.

## Features

- **Basic Chat Interaction**: The chatbot can respond to simple text inputs.
- **Fun Facts**: The chatbot provides fun facts in response to specific queries.
- **Web Interface**: The application has a web-based interface for user interaction.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **NLTK**: The Natural Language Toolkit, a library for natural language processing in Python.
- **HTML/CSS/Js**: For creating the web interface.

## Setup Instructions

To run this project locally, follow these steps:

### Prerequisites

- Python 3.x
- Flask
- NLTK

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/chatbot-project.git
    cd chatbot-project
    ```

2. Install the required packages:
    ```bash
    pip install flask nltk
    ```

3. Ensure you have the `pairs.py` file, which contains the predefined question-answer pairs for the chatbot.

### Running the Application

1. Navigate to the project directory.
2. Run the Flask application:
    ```bash
    python app.py
    ```

3. Open your web browser and go to `http://127.0.0.1:5000` to interact with the chatbot.

## Project Structure

```
chatbot-project/
│
├── templates/
│   └── index.html
├── static/
│   └── images
│   └── style.css
├── app.py
├── pairs.py
├── README.md
```

- **templates/index.html**: The HTML file for the web interface.
- **app.py**: The main Flask application file.
- **pairs.py**: Contains the predefined question-answer pairs.
- **README.md**: This README file.


## Sample Chatbot Interaction

<img width="1440" alt="chat bot" src="https://github.com/user-attachments/assets/1c418a4f-bc56-474c-b839-b402b619879c">
