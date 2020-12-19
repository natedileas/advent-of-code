# day18

INPUT = open('input18.txt').read()
TEST1  = """
2 + 3 * 4 
1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
1 + (2 * 3) + 4 * (5 + 6)
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
"""

import ply.lex as lex
import ply.yacc as yacc

class Parser:
    tokens = (
        'NUMBER',
        'PLUS',
        'TIMES',
        'LPAREN',
        'RPAREN',
    )

    # Regular expression rules for simple tokens
    t_PLUS    = r'\+'
    t_TIMES   = r'\*'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'


    # A regular expression rule with some action code
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)    
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def p_expression_plus(self, p):
        'expression : expression PLUS expression'
        p[0] = p[1] + p[3]

    def p_expression_term(self, p):
        ''' expression : term
                       | factor
        '''
        p[0] = p[1]

    def p_term_times(self, p):
        'expression : expression TIMES expression'
        p[0] = p[1] * p[3]

    def p_term_factor(self, p):
        'term : factor'
        p[0] = p[1]

    def p_factor_num(self, p):
        'factor : NUMBER'
        p[0] = p[1]

    def p_factor_expr(self, p):
        'factor : LPAREN expression RPAREN'
        p[0] = p[2]

    # Error rule for syntax errors
    def p_error(self, p):
        print("Syntax error in input!")

    # precedence = (
    #     # ('left', 'NUMBER'),
    #     # ('left', 'RPAREN', 'LPAREN'),
    #     ('left', 'PLUS', 'TIMES'),
    # )

    precedence = (
        ('left', 'TIMES'),
        ('left', 'PLUS'),
    )

    def __init__(self, **kwargs):
        # Build the lexer
        self.lexer = lex.lex(module=self, **kwargs)

        # Build the parser
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, text):
        return self.parser.parse(text, lexer=self.lexer)


if __name__ == '__main__':
    p = Parser(debug=True)

    print('\n'.join((str(p.parse(l)) for l in TEST1.splitlines() if l)))
    print(sum((p.parse(l) for l in INPUT.splitlines() if l)))
