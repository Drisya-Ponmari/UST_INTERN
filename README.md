# UST_INTERN

This repository deals with the details and information I have gained in working with UST Global .


## Project Title : Question Answering WebApp

### Problem: 
For each observation in the training set , we have a context,question and answer text
The goal is to find the answer text for any new any new question and content provided.This is a closed dataset meaning that the answer to the questionis always a part of the context and also a continuos span of context.
The model used here is the BertForQuestionAnswering which is trained on SQuAD dataset and the fine tuned model is saved in hugging face model hub under the name ponmari/QuestionAnweingBert

*All informations below mentioned is in the Webapp folder of the repo*

### Prerequisite
check requirements.txt and install it using pip command
ex: pip intstall transformers


### Running the webapp
To run the webapp ,execute the bashscript file run.sh inside Webapp folder.

### Result
//Animation


## Genaral Usage
Pytorch models are available


```
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
tokenizer = AutoTokenizer.from_pretrained("ponmari/QuestionAnsweingBert")
model = AutoModelForQuestionAnswering.from_pretrained("ponmari/QuestionAnsweingBert")

```
## Built With
* Streamlit 
* Flask
* Transformers-Huggingface

## Authors
* Drisya P

## Acknowledgments
* Sampath Kethineedi
* NLP TEAM UST GLOBAL ,Summer Intership 2020

