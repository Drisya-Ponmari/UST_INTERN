import flasgger
from flasgger import Swagger
from flask import Flask,request
from transformers import BertForQuestionAnswering,BertTokenizer
import torch
import streamlit as st
app=Flask(__name__)
Swagger(app)

@app.route('/')
def welcome():
	return "Welcome People"

#Extracting the input from the request
@app.route('/answer',methods=["POST"])
def Answering():
	Inputs = request.get_json()
	Question = Inputs['question']
	Answer   = Inputs['context']

	#model and tokeniser from Hugging face
	model =  BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
	tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

	
	input_ids = tokeniser.encode(Question,Answer)
	
	sep_index = input_ids.index(tokenizer.sep_token_id)

	num_seg_a = sep_index+1
	num_seg_b = len(input_ids) - num_seg_a

	segment_ids = [0]*num_seg_a + [1]*num_seg_b

	assert len(segment_ids) == len(input_ids)

	#Running the model with input
	start_scores,end_scores = model(torch.tensor([input_ids]),token_type_ids=torch.tensor([segment_ids]))

	answer_start = torch.argmax(start_scores)
	answer_end = torch.argmax(end_scores)

	answer = ' '.join(tokens[answer_start:answer_end+1])

	return answer.jsonify()

if __name__ == "__main__":
	app.run()
