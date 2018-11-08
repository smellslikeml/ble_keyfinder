# coding: utf-8
import sys
import pickle
import numpy as np
import pandas as pd
from ast import literal_eval
from collections import Counter
sys.path.append('/home/funk/bluebot/')
from reverse_read import reverse_readline

def loc_predict(mdl_):
    read_dict = {}
    line_gen = reverse_readline('bt_logs.txt')
    res_lst = []
    for idx, ll in enumerate(line_gen):
        if idx < 5:
            res_lst.append(literal_eval(ll))
        else:
            break

    val = pd.DataFrame(res_lst).replace({'0': np.nan})
    try:
        val.pop('location')
    except:
        pass
    val = val.values

    #mdl_ = pickle.load(open('bt_model.dat', 'rb'))
    preds = mdl_.predict(val)
    guess = Counter(preds)
    guess = guess.most_common(1)[0][0]
    out_str = 'Look near the ' + guess
    return out_str

if __name__ == '__main__':
    mdl_ = pickle.load(open('bt_model.dat', 'rb'))
    print(loc_predict(mdl_))
