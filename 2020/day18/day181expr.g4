grammar day181expr;

expr: expr op=('+') expr  # BinaryOp
    | expr op=('*') expr  # BinaryOp
    | '(' expr ')'            # Parens
    | INT                     # int
    ;

MUL: '*';
ADD: '+';
INT: [0-9]+;
WS  :   [ \t]+ -> skip ;