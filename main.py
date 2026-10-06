import sys
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from StoreLangLexer import StoreLangLexer
from StoreLangParser import StoreLangParser
from semantic import SemanticAnalyzer


class CollectorErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Línea {line}, columna {column}: {msg}")


def compilar(codigo):
    lexer = StoreLangLexer(InputStream(codigo))
    lex_err = CollectorErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lex_err)

    parser = StoreLangParser(CommonTokenStream(lexer))
    syn_err = CollectorErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(syn_err)

    tree = parser.programa()

    if lex_err.errors or syn_err.errors:
        for e in lex_err.errors:
            print("Error léxico:", e)
        for e in syn_err.errors:
            print("Error sintáctico:", e)
        return False

    errores = SemanticAnalyzer().analizar(tree)
    if errores:
        for e in errores:
            print("Error semántico:", e)
        return False

    print("Correcto: el programa supera el análisis léxico, sintáctico y semántico.")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <archivo.store>")
        sys.exit(2)
    with open(sys.argv[1], encoding="utf-8") as f:
        ok = compilar(f.read())
    sys.exit(0 if ok else 1)