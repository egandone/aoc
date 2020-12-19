grammar day182expr;

expr: expr '+' expr  # Add
    | expr '*' expr  # Mult
    | '(' expr ')'            # Parens
    | INT                     # int
    ;

INT: [0-9]+;
WS  :   [ \t]+ -> skip ;