import spacy
from spacy.tokenizer import Tokenizer

def get_lemmas(text):

    nlp = spacy.load("en_core_web_sm-2.2.5", path="./")

    tokenizer = Tokenizer(nlp.vocab)

    STOP_WORDS = nlp.Defaults.stop_words.union(['  ', 'und', '-', 'die', 'der', 'berlin', 'ein', 'das', 'mit', 'ist', 'im', 'zu', 'eine', 'es', 'für'
                                            'berlin.', 'zum', 'sind', 'für', 'Berlin.', '-pron-', 's', 'u', '', "'", ' ', '-PRON-'])

    lemmas = []

    doc = nlp(text)

    # Something goes here :P
    for token in doc:
        #if ((token.is_stop == False) and (token.is_punct == False)) and (token.pos_!= 'PRON'):
        lemmas.append(token.lemma_)

    lemma_summary = []

    #for set_of_lemmas in lemmas.values:
    working_set = ""
    for lemma in lemmas:
        working_set += lemma + ' '
    lemma_summary.append(working_set)


    description = [lemma_summary[0]]

    tokens = []

    for doc in tokenizer.pipe(description, batch_size=500):

        doc_tokens = []

        for token in doc:
            if ((token.is_stop == False) and (token.is_punct == False)) and (token.pos_!= 'PRON'):
                if token.text.lower() not in STOP_WORDS:
                    doc_tokens.append(token.text.lower())

        tokens.append(doc_tokens)

    token_summary = []

    for set_of_tokens in tokens:
        working_set = ""
        for variable in set_of_tokens:
            working_set += variable + ' '
        token_summary.append(working_set)

    return token_summary[0]
