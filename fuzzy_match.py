from thefuzz import fuzz
import json
#import spacy

queries = json.load(open("query_mapping.json",'rb'))

questions = [x for x in queries.keys()]

def check_closest_match(inputt):
        inputtt = inputt.strip().lower() #.replace("monthly", "month")
        sims = [fuzz.token_sort_ratio(inputtt, x.strip().lower()) for x in questions]
        print(max(sims))
        if max(sims)>=50:
            maxx = sims.index(max(sims))
            detected = questions[maxx]
            print(detected)
            ans = queries[detected]
            return ans
        else:
            return 'Null'
        

"""nlp = spacy.load("en_core_web_md")
ques = [nlp(x.lower().strip()) for x in questions]

def check_closest_match(inputt):
        inputt = inputt.replace('quarterly', 'quarter').replace('monthly', 'month')
        inputtt = nlp(inputt)
        #inputtt = nlp(' '.join([str(t) for t in inputtt if not t.is_stop]))
        sims = [inputtt.similarity(x) for x in ques]
        print(sims)
        print(max(sims))
        if max(sims)>=0.5:
            maxx = sims.index(max(sims))
            detected = questions[maxx]
            print(detected)
            ans = queries[detected]
            return ans
        else:
            return 'Null'"""