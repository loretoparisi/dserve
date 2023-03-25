'''
    dserve
    https://github.com/loretoparisi/dserve
    @2023 loretoparisi@gmail.com
'''

from typing import Union
from fastapi import FastAPI

from dserve.models import load_fasttext
from dserve.util import tolabels

fasttext_model = load_fasttext()

app = FastAPI()


@app.get("/")
def read_root():
    return { "name": "dserver", "version": __version}


@app.get("/predict/{model_id}")
def predict(model_id: str, q: Union[str, None] = None):
    if q is None:
        return { 'error': 'invalid query string' }
    if model_id=='langid':
        top_k = 2
        predictions = fasttext_model.predict(q, k=top_k)
        labels = tolabels(predictions)
        return { 'result': labels }
    else:
        return { 'error': 'invalid model' }