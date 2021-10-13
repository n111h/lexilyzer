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
    "else":12,      ')':28,         "do":29,                    #   NOTE:  added "do":29 (not in documentation)
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

def lexilyzerOnePass(programString = '', filepath = "test.pl0"):##  this lexilyzer will iterate over the program string by char
    if(not programString):
        programString = fileOpener(filepath)

    tokenString = []

    token = ''
    endOfToken = False
    for char in programString:
        if(endOfToken): 
            tokenString.append(token)
            token = ''
    pass                                                        #   work in progress...

def lexilyzerTwoPass(programString = '', filepath = "test.pl0"):##  this lexilyzer uses a string cleaning preprocess step
    if(not programString):                                      #   if there is no passed program string, a file will be opened
        programString = fileOpener(filepath)

    programString = stringCleaner(programString)                #   adds whitespace to program string for python3 split()

    programTokens = programString.split()                       #   splits program string into tokens using arbitary whitespace
    tokenString = []

    for token in programTokens:                                 #   iterate through tokens
        if(token in tokens):                                    #   if the token is in the token table
            tokenString.append(str(tokens[token]))              #   add the string value of the looked up token to token string
        elif(token[0].isalpha()):                               #   else if the token starts with an alpha char
            tokenString.append("0 "+str(h(token)))              #   it is a symbol - hash the token and add it to token string
            symbolTable[h(token)].append(token)                                                                ##  DEBUGGING  ##
        else:                                                   #   else the token is a number
            tokenString.append("1 "+str(token))                 #   add the number as a prefixed string to token string
    
    return(programTokens,tokenString)                           #   returns: tokens, transcribed (translated) tokens

lexilyzer = lexilyzerTwoPass                                    #   sets lexilyzer() to the two pass version

####  MAIN  ####################################################################################################################

def main():
    tokenList,tokenStr = lexilyzer()                            #   test with default file

    for e,t in enumerate(tokenList): print(f"{e:<8}{t:<32}")    #   prints each of the tokens                  ##  DEBUGGING  ##
    print()                                                                                                    ##  DEBUGGING  ##
    for e,s in enumerate(symbolTable):                          #   prints symbol table (check for collisions) ##  DEBUGGING  ##
        if(s): print(f"{e:<8}{','.join(s):<32}")                                                               ##  DEBUGGING  ##
    print('\n'," * ".join(tokenStr))                            #   final lexilyzer output                     ##  DEBUGGING  ##

if(__name__=="__main__"): main()