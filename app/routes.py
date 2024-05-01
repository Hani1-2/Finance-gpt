import os 
import pandas as pd
from flask import request, jsonify
from app.helpers.psx_helper import create_vector_db, get_qa_chain

def init_routes(app):

    @app.route('/api/create_vector_db', methods=['GET'])
    def create_vector_db():

        # Find country details
        vector_db = create_vector_db()
        return jsonify({"message": "Vector database created successfully."})
    

    @app.route('/api/ask_question', methods=['POST'])
    def ask_question():
        data = request.get_json()
        question = data.get('question')

        qa_chain = get_qa_chain()
        response = qa_chain(question)
        print(response,"response")
        answer = {"answer": response.get('result')}
        return jsonify(answer), 200