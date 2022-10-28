

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

def qna(context,question):

    QA_input = {
        'context': context,
        'question': question 
        
    }
    res = nlp(QA_input)

    return res


# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)