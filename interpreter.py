# Errors

class Error:
    def __init__(self, pos_start, pos_end, error_name, description):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.description = description
    
    def __repr__(self):
        return f"{self.error_name}: {self.description} in {self.pos_start.filename}, on line {self.pos_start.line + 1}:{self.pos_start.column+1}"

class IllegalCharacter(Error):
    def __init__(self, pos_start, pos_end, description):
        super().__init__(pos_start, pos_end,"Illegal character", description)

# Position

class Position:
    def __init__(self, index, line, column, filename, text):
        self.filename = filename
        self.text = text
        self.index = index
        self.line = line
        self.column = column
    
    def advance(self, char):
        self.index += 1
        self.column += 1

        if char == "\n":
            self.line += 1
            self.column = 0
        
        return self
    
    def copy(self):
        return Position(self.index, self.line, self.column)

    



# Tokens

INT_TOKEN = "INT"
FLOAT_TOKEN ="FLOAT"
PLUS_TOKEN = "PLUS"
MINUS_TOKEN = "MINUS"
MUL_TOKEN = "MULTIPLY"
DIV_TOKEN = "DIVIDE"
L_PAR_TOKEN = "L_PAR"
R_PAR_TOKEN = "R_PAR"


class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value:
            return f"{self.type} {self.value}"
        return str(self.type)


# Position



# Lexer

class Lexer:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.position = Position(-1, 0,-1, filename, text)


    def generate_tokens(self):
        tokens = []
        current_number = ""
        
        for i in range(len(self.text)):
            char = self.text[i]
            self.position.advance(char)
            
            if char in "0123456789":
                current_number += char
                continue
            elif char == "." and "." not in current_number and current_number:
                current_number += char
                continue


            if current_number:
                if "." in current_number:
                    tokens.append(Token(FLOAT_TOKEN, float(current_number)))
                else:
                    tokens.append(Token(INT_TOKEN, int(current_number)))
                current_number = ""


            if char in (" \t"):
                continue
            elif char == "+":
                tokens.append(Token(PLUS_TOKEN))
            elif char == "-":
                tokens.append(Token(MINUS_TOKEN))
            elif char == "*":
                tokens.append(Token(MUL_TOKEN))
            elif char == "/":
                tokens.append(Token(DIV_TOKEN))
            elif char == "(":
                tokens.append(Token(L_PAR_TOKEN))
            elif char == ")":
                tokens.append(Token(R_PAR_TOKEN))
            else:
                return [], IllegalCharacter(self.position, self.position, f'"{char}"')

        if current_number:
            if "." in current_number:
                tokens.append(Token(FLOAT_TOKEN, float(current_number)))
            else:
                tokens.append(Token(INT_TOKEN, int(current_number)))

        return tokens, None

def execute(filename, text):
    lexer = Lexer(filename, text)

    return lexer.generate_tokens()

        
            
            
