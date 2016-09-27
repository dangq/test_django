
import requests
import re
from decimal import *
import string
import bisect
import pickle
from nltk.corpus import stopwords
cachedStopWords = stopwords.words("english")
class Weight_factor():
    def __int__(self):
        self.skill_list=[]

    def print_file(self,skill_list):
        with open(self.skill_list) as sl:
            for skill in sl:
                print (skill)

    def cal_weight(self,skill_x_in_y_times,skill_y_in_x_times):
        return skill_x_in_y_times/skill_y_in_x_times, skill_y_in_x_times/skill_x_in_y_times

    def review_to_words(raw_review):
        # Function to convert a raw review to a string of words
        # The input is a single string (a raw movie review), and
        # the output is a single string (a preprocessed movie review)
        #
        # 1. Remove HTML
        review_text = BeautifulSoup(raw_review).get_text()
        #
        # 2. Remove non-letters
        letters_only = re.sub("[^a-zA-Z]", " ", review_text)
        #
        # 3. Convert to lower case, split into individual words
        words = letters_only.lower().split()
        #
        # 4. In Python, searching a set is much faster than searching
        #   a list, so convert the stop words to a set
        stops = set(stopwords.words("english"))
        #
        # 5. Remove stop words
        meaningful_words = [w for w in words if not w in stops]
        #
        # 6. Join the words back into one string separated by space,
        # and return the result.
        return (" ".join(meaningful_words))

    def search_wiki_pedia(self,key_word,max_hit):
        key_word=key_word.replace(" ","_")
        # print key_word

        key='http://lookup.dbpedia.org/api/search/PrefixSearch?QueryClass=&MaxHits='+str(max_hit)+'&QueryString='+key_word
        response = requests.get(key)
        output  = re.compile('<description>(.*?)</description>', re.DOTALL |  re.IGNORECASE).findall(response.text)
        text=[]



        for doc in output:
            #doc=doc.encode('ascii','ignore')
            text_1 = ' '.join([word for word in doc.split() if word not in cachedStopWords])
            text.append(text_1)
        #First parameter is the replacement, second parameter is your input string

        return text

    def count_number(self,key,text):
        count=0
        key=key.lower()

        key_set=key.split()
        #text_set=text.lower().split()
        #text_set=set(text)
        # Seprate two keys: for example: [1,2,3] --> ([1,2],[2,3])
        B = zip(key_set, key_set[1:])
        #C = zip(text_set,text_set[1:])
        if len(key_set)>3:
            count=0
            return count
        for i in range(0,len(text)):
        #
            #a=set(text[i].lower().split())
            a = set(text[i].lower().split())
            #b=text[i].lower().split()
            b = text[i].lower().split()
            C = zip(b, b[1:])
            if len(key_set)==1:
                if key_set[0] in a:
                    count=count+1
            elif len(B)==2 and len(C)>2:
                if B[0] in C or B[1] in C:
                    count=count+1
            elif len(B)==3 and len(C)>3:
                if B[0] in C or B[1] in C or B[2] in C:
                    count += 1
            elif len(B)==4 and len(C)>4:
                if B[0] in C or B[1] in C or B[2] in C or B[3] in C:
                    count+=1
            else:
                for ii in B:
                    if ii in C:
                        count += 1

        #     b=key.split()

        #     #len_doc=len_doc+len(a)
        #     if key in a:
        #         count=count+1
        return count
    def quantize(num, quant):
        mids = [(quant[i] + quant[i + 1]) / 2.0
            for i in xrange(len(quant) - 1)]
        ind = bisect.bisect_right(mids, num)
        return quant[ind]
    def write_dict_file(self,file_name,file):
        with open(file_name,'wb') as f:
            pickle.dump(file,f)
    def read_dict_file(self,file_name):
        with open(file_name,'r') as g:
            file=pickle.loads(g.read())
        return file

