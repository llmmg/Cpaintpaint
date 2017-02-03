import ply.yacc as yacc
from lex5 import tokens
import AST

vars = {}


def p_programme_statement(p):
    ''' programme : statement '''
    p[0] = AST.ProgramNode(p[1])


def p_programme_recursive(p):
    ''' programme : statement ';' programme '''
    p[0] = AST.ProgramNode([p[1]] + p[3].children)


def p_statement(p):
    ''' statement : assignation
        | structure '''
    p[0] = p[1]


def p_statement_print(p):
    ''' statement : PRINT expression '''
    p[0] = AST.PrintNode(p[2])


def p_structure_for(p):
    # ''' structure : FOR expression ',' expression ',' expression '{' programme '}' '''
    # p[0] = AST.ForNode([p[2], p[4], p[6], p[8]])
    ''' structure : FOR '(' expression ',' assignation ')' '{' programme '}' '''
    p[0] = AST.ForNode([p[3], p[5], p[8]])


def p_structure(p):
    ''' structure : WHILE expression '{' programme '}' '''
    p[0] = AST.WhileNode([p[2], p[4]])


def p_structure_if(p):
    ''' structure : IF expression '{' programme '}' '''
    p[0] = AST.IfNode([p[2], p[4]])


def p_printPixel(p):
    ''' statement : PRINTPIXEL '(' expression ',' expression ',' expression ',' expression ',' expression ')' '''
    p[0] = AST.PrintPixelNode([p[3], p[5], p[7], p[9], p[11]])

# Line : x1, y1, x2, y2, R, G, B, thickness
def p_drawLine(p):
    ''' statement : DRAWLINE '(' expression ',' expression ',' expression ',' expression ',' expression ',' expression ',' expression ',' expression ')' '''
    p[0] = AST.DrawLineNode([p[3], p[5], p[7], p[9], p[11], p[13], p[15], p[17]])

# Rectangle : x1, y1, x2, y2, R, G, B
def p_drawRectangle(p):
    ''' statement : DRAWRECTANGLE '(' expression ',' expression ',' expression ',' expression ',' expression ',' expression ',' expression ',' expression ')' '''
    p[0] = AST.DrawRectangleNode([p[3], p[5], p[7], p[9], p[11], p[13], p[15]])

def p_expression_op(p):
    '''expression : expression ADD_OP expression
            | expression MUL_OP expression'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])


def p_expression_equal(p):
    ''' expression : expression EQUAL expression '''
    p[0] = AST.EqualNode([p[1], p[3]])


def p_expression_notequal(p):
    ''' expression : expression NOTEQUAL expression '''
    p[0] = AST.NotEqualNode([p[1], p[3]])


def p_expression_less(p):
    ''' expression : expression '<' expression '''
    p[0] = AST.LessNode([p[1], p[3]])


def p_expression_more(p):
    ''' expression : expression '>' expression '''
    p[0] = AST.MoreNode([p[1], p[3]])


def p_expression_num_or_var(p):
    '''expression : NUMBER
        | IDENTIFIER '''
    p[0] = AST.TokenNode(p[1])


def p_expression_paren(p):
    '''expression : '(' expression ')' '''
    p[0] = p[2]


def p_minus(p):
    ''' expression : ADD_OP expression %prec UMINUS'''
    p[0] = AST.OpNode(p[1], [p[2]])


def p_assign(p):
    ''' assignation : IDENTIFIER '=' expression '''
    p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])


def p_error(p):
    if p:
        print("Syntax error in line %d" % p.lineno)
        yacc.errok()
    else:
        print("Syntax error: unexpected end of file!")


precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('right', 'UMINUS'),
    ('right', 'EQUAL'),
    ('right', 'NOTEQUAL'),
    ('right', '<'),
    ('right', '>'),
)


def parse(program):
    return yacc.parse(program)


yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys

    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)
    if result:
        print(result)

        import os

        graph = result.makegraphicaltree()
        name = os.path.splitext(sys.argv[1])[0] + '-ast.pdf'
        graph.write_pdf(name)
        print("wrote ast to", name)
    else:
        print("Parsing returned no result!")
