import AST
from AST import addToClass

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
operations = {
    '+': 'ADD',
    '-': 'SUB',
    '*': 'MUL',
    '/': 'DIV'
}

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
    bytecode = ""
    if isinstance(self.tok, str):
        bytecode += "%s" % self.tok
    else:
        bytecode += "%s" % self.tok
    return bytecode


# noeud d'assignation de variable
# exécute le noeud à droite du signe =
# dépile un élément et le met dans ID
@addToClass(AST.AssignNode)
def compile(self):
    bytecode = ""
    # bytecode += self.children[1].compile()
    # bytecode += "SET %s\n" % self.children[0].tok
    name = self.children[0].tok
    val = self.children[1].compile()
    vars[name] = val
    # bytecode += name + "="
    # bytecode += val

    return bytecode


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
# si c'est une opération unaire (nombre négatif), empile le nombre et l'inverse
# si c'est une opération binaire, empile les enfants puis l'opération
@addToClass(AST.OpNode)
def compile(self):
    bytecode = ""
    if len(self.children) == 1:
        # bytecode += self.children[0].compile()
        bytecode += "USUB\n"
    else:
        stack = []
        for c in self.children:
            # bytecode += c.compile()
            stack.append(c.compile())
        # bytecode += operations[self.op] + "\n"
        if self.op == '-':
            vars[stack[0]] = float(vars[stack[0]]) - float(stack[1])
        elif self.op == '+':
            vars[stack[0]] = float(vars[stack[0]]) + float(stack[1])

    return bytecode


# noeud de boucle while
# saute au label de la condition défini plus bas
# insère le label puis le corps du body
# insère le label puis le corps de la condition
# réalise un saut conditionnel sur le résultat de la condition (empilé)
@addToClass(AST.WhileNode)
def compile(self):
    # counter = whilecounter()
    bytecode = ""
    # bytecode += "JMP cond%s\n" % counter
    # bytecode += "body%s: " % counter
    # bytecode += self.children[1].compile()
    # bytecode += "cond%s: " % counter
    # bytecode += self.children[0].compile()
    # bytecode += "JINZ body%s\n" % counter

    ##TEST
    # body
    # bytecode += "\n---body---: \n"
    bytecode += self.children[1].compile()
    # bytecode += "\n ---while param--- \n"
    # while param
    bytecode += self.children[0].compile()
    bytecode+="="
    bytecode+= vars[self.children[0].compile()]
    # bytecode += "\nEND\n"

    return bytecode


@addToClass(AST.PrintPixelNode)
def compile(self):
    bytecode = "img["
    bytecode += self.children[0].compile()
    bytecode += ","
    bytecode += self.children[1].compile()
    bytecode += "]=["
    bytecode += self.children[2].compile()
    bytecode += ","
    bytecode += self.children[3].compile()
    bytecode += ","
    bytecode += self.children[4].compile()
    bytecode += "]"
    return bytecode


if __name__ == "__main__":
    from parserPaint import parse
    import sys, os

    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    print(ast)
    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0] + '.vm'
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()

    print("Wrote output to", name)

    graph = ast.makegraphicaltree()
    graph.write_pdf(os.path.splitext(sys.argv[1])[0] + '.pdf')

    print("Wrote pdf tree to", name)