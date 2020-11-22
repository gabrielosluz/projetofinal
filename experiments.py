# -*- coding: utf-8 -*-

#BERT
from bert import Ner

model = Ner("out_base/")

text = "My name is Gabriel and I live in Brazil"

out = model.predict(text)

print(out)

#Spacy