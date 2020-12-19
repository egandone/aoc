from antlr4 import *
from day182exprLexer import day182exprLexer
from day182exprParser import day182exprParser
from day182exprVisitor import day182exprVisitor


class visitor(day182exprVisitor):
    def visitInt(self, ctx):
        return ctx.INT().getText()

    def visitMult(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        return left * right

    def visitAdd(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        return left + right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())


def run_expr(str):
    lexer = day182exprLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    parser = day182exprParser(stream)
    tree = parser.expr()

    v = visitor()
    out = v.visit(tree)
    return out


def main():
    values = []
    with open('input.txt') as input:
        for line in input.readlines():
            line = line.strip()
            value = run_expr(line.strip())
            print(f'{value} <-- {line}')
            values.append(value)
    s = sum(values)
    print(s)


if __name__ == '__main__':
    main()
