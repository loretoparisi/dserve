'''
    dserve
    https://github.com/loretoparisi/dserve
    @2023 loretoparisi@gmail.com
'''

import os
from time import time
import fasttext

root_path = os.path.dirname(os.path.realpath(__file__))

def load_fasttext():
    '''
        load fasttext model
    '''
    start = time()
    model = fasttext.load_model(os.path.join(root_path,"models","fasttext","lid.176.ftz"))
    print(f"loading model: FastText took: %.2f seconds." % (time() - start))
    return model

