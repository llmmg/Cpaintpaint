import AST
from AST import addToClass
from functools import reduce

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '%': lambda x, y: x % y,
}

vars = {}

# noeud de programme
# Retourne les instructions des enfants
@addToClass(AST.ProgramNode)
def compile(self):
    bytecode = ""
    for c in self.children:
        bytecode += c.compile()
    return bytecode


# noeud terminal
@addToClass(AST.TokenNode)
def compile(self):
    if isinstance(self.tok, str):
        try:
            return vars[self.tok]
        except KeyError:
            print("*** Error: variable %s undefined!" % self.tok)
    return self.tok


# noeud d'assignation de variable
# Met la valeur dans le dictionnaire des variables
@addToClass(AST.AssignNode)
def compile(self):
    vars[self.children[0].tok] = self.children[1].compile()
    return ""


# noeud d'opération arithmétique
@addToClass(AST.OpNode)
def compile(self):
    bytecode = ""
    args = [c.compile() for c in self.children]
    if len(args) == 1:
        args.insert(0, 0)
    return reduce(operations[self.op], args)


# noeud de boucle while
@addToClass(AST.WhileNode)
def compile(self):
    bytecode = ""
    # Tant que la condition de la boucle while est vraie, on execute le programme
    while (self.children[0].compile() != 0):
        bytecode += str(self.children[1].compile())
    return bytecode


# noeud de boucle for
@addToClass(AST.ForNode)
def compile(self):
    bytecode = ""
    self.children[0].compile()
    # Tant que le deuxième paramètre du For est vraie, on continue le programme
    while (self.children[1].compile()):
        bytecode += str(self.children[3].compile())
        self.children[2].compile()

    return bytecode


# condition
@addToClass(AST.IfNode)
def compile(self):
    bytecode = ""
    # if true
    if (self.children[0].compile() != 0):
        bytecode += str(self.children[1].compile())

    return bytecode


# Noeud de la fonction printPixel
@addToClass(AST.PrintPixelNode)
def compile(self):
    global sizeX
    global sizeY

    sizeX = max(sizeX, int(self.children[1].compile()))
    sizeY = max(sizeY, int(self.children[0].compile()))
    # In opencv x and y are inversed ??
    bytecode = "img["
    bytecode += str(int(self.children[1].compile()))
    bytecode += ","
    bytecode += str(int(self.children[0].compile()))
    bytecode += "]=["
    bytecode += str(int(self.children[2].compile()))
    bytecode += ","
    bytecode += str(int(self.children[3].compile()))
    bytecode += ","
    bytecode += str(int(self.children[4].compile()))
    bytecode += "]"
    bytecode += "\n"
    return bytecode


# Noeud drawLine
@addToClass(AST.DrawLineNode)
def compile(self):

    global sizeX
    global sizeY

    bytecode = ""
    xi = int(self.children[1].compile())
    yi = int(self.children[0].compile())
    xf = int(self.children[3].compile())
    yf = int(self.children[2].compile())
    rc = str(int(self.children[4].compile()))
    gc = str(int(self.children[5].compile()))
    bc = str(int(self.children[6].compile()))
    t = int(self.children[7].compile())

    # La ligne est dessiné avec l'equation cartésienne

    # si la ligne n'est pas verticale
    if ((xf - xi) != 0):
        a = (yf - yi) / (xf - xi)
        b = yi - a * xi
        for i in range(int(-t / 2), int(t / 2)):
            for x in range(xi, xf, 1 if ((xf - xi) > 1) else -1):
                y = int((a * x + b))
                sizeX = max(sizeX, y+i)
                sizeY = max(sizeY, x)
                bytecode += "img[" + str(x) + "," + str(y + i) + "]=[" + rc + "," + gc + "," + bc + "]\n"

    # si la ligne n'est pas horizontale
    if ((yf - yi) != 0):
        a = (xf - xi) / (yf - yi)
        b = xi - a * yi
        for i in range(int(-t / 2), int(t / 2)):
            for y in range(yi, yf, 1 if ((yf - yi) > 1) else -1):
                x = int((a * y + b))
                sizeX = max(sizeX, y)
                sizeY = max(sizeY, x+i)
                bytecode += "img[" + str(x + i) + "," + str(y) + "]=[" + rc + "," + gc + "," + bc + "]\n"

    return bytecode


@addToClass(AST.DrawRectangleNode)
def compile(self):
    global sizeX
    global sizeY

    bytecode = ""
    xi = int(self.children[1].compile())
    yi = int(self.children[0].compile())
    xf = int(self.children[3].compile())
    yf = int(self.children[2].compile())
    rc = str(int(self.children[4].compile()))
    gc = str(int(self.children[5].compile()))
    bc = str(int(self.children[6].compile()))

    sizeX = max(sizeX, xi)
    sizeX = max(sizeX, xf)
    sizeY = max(sizeY, yi)
    sizeY = max(sizeY, yf)

    # Entre la position A et B, dessine des pixels
    for i in range(xi, xf, 1 if ((xf - xi) > 1) else -1):
        for j in range(yi, yf, 1 if ((yf - yi) > 1) else -1):
            bytecode += "img[" + str(i) + "," + str(j) + "]=[" + rc + "," + gc + "," + bc + "]\n"

    return bytecode


# Noeud drawCircle
@addToClass(AST.DrawCircleNode)
def compile(self):

    global sizeX
    global sizeY

    bytecode = ""
    # positions et rayon
    x = int(self.children[1].compile())
    y = int(self.children[0].compile())
    r = int(self.children[2].compile())

    # couleurs
    rc = str(int(self.children[3].compile()))
    gc = str(int(self.children[4].compile()))
    bc = str(int(self.children[5].compile()))

    # On regarde dans le rectangle englobant si le pixel est < ou = au rayon du cercle.
    # Si il est dans le cercle alors on dessine le pixel sinon on saute l'instruction
    for i in range(x - r, x + r):
        for j in range(y - r, y + r):
            if ((i - x) ** 2 + (j - y) ** 2) <= r ** 2:
                sizeX = max(sizeX, j)
                sizeY = max(sizeY, i)
                bytecode += "img[" + str(i) + "," + str(j) + "]=[" + rc + "," + gc + "," + bc + "]\n"

    return bytecode


# Egalité
@addToClass(AST.EqualNode)
def compile(self):
    if (self.children[0].compile() == self.children[1].compile()):
        return 1
    else:
        return 0


# Inégalité
@addToClass(AST.NotEqualNode)
def compile(self):
    if (self.children[0].compile() == self.children[1].compile()):
        return 0
    else:
        return 1


# <
@addToClass(AST.LessNode)
def compile(self):
    if (self.children[0].compile() < self.children[1].compile()):
        return 1
    else:
        return 0


# >
@addToClass(AST.MoreNode)
def compile(self):
    if (self.children[0].compile() > self.children[1].compile()):
        return 1
    else:
        return 0


# <=
@addToClass(AST.LessOrEqualNode)
def compile(self):
    if (self.children[0].compile() <= self.children[1].compile()):
        return 1
    else:
        return 0


# >=
@addToClass(AST.MoreOrEqualNode)
def compile(self):
    if (self.children[0].compile() >= self.children[1].compile()):
        return 1
    else:
        return 0

if __name__ == "__main__":
    from parserPaint import parse
    import sys, os

    sizeX = 0
    sizeY = 0

    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    print(ast)
    compiled = ast.compile()

    name = os.path.splitext(sys.argv[1])[0] + '.py'

    outfile = open(name, 'w')
    outfile.write("import numpy as np\n")
    outfile.write("import cv2\n")
    outfile.write("img = np.zeros(("+str(sizeX+1)+","+str(sizeY+1)+",3), np.uint8)\n")

    outfile.write(compiled)

    outfile.write("\n\ncv2.imshow('image',img)\n")
    outfile.write("cv2.waitKey(0)\n")
    outfile.write("cv2.destroyAllWindows()\n")
    outfile.write("cv2.imwrite(__file__.split('.')[0]+'.png', img)")
    outfile.close()

    print("Wrote output to", name)

    # graph = ast.makegraphicaltree()
    # graph.write_pdf(os.path.splitext(sys.argv[1])[0] + '.pdf')
    #
    # print("Wrote pdf tree to", name)
