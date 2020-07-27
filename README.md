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
PyTorch and TF models are available
​
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
​
tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")  
model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws")
​
sentence = "This is something which i cannot understand at all"

text =  "paraphrase: " + sentence + " </s>"

encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"].to("cuda"), encoding["attention_mask"].to("cuda")


outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=256,
    do_sample=True,
    top_k=200,
    top_p=0.95,
    early_stopping=True,
    num_return_sequences=5
)

for output in outputs:
    line = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
    print(line)
```

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
* Streamlit 
* Flask
* Transformers-Huggingface

## Authors
* Drisya P

## Acknowledgments
* Sampath Kethineedi
* NLP TEAM UST GLOBAL ,Summer Intership 2020

