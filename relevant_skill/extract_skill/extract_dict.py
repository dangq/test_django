import pickle
import operator
from difflib import SequenceMatcher
file_result='data/result_1606.txt'
def extract_dict(key,num):

    with open(file_result,'r') as f:
        file=pickle.loads(f.read())
        #print file.keys()

        true_key=key_matching(file.keys(),key)
        dict_file=file[true_key]

        dict_file=sorted(dict_file.items(), key=operator.itemgetter(1),reverse=True)
        #print dict_file
        #return dict_file[0:num]
        if len(dict_file)<=num:
            return dict_file
        else:
            return dict_file[0:num]
def key_matching(key_dict,key_input):
    true_key=None
    # a=[]
    for key in key_dict:
        # a.append(similar(key,key_input))
        if similar(key,key_input)>0.8:

            true_key=key
            break
     #print max(a)
    return true_key
def similar(a,b):
    return SequenceMatcher(None,a,b).ratio()
#extract_dict(file_result,'Dependent ML',6)

