#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        _len = len(sentence)
        first = sentence[0]
        return _len, first
    return 0, None
