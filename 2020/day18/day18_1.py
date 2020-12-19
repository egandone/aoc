from antlr4 import *
from day181exprLexer import day181exprLexer
from day181exprParser import day181exprParser
from day181exprVisitor import day181exprVisitor


class visitor(day181exprVisitor):
    def visitInt(self, ctx):
        return ctx.INT().getText()

    def visitBinaryOp(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == day181exprParser.MUL:
            return left * right
        else:
            return left + right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())


def run_expr(str):
    lexer = day181exprLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    parser = day181exprParser(stream)
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
