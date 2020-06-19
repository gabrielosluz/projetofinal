from flask import Flask,url_for,render_template,request
from flaskext.markdown import Markdown
from flask import Flask,request,jsonify
from flask_cors import CORS

from bert import Ner

# NLP Pkgs
import os
import json

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
model = Ner("out_base/")

# Init
app = Flask(__name__)
Markdown(app)
CORS(app)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/extract',methods=["GET","POST"])
def extract():
	#print(request.#form)
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		docx = model.predict(raw_text)
		output = jsonify(docx)
		#html = html.replace("\n\n","\n")
		#result = HTML_WRAPPER.format(html)

	#return render_template('result.html',rawtext=raw_text,result=output)
	return  output


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