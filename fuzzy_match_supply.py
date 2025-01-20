from thefuzz import fuzz
# import spacy

questions = ['What was the total cost to serve the German market in 2023',
             'How has the cost to serve evolved from 2022?',
             'What are the drivers of increase in transport costs?',
             'How can the average pallets per trip be controlled / improved',
             'Explore reduction of SLA of top 40 customers and generate scenarios to identify cost savings.',
             'Explore reduction of SLA of top 20 customers and generate scenarios to identify cost savings.',
             'Specify cost savings for Customer ID Dir_239',
             'Specify cost savings for Customer ID Dir_121']


#nlp = spacy.load("en_core_web_md")
#ques = [nlp(x) for x in questions]

def check_closest_match(inputt):
        sims = [fuzz.partial_ratio(inputt.lower().strip(), x) for x in questions]
        print(sims)
        print(max(sims))
        if max(sims)>=50:
            maxx = sims.index(max(sims))
            return questions[maxx]
        else:
            return 'Null'
