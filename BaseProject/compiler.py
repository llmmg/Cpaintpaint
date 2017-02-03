import AST
from AST import addToClass
from functools import reduce

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

# opcodes de la SVM
#    PUSHC <val>     pushes the constant <val> on the stack
#    PUSHV <id>      pushes the value of identifier <id> on the stack
#    SET <id>        pops a value from the top of stack and sets <id>
#    PRINT           pops a value from the top of stack and print it
#    ADD,SUB,DIV,MUL pops 2 values from the top of stack and compute them
#    USUB            changes the sign of the number on the top of stack
#    JMP <tag>       jump to :<tag>
#    JIZ,JINZ <tag>  pops a value from the top of stack and jump to :<tag> if (not) zero

# chaque opération correspond à son instruction d'exécution de la machine SVM

# operations = {
#     '+': 'ADD',
#     '-': 'SUB',
#     '*': 'MUL',
#     '/': 'DIV'
# }

vars = {}


def whilecounter():
    whilecounter.current += 1
    return whilecounter.current


whilecounter.current = 0


# noeud de programme
# retourne la suite d'opcodes de tous les enfants
@addToClass(AST.ProgramNode)
def compile(self):
    bytecode = ""
    for c in self.children:
        bytecode += c.compile()
    return bytecode


# noeud terminal
# si c'est une variable : empile la valeur de la variable
# si c'est une constante : empile la constante
@addToClass(AST.TokenNode)
def compile(self):
    if isinstance(self.tok, str):
        try:
            return vars[self.tok]
        except KeyError:
            print("*** Error: variable %s undefined!" % self.tok)
    return self.tok


# noeud d'assignation de variable
# exécute le noeud à droite du signe =
# dépile un élément et le met dans ID
@addToClass(AST.AssignNode)
def compile(self):
    vars[self.children[0].tok] = self.children[1].compile()
    return ""


# noeud d'affichage
# exécute le noeud qui suit le PRINT
# dépile un élément et l'affiche
@addToClass(AST.PrintNode)
def compile(self):
    bytecode = ""
    # bytecode += self.children[0].compile()
    # bytecode += "PRINT\n"
    bytecode += "print("
    bytecode += vars(self.children[0].compile())

    return bytecode


# noeud d'opération arithmétique
@addToClass(AST.OpNode)
def compile(self):
    bytecode = ""
    args = [c.compile() for c in self.children]
    if len(args) == 1:
        args.insert(0, 0)
    return reduce(operations[self.op], args)


# noeud de boucle while
# saute au label de la condition défini plus bas
# insère le label puis le corps du body
# insère le label puis le corps de la condition
# réalise un saut conditionnel sur le résultat de la condition (empilé)
@addToClass(AST.WhileNode)
def compile(self):
    bytecode = "\n"

    while (self.children[0].compile() != 0):
        bytecode += str(self.children[1].compile())
    return bytecode


@addToClass(AST.ForNode)
def compile(self):
    bytecode = "\n"

    while (self.children[0].compile()):
        self.children[1].compile()
        bytecode += str(self.children[2].compile())
        # self.children[0] += self.children[2].compile()
    return bytecode


@addToClass(AST.IfNode)
def compile(self):
    bytecode = "\n"
    # if true
    if (self.children[0].compile() != 0):
        bytecode += str(self.children[1].compile())
        bytecode += "\n"

    return bytecode


@addToClass(AST.PrintPixelNode)
def compile(self):
    bytecode = "img["
    bytecode += str(int(self.children[0].compile()))
    bytecode += ","
    bytecode += str(int(self.children[1].compile()))
    bytecode += "]=["
    bytecode += str(int(self.children[2].compile()))
    bytecode += ","
    bytecode += str(int(self.children[3].compile()))
    bytecode += ","
    bytecode += str(int(self.children[4].compile()))
    bytecode += "]"
    bytecode += "\n"
    return bytecode

@addToClass(AST.DrawLineNode)
def compile(self):
    bytecode = ""
    xi = int(self.children[0].compile())
    yi = int(self.children[1].compile())
    xf = int(self.children[2].compile())
    yf = int(self.children[3].compile())
    rc = str(int(self.children[4].compile()))
    gc = str(int(self.children[5].compile()))
    bc = str(int(self.children[6].compile()))
    t = int(self.children[6].compile())
    a = (yf-yi)/(xf-xi)
    b  = yi - a * xi
    for i in range(-t/2, t/2):
        for x in range(xi, xf):
            y = int((a * x + b))
            bytecode += "img["+str(x)+","+str(y+i)+"]=["+rc+","+gc+","+bc+"]\n"

    print(bytecode)
    return bytecode


@addToClass(AST.EqualNode)
def compile(self):
    if (self.children[0].compile() == self.children[1].compile()):
        return 1
    else:
        return 0


@addToClass(AST.NotEqualNode)
def compile(self):
    if (self.children[0].compile() == self.children[1].compile()):
        return 0
    else:
        return 1


@addToClass(AST.LessNode)
def compile(self):
    if (self.children[0].compile() < self.children[1].compile()):
        return 1
    else:
        return 0


@addToClass(AST.MoreNode)
def compile(self):
    if (self.children[0].compile() > self.children[1].compile()):
        return 1
    else:
        return 0


if __name__ == "__main__":
    from parserPaint import parse
    import sys, os

    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    print(ast)
    compiled = ast.compile()

    name = os.path.splitext(sys.argv[1])[0] + '.py'

    outfile = open(name, 'w')
    outfile.write("import numpy as np\n")
    outfile.write("import cv2\n")
    outfile.write("img = np.zeros((400,300,3), np.uint8)\n")

    outfile.write(compiled)

    outfile.write("\n\ncv2.imshow('image',img)\n")
    outfile.write("cv2.waitKey(0)\n")
    outfile.write("cv2.destroyAllWindows()\n")
    outfile.close()

    print("Wrote output to", name)

    graph = ast.makegraphicaltree()
    graph.write_pdf(os.path.splitext(sys.argv[1])[0] + '.pdf')

    print("Wrote pdf tree to", name)
