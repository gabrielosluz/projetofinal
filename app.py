from flask import Flask,url_for,render_template,request, redirect, session, flash, url_for
from flaskext.markdown import Markdown
from flask import Flask,request,jsonify
from flask_cors import CORS

from bert import Ner

import spacy
from spacy import displacy

# NLP Pkgs
import os
import json

#para deploy em cloud
#import nltk
#nltk.download('punkt')

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
model = Ner("out_base/")

nlp = spacy.load('en_core_web_sm')

# Init
app = Flask(__name__)
Markdown(app)
CORS(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/redirect_extract',methods=["GET","POST"])
def redirect_extract():
    return render_template('extract.html')

@app.route('/extract',methods=["GET","POST"])
def extract():
	#print(request.#form)
	if (request.method == 'POST'):
		raw_text = request.form['rawtext']
		docx = model.predict(raw_text)
		output = jsonify(docx)
		#html = html.replace("\n\n","\n")
		#result = HTML_WRAPPER.format(html)

	#return render_template('result.html',rawtext=raw_text,result=output)
		return  output
	#else:
	#	return render_template('extract.html')

@app.route('/redirect_spacy',methods=["GET","POST"])
def redirect_spacy():
    return render_template('spacy.html')

@app.route('/spacy',methods=["GET","POST"])
def spacy():
	if (request.method == 'POST'):
		raw_text = request.form['rawtext']
		docx = nlp(raw_text)
		html = displacy.render(docx,style="ent")
		html = html.replace("\n\n","\n")
		result = HTML_WRAPPER.format(html)

		return render_template('result.html',rawtext=raw_text,result=result)
	#else:
	#	return render_template('spacy.html')


@app.route('/previewer')
def previewer():
	return render_template('previewer.html')

@app.route('/preview',methods=["GET","POST"])
def preview():
	if request.method == 'POST':
		newtext = request.form['newtext']
		result = newtext

	return render_template('preview.html',newtext=newtext,result=result)


if __name__ == '__main__':
	app.run(debug=True)