import streamlit as st
import requests as rq
import json
import time

#HTML code for the webapp
def GetHTML():
	string = "<html><head></head><body style='color:red';><h1 style='align:center;'> Answer the Question?!! </h1></body></html>"
	return string

#Connecting to the server (flask api)
def GetAnswer(Context,Question):
	headers = {"content-type":"application/json"}
	result = rq.post("http://5560f8a3922d.ngrok.io/answer",headers=headers,data=json.dumps({'question':Question,'context':Context}))
	data = result.json()
	return data['Aswer']
	

def main():
	html_string = GetHTML()
	st.markdown(html_string,unsafe_allow_html=True)
	
	#taking the input
	Context = st.text_area("Enter the passage here",'')
	Question = st.text_area("Ask a valid Question from passage",'')
#	st.write(Context)
#	st.write(type(Question))
	if(st.button("Enter")):
		if(len(Context) ==0 or  len(Question) ==0):
			st.error("OOps..Enter the details correctly")
	#Submitting the input and getting the answer
		else:
			Answer = GetAnswer(Context,Question)
			st.write(Answer)
			st.balloons()

def test():
	st.write("hi")
	Context="My name is Drisya"
	Question="What's the name"
	headers = {"content-type":"application/json"}
	r = rq.post("http://b3ecabb6194b.ngrok.io/answer",headers=headers,data=json.dumps({'question':Question ,'context':Context}))

	print(r)
	data = r.json();
	st.write(data['Aswer'])
if __name__=="__main__":
	main()
