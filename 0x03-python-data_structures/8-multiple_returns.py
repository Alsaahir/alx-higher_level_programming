#!/usr/bin/python3


def multiple_returns(sentence):
    sentence_tuple = ()
    if sentence is None:
        sentence_tuple.append(len(sentence))
        sentence_tuple.append(None)
    else:
        sentence_tuple.append(len(sentence))
        sentence_tuple.append(sentence[0])
    return (sentence_tuple)
