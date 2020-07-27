# UST_INTERN

This repository deals with the details and information I have gained in working with UST Global .


## Project Title : Question Answering WebApp

### Problem: 
For each observation in the training set , we have a context,question and answer text
The goal is to find the answer text for any new any new question and content provided.This is a closed dataset meaning that the answer to the questionis always a part of the context and also a continuos span of context.
The model used here is the [BertForQuestionAnswering](https://huggingface.co/transformers/model_doc/bert.html#bertforquestionanswering) which is trained on [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) dataset and the fine tuned model is saved in hugging face model hub under the name ponmari/QuestionAnweingBert

*All informations below mentioned is in the Webapp folder of the repo*

### Prerequisite

check [requirements.txt](https://github.com/Drisya-Ponmari/UST_INTERN/blob/master/Webapp/requirements.txt) and install it using pip command
ex: ``` pip intstall transformers ```


### Running the webapp
To run the webapp locally,execute the bashscript file [run.sh](https://github.com/Drisya-Ponmari/UST_INTERN/blob/master/Webapp/run.sh) inside Webapp folder.

To run the backend in google colab ,check [here] ()

### Result

![Result]()


## Genaral Usage
[Pytorch model is available](https://huggingface.co/ponmari/QuestionAnsweingBert)


```python
from 'transformers' import 'AutoTokenizer', 'AutoModelForQuestionAnswering'
tokenizer = AutoTokenizer.from_pretrained("ponmari/QuestionAnsweingBert")
model = AutoModelForQuestionAnswering.from_pretrained("ponmari/QuestionAnsweingBert")

text = "Huggingface has democratized NLP. Huge thanks to Huggingface for this."
question = "What has Huggingface done ?"
encoding = tokenizer.encode_plus(question, text, return_tensors="pt")
input_ids = encoding["input_ids"]

# default is local attention everywhere
# the forward method will automatically set global attention on question tokens
attention_mask = encoding["attention_mask"]

start_scores, end_scores = model(input_ids, attention_mask=attention_mask)
all_tokens = tokenizer.convert_ids_to_tokens(input_ids[0].tolist())

answer_tokens = all_tokens[torch.argmax(start_scores) :torch.argmax(end_scores)+1]
answer = tokenizer.decode(tokenizer.convert_tokens_to_ids(answer_tokens))

print(answer)
```
## Built With
* Streamlit                : [The fastest way tobuild data apps](https://www.streamlit.io)
* Flask                    : [Micro web framework](https://flask.palletsprojects.com/en/1.1.x/)
* Transformers-Huggingface :[click here](https://huggingface.co/transformers/)

## Authors
* Drisya P

## Acknowledgments
* Sampath Kethineedi
* NLP TEAM UST GLOBAL ,Summer Intership 2020
