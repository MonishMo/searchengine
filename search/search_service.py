import os

import openai
import pandas as pd

from openai.embeddings_utils import cosine_similarity



openai_key = os.environ.get('openai_key')

openai.api_key = openai_key

def load_documents(dir):

    for file in os.listdir(dir):
        if file.endswith(".txt"):
            with open(dir + file, "r") as f:
                text_list = f.read()

    question_answer = text_list.replace("\n\n", "--").split("--")

    df = pd.DataFrame(question_answer, columns=["QnA"])
    df[['question', 'answer']] = df['QnA'].str.split('\n', n=1, expand=True)

    return df


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

def find_similarity(df, question):

    df['qna_embedding'] = df.QnA.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))
    question_embedding = get_embedding(question)
    df["similarity"] = df.qna_embedding.apply(lambda x: cosine_similarity(x, question_embedding))

    return df
