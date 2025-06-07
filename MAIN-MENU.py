import re

def trim(list):
    for l in list:
        l += " "

    return l

with open("obama.tasr", "r", encoding="UTF-8") as n:
    f = n.read().strip().split()

def plus():
    return "PLUS"

def minus():
    return "MINUS"

def division():
    return "DIVISION"

def multi():
    return "MULTIPLICATION"

def equal():
    return "ASSIGNMENT"

def int_token():
    return "DIGIT"

def double():
    return "FLOATIONG-POINT"

def stringd():
    return "STRING"

def bool_token():
    return "BOOL"

def printf():
    return "OUTPUT"

def scanf():
    return "INPUT"

comma = ["printf", "renderf", "obama", "system", "scanf"]
ID = r'[a-zA-Z]'
operators = ["(", ")", "+", "-", "/", "*", "=", "!=", "==", ">", "<"]  #Taskall Render Edition v0.1 operators
logical = ["and", "&&", "or", "||", "xor", "^^", "not", "!"]
values = [r"\d+", "true", "false", "yes", "no", r"[a-zA-z]"]
types = ["int", "str", "bool", "long", "double", "sinister", "digit", "string", "boolean", "digit", "float"]
tan_operators = ["for", "do_while", "do_while_not", "if", "elif", "else", "rend", "then"]
char = [":", ";", "[", "]"]

token_operators = {
    "+": plus,
    "-": minus,
    "=": equal,
    "/": division,
    "*": multi,
    "int": int_token,
    "digit": int_token,
    "double": double,
    "float": double,
    "string": stringd,
    "bool": bool_token,
    "boolean": bool_token,
    "printf": printf,
    "scanf": scanf,

}



token = []
def lexer(char):
    for code in char:
        token.append((code, "undefined"))

    return token

def tokenization():

    for char, state in lexer(f):
        if char in comma:
            if char == "printf":
                state = token_operators.get(char)()
            elif char == "scanf":
                state = token_operators.get(char)()

        elif char in types:
            if char == "int" or char == "digit":
                state = token_operators.get(char)()
            elif char == "double" or char == "float":
                state = token_operators.get(char)()
            elif char == "string":
                state = token_operators.get(char)()
            elif char == "bool" or char == "boolean":
                state = token_operators.get(char)()

        elif char in operators:
            if char == "+":
                state = token_operators.get(char)()
            elif char == "-":
                state = token_operators.get(char)()
            elif char == "/":
                state = token_operators.get(char)()
            elif char == "=":
                state = token_operators.get(char)()
            elif char == "*":
                state = token_operators.get(char)()


        print(f"('{char}') : ({state})")




tokenization()
