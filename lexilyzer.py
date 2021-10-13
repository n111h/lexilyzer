#!/usr/bin/python3
#
#  Noah Olmstead Harvey
#  04102021
#
#  lexical analyzer for pl0

####  IMPORTS  #################################################################################################################

from os import read
from hasher import hasher as h

####  GLOBALS  #################################################################################################################

tokens = {                                                      #  token table from specification document
    "program":2,    "while":18,     "EOF":35,
    "begin":3,      "loop":19,      "var":36,
    "end":4,        "end_loop":20,  "const":37,
    ';':5,          "input":21,     "call":38,
    "declare":6,    "output":22,    "procedure":39,
    ',':7,          '+':23,         "<>":40,
    ":=":8,         '-':24,         '<':41,
    '.':9,          '*':25,         '>':42,
    "if":10,        '/':26,         ">=":43,
    "then":11,      '(':27,         "<=":44,
    "else":12,      ')':28,         "do":29,
    "end_if":13,    "Real":30,
    "odd":14,       "Integer":31,
    ':':15,         "Boolean":32,
    '{':16,         '=':33,
    '}':17,         "EOL":34
}

symbolTable = [[] for i in range(499)]                          #  499 closest prime <= 500

####  FUNCTIONS  ###############################################################################################################

def fileOpener(filepath = "test.pl0"):                          ##  opens passed filename/filepath and returns it as a string
    with open(filepath, 'r') as f:
        programString = f.read()
    return(programString)

def stringCleaner(programString=''):                            ##  used in two pass lexilyzer to preprocess program string
    print(programString)                                                                                       ##  DEBUGGING  ##
    programString += " EOF"                                     #   EOF (end of file) added to end of program string
    programString = programString.replace(';'," ; ")            #   whitespace added around token for python3 split()
    programString = programString.replace(','," , ")            #   ''
    programString = programString.replace(":="," := ")          #   ''
    programString = programString.replace('.'," . ")            #   ''
    programString = programString.replace('{'," { ")            #   ''
    programString = programString.replace('}'," } ")            #   ''
    programString = programString.replace('+'," + ")            #   ''
    programString = programString.replace('-'," - ")            #   ''
    programString = programString.replace('*'," * ")            #   ''
    programString = programString.replace('/'," / ")            #   ''
    programString = programString.replace('('," ( ")            #   ''
    programString = programString.replace(')'," ) ")            #   ''
    programString = programString.replace("<>"," <> ")          #   ''
    programString = programString.replace(">="," >= ")          #   ''
    programString = programString.replace("<="," <= ")          #   ''
    programString = programString.replace('\n'," EOL ")         #   newline chars replaced by EOL (end of line)
    print(programString)                                                                                       ##  DEBUGGING  ##
    return(programString)

def lexilyzerOnePass(programString = '', filepath = "test.5.14.pl0"):
    if(not programString):
        programString = fileOpener(filepath)

    tokenString = []

    token = ''
    endOfToken = False
    for char in programString:
        if(endOfToken): 
            tokenString.append(token)
            token = ''


    pass

def lexilyzerTwoPass(programString = '', filepath = "test.5.14.pl0"):
    if(not programString):
        programString = fileOpener(filepath)

    programString = stringCleaner(programString)

    programTokens = programString.split()
    tokenString = []

    for token in programTokens:
        if(token in tokens):
            tokenString.append(str(tokens[token]))
        elif(token[0].isalpha()):
            tokenString.append("0 "+str(h(token)))
            symbolTable[h(token)].append(token)                                                                ##  DEBUGGING  ##
        else:
            tokenString.append("1 "+str(token))
    
    return(programTokens,tokenString)

lexilyzer = lexilyzerTwoPass

####  MAIN  ####################################################################################################################

def main():
    tokenList,tokenStr = lexilyzer()

    for e,t in enumerate(tokenList): print(f"{e:<8}{t:<32}")
    print()
    for e,s in enumerate(symbolTable):
        if(s): print(f"{e:<8}{','.join(s):<32}")
    print('\n'," * ".join(tokenStr))

if(__name__=="__main__"): main()