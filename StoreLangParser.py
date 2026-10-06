# Generated from StoreLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,162,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,54,8,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        1,14,1,15,4,15,132,8,15,11,15,12,15,133,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,17,1,17,1,17,3,17,148,8,17,1,17,1,17,1,18,
        1,18,1,19,1,19,1,19,1,19,1,19,1,19,3,19,160,8,19,1,19,0,0,20,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,1,1,0,12,14,
        149,0,43,1,0,0,0,2,53,1,0,0,0,4,55,1,0,0,0,6,63,1,0,0,0,8,68,1,0,
        0,0,10,73,1,0,0,0,12,78,1,0,0,0,14,85,1,0,0,0,16,90,1,0,0,0,18,95,
        1,0,0,0,20,104,1,0,0,0,22,109,1,0,0,0,24,114,1,0,0,0,26,119,1,0,
        0,0,28,124,1,0,0,0,30,131,1,0,0,0,32,135,1,0,0,0,34,144,1,0,0,0,
        36,151,1,0,0,0,38,159,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,45,
        1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,
        46,47,5,0,0,1,47,1,1,0,0,0,48,54,3,4,2,0,49,54,3,12,6,0,50,54,3,
        18,9,0,51,54,3,28,14,0,52,54,3,34,17,0,53,48,1,0,0,0,53,49,1,0,0,
        0,53,50,1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,3,1,0,0,0,55,56,5,
        1,0,0,56,57,5,22,0,0,57,58,5,15,0,0,58,59,3,6,3,0,59,60,3,8,4,0,
        60,61,3,10,5,0,61,62,5,16,0,0,62,5,1,0,0,0,63,64,5,6,0,0,64,65,5,
        17,0,0,65,66,5,21,0,0,66,67,5,18,0,0,67,7,1,0,0,0,68,69,5,7,0,0,
        69,70,5,17,0,0,70,71,5,19,0,0,71,72,5,18,0,0,72,9,1,0,0,0,73,74,
        5,8,0,0,74,75,5,17,0,0,75,76,5,21,0,0,76,77,5,18,0,0,77,11,1,0,0,
        0,78,79,5,2,0,0,79,80,5,22,0,0,80,81,5,15,0,0,81,82,3,14,7,0,82,
        83,3,16,8,0,83,84,5,16,0,0,84,13,1,0,0,0,85,86,5,6,0,0,86,87,5,17,
        0,0,87,88,5,21,0,0,88,89,5,18,0,0,89,15,1,0,0,0,90,91,5,9,0,0,91,
        92,5,17,0,0,92,93,5,21,0,0,93,94,5,18,0,0,94,17,1,0,0,0,95,96,5,
        3,0,0,96,97,5,22,0,0,97,98,5,15,0,0,98,99,3,20,10,0,99,100,3,22,
        11,0,100,101,3,24,12,0,101,102,3,26,13,0,102,103,5,16,0,0,103,19,
        1,0,0,0,104,105,5,2,0,0,105,106,5,17,0,0,106,107,5,22,0,0,107,108,
        5,18,0,0,108,21,1,0,0,0,109,110,5,1,0,0,110,111,5,17,0,0,111,112,
        5,22,0,0,112,113,5,18,0,0,113,23,1,0,0,0,114,115,5,10,0,0,115,116,
        5,17,0,0,116,117,5,20,0,0,117,118,5,18,0,0,118,25,1,0,0,0,119,120,
        5,11,0,0,120,121,5,17,0,0,121,122,5,19,0,0,122,123,5,18,0,0,123,
        27,1,0,0,0,124,125,5,4,0,0,125,126,5,22,0,0,126,127,5,15,0,0,127,
        128,3,30,15,0,128,129,5,16,0,0,129,29,1,0,0,0,130,132,3,32,16,0,
        131,130,1,0,0,0,132,133,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,
        134,31,1,0,0,0,135,136,5,1,0,0,136,137,5,17,0,0,137,138,5,22,0,0,
        138,139,5,18,0,0,139,140,5,10,0,0,140,141,5,17,0,0,141,142,5,20,
        0,0,142,143,5,18,0,0,143,33,1,0,0,0,144,145,5,5,0,0,145,147,3,36,
        18,0,146,148,3,38,19,0,147,146,1,0,0,0,147,148,1,0,0,0,148,149,1,
        0,0,0,149,150,5,18,0,0,150,35,1,0,0,0,151,152,7,0,0,0,152,37,1,0,
        0,0,153,154,5,8,0,0,154,155,5,17,0,0,155,160,5,21,0,0,156,157,5,
        1,0,0,157,158,5,17,0,0,158,160,5,22,0,0,159,153,1,0,0,0,159,156,
        1,0,0,0,160,39,1,0,0,0,5,43,53,133,147,159
    ]

class StoreLangParser ( Parser ):

    grammarFileName = "StoreLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'producto'", "'proveedor'", "'compra'", 
                     "'venta'", "'reporte'", "'nombre'", "'precio'", "'categoria'", 
                     "'contacto'", "'cantidad'", "'costo'", "'stock'", "'ventas'", 
                     "'productos'", "'{'", "'}'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>", "PRODUCTO", "PROVEEDOR", "COMPRA", "VENTA", 
                      "REPORTE", "NOMBRE", "PRECIO", "CATEGORIA", "CONTACTO", 
                      "CANTIDAD", "COSTO", "STOCK", "VENTAS", "PRODUCTOS", 
                      "LBRACE", "RBRACE", "ASSIGN", "SEMI", "DECIMAL", "ENTERO", 
                      "CADENA", "ID", "WS", "COMMENT" ]

    RULE_programa = 0
    RULE_construccion = 1
    RULE_producto = 2
    RULE_nombre = 3
    RULE_precio = 4
    RULE_categoria = 5
    RULE_proveedor = 6
    RULE_nombreProveedor = 7
    RULE_contacto = 8
    RULE_compra = 9
    RULE_proveedorRef = 10
    RULE_productoRef = 11
    RULE_cantidad = 12
    RULE_costo = 13
    RULE_venta = 14
    RULE_listaItems = 15
    RULE_itemVenta = 16
    RULE_reporte = 17
    RULE_tipoReporte = 18
    RULE_filtro = 19

    ruleNames =  [ "programa", "construccion", "producto", "nombre", "precio", 
                   "categoria", "proveedor", "nombreProveedor", "contacto", 
                   "compra", "proveedorRef", "productoRef", "cantidad", 
                   "costo", "venta", "listaItems", "itemVenta", "reporte", 
                   "tipoReporte", "filtro" ]

    EOF = Token.EOF
    PRODUCTO=1
    PROVEEDOR=2
    COMPRA=3
    VENTA=4
    REPORTE=5
    NOMBRE=6
    PRECIO=7
    CATEGORIA=8
    CONTACTO=9
    CANTIDAD=10
    COSTO=11
    STOCK=12
    VENTAS=13
    PRODUCTOS=14
    LBRACE=15
    RBRACE=16
    ASSIGN=17
    SEMI=18
    DECIMAL=19
    ENTERO=20
    CADENA=21
    ID=22
    WS=23
    COMMENT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(StoreLangParser.EOF, 0)

        def construccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoreLangParser.ConstruccionContext)
            else:
                return self.getTypedRuleContext(StoreLangParser.ConstruccionContext,i)


        def getRuleIndex(self):
            return StoreLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = StoreLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0):
                self.state = 40
                self.construccion()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(StoreLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def producto(self):
            return self.getTypedRuleContext(StoreLangParser.ProductoContext,0)


        def proveedor(self):
            return self.getTypedRuleContext(StoreLangParser.ProveedorContext,0)


        def compra(self):
            return self.getTypedRuleContext(StoreLangParser.CompraContext,0)


        def venta(self):
            return self.getTypedRuleContext(StoreLangParser.VentaContext,0)


        def reporte(self):
            return self.getTypedRuleContext(StoreLangParser.ReporteContext,0)


        def getRuleIndex(self):
            return StoreLangParser.RULE_construccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstruccion" ):
                listener.enterConstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstruccion" ):
                listener.exitConstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstruccion" ):
                return visitor.visitConstruccion(self)
            else:
                return visitor.visitChildren(self)




    def construccion(self):

        localctx = StoreLangParser.ConstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_construccion)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.producto()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.proveedor()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.compra()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.venta()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.reporte()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProductoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRODUCTO(self):
            return self.getToken(StoreLangParser.PRODUCTO, 0)

        def ID(self):
            return self.getToken(StoreLangParser.ID, 0)

        def LBRACE(self):
            return self.getToken(StoreLangParser.LBRACE, 0)

        def nombre(self):
            return self.getTypedRuleContext(StoreLangParser.NombreContext,0)


        def precio(self):
            return self.getTypedRuleContext(StoreLangParser.PrecioContext,0)


        def categoria(self):
            return self.getTypedRuleContext(StoreLangParser.CategoriaContext,0)


        def RBRACE(self):
            return self.getToken(StoreLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_producto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProducto" ):
                listener.enterProducto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProducto" ):
                listener.exitProducto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProducto" ):
                return visitor.visitProducto(self)
            else:
                return visitor.visitChildren(self)




    def producto(self):

        localctx = StoreLangParser.ProductoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_producto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(StoreLangParser.PRODUCTO)
            self.state = 56
            self.match(StoreLangParser.ID)
            self.state = 57
            self.match(StoreLangParser.LBRACE)
            self.state = 58
            self.nombre()
            self.state = 59
            self.precio()
            self.state = 60
            self.categoria()
            self.state = 61
            self.match(StoreLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NombreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOMBRE(self):
            return self.getToken(StoreLangParser.NOMBRE, 0)

        def ASSIGN(self):
            return self.getToken(StoreLangParser.ASSIGN, 0)

        def CADENA(self):
            return self.getToken(StoreLangParser.CADENA, 0)

        def SEMI(self):
            return self.getToken(StoreLangParser.SEMI, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_nombre

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNombre" ):
                listener.enterNombre(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNombre" ):
                listener.exitNombre(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNombre" ):
                return visitor.visitNombre(self)
            else:
                return visitor.visitChildren(self)




    def nombre(self):

        localctx = StoreLangParser.NombreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nombre)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(StoreLangParser.NOMBRE)
            self.state = 64
            self.match(StoreLangParser.ASSIGN)
            self.state = 65
            self.match(StoreLangParser.CADENA)
            self.state = 66
            self.match(StoreLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrecioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRECIO(self):
            return self.getToken(StoreLangParser.PRECIO, 0)

        def ASSIGN(self):
            return self.getToken(StoreLangParser.ASSIGN, 0)

        def DECIMAL(self):
            return self.getToken(StoreLangParser.DECIMAL, 0)

        def SEMI(self):
            return self.getToken(StoreLangParser.SEMI, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_precio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecio" ):
                listener.enterPrecio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecio" ):
                listener.exitPrecio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecio" ):
                return visitor.visitPrecio(self)
            else:
                return visitor.visitChildren(self)




    def precio(self):

        localctx = StoreLangParser.PrecioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_precio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(StoreLangParser.PRECIO)
            self.state = 69
            self.match(StoreLangParser.ASSIGN)
            self.state = 70
            self.match(StoreLangParser.DECIMAL)
            self.state = 71
            self.match(StoreLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CategoriaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATEGORIA(self):
            return self.getToken(StoreLangParser.CATEGORIA, 0)

        def ASSIGN(self):
            return self.getToken(StoreLangParser.ASSIGN, 0)

        def CADENA(self):
            return self.getToken(StoreLangParser.CADENA, 0)

        def SEMI(self):
            return self.getToken(StoreLangParser.SEMI, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_categoria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCategoria" ):
                listener.enterCategoria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCategoria" ):
                listener.exitCategoria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCategoria" ):
                return visitor.visitCategoria(self)
            else:
                return visitor.visitChildren(self)




    def categoria(self):

        localctx = StoreLangParser.CategoriaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_categoria)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(StoreLangParser.CATEGORIA)
            self.state = 74
            self.match(StoreLangParser.ASSIGN)
            self.state = 75
            self.match(StoreLangParser.CADENA)
            self.state = 76
            self.match(StoreLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProveedorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROVEEDOR(self):
            return self.getToken(StoreLangParser.PROVEEDOR, 0)

        def ID(self):
            return self.getToken(StoreLangParser.ID, 0)

        def LBRACE(self):
            return self.getToken(StoreLangParser.LBRACE, 0)

        def nombreProveedor(self):
            return self.getTypedRuleContext(StoreLangParser.NombreProveedorContext,0)


        def contacto(self):
            return self.getTypedRuleContext(StoreLangParser.ContactoContext,0)


        def RBRACE(self):
            return self.getToken(StoreLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_proveedor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProveedor" ):
                listener.enterProveedor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProveedor" ):
                listener.exitProveedor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProveedor" ):
                return visitor.visitProveedor(self)
            else:
                return visitor.visitChildren(self)




    def proveedor(self):

        localctx = StoreLangParser.ProveedorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_proveedor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(StoreLangParser.PROVEEDOR)
            self.state = 79
            self.match(StoreLangParser.ID)
            self.state = 80
            self.match(StoreLangParser.LBRACE)
            self.state = 81
            self.nombreProveedor()
            self.state = 82
            self.contacto()
            self.state = 83
            self.match(StoreLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NombreProveedorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOMBRE(self):
            return self.getToken(StoreLangParser.NOMBRE, 0)

        def ASSIGN(self):
            return self.getToken(StoreLangParser.ASSIGN, 0)

        def CADENA(self):
            return self.getToken(StoreLangParser.CADENA, 0)

        def SEMI(self):
            return self.getToken(StoreLangParser.SEMI, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_nombreProveedor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNombreProveedor" ):
                listener.enterNombreProveedor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNombreProveedor" ):
                listener.exitNombreProveedor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNombreProveedor" ):
                return visitor.visitNombreProveedor(self)
            else:
                return visitor.visitChildren(self)




    def nombreProveedor(self):

        localctx = StoreLangParser.NombreProveedorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nombreProveedor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(StoreLangParser.NOMBRE)
            self.state = 86
            self.match(StoreLangParser.ASSIGN)
            self.state = 87
            self.match(StoreLangParser.CADENA)
            self.state = 88
            self.match(StoreLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContactoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTACTO(self):
            return self.getToken(StoreLangParser.CONTACTO, 0)

        def ASSIGN(self):
            return self.getToken(StoreLangParser.ASSIGN, 0)

        def CADENA(self):
            return self.getToken(StoreLangParser.CADENA, 0)

        def SEMI(self):
            return self.getToken(StoreLangParser.SEMI, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_contacto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContacto" ):
                listener.enterContacto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContacto" ):
                listener.exitContacto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContacto" ):
                return visitor.visitContacto(self)
            else:
                return visitor.visitChildren(self)




    def contacto(self):

        localctx = StoreLangParser.ContactoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_contacto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(StoreLangParser.CONTACTO)
            self.state = 91
            self.match(StoreLangParser.ASSIGN)
            self.state = 92
            self.match(StoreLangParser.CADENA)
            self.state = 93
            self.match(StoreLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPRA(self):
            return self.getToken(StoreLangParser.COMPRA, 0)

        def ID(self):
            return self.getToken(StoreLangParser.ID, 0)

        def LBRACE(self):
            return self.getToken(StoreLangParser.LBRACE, 0)

        def proveedorRef(self):
            return self.getTypedRuleContext(StoreLangParser.ProveedorRefContext,0)


        def productoRef(self):
            return self.getTypedRuleContext(StoreLangParser.ProductoRefContext,0)


        def cantidad(self):
            return self.getTypedRuleContext(StoreLangParser.CantidadContext,0)


        def costo(self):
            return self.getTypedRuleContext(StoreLangParser.CostoContext,0)


        def RBRACE(self):
            return self.getToken(StoreLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_compra

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompra" ):
                listener.enterCompra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompra" ):
                listener.exitCompra(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompra" ):
                return visitor.visitCompra(self)
            else:
                return visitor.visitChildren(self)




    def compra(self):

        localctx = StoreLangParser.CompraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_compra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(StoreLangParser.COMPRA)
            self.state = 96
            self.match(StoreLangParser.ID)
            self.state = 97
            self.match(StoreLangParser.LBRACE)
            self.state = 98
            self.proveedorRef()
            self.state = 99
            self.productoRef()
            self.state = 100
            self.cantidad()
            self.state = 101
            self.costo()
            self.state = 102
            self.match(StoreLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProveedorRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROVEEDOR(self):
            return self.getToken(StoreLangParser.PROVEEDOR, 0)

        def ASSIGN(self):
            return self.getToken(StoreLangParser.ASSIGN, 0)

        def ID(self):
            return self.getToken(StoreLangParser.ID, 0)

        def SEMI(self):
            return self.getToken(StoreLangParser.SEMI, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_proveedorRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProveedorRef" ):
                listener.enterProveedorRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProveedorRef" ):
                listener.exitProveedorRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProveedorRef" ):
                return visitor.visitProveedorRef(self)
            else:
                return visitor.visitChildren(self)




    def proveedorRef(self):

        localctx = StoreLangParser.ProveedorRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_proveedorRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(StoreLangParser.PROVEEDOR)
            self.state = 105
            self.match(StoreLangParser.ASSIGN)
            self.state = 106
            self.match(StoreLangParser.ID)
            self.state = 107
            self.match(StoreLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProductoRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRODUCTO(self):
            return self.getToken(StoreLangParser.PRODUCTO, 0)

        def ASSIGN(self):
            return self.getToken(StoreLangParser.ASSIGN, 0)

        def ID(self):
            return self.getToken(StoreLangParser.ID, 0)

        def SEMI(self):
            return self.getToken(StoreLangParser.SEMI, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_productoRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProductoRef" ):
                listener.enterProductoRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProductoRef" ):
                listener.exitProductoRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProductoRef" ):
                return visitor.visitProductoRef(self)
            else:
                return visitor.visitChildren(self)




    def productoRef(self):

        localctx = StoreLangParser.ProductoRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_productoRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(StoreLangParser.PRODUCTO)
            self.state = 110
            self.match(StoreLangParser.ASSIGN)
            self.state = 111
            self.match(StoreLangParser.ID)
            self.state = 112
            self.match(StoreLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CantidadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CANTIDAD(self):
            return self.getToken(StoreLangParser.CANTIDAD, 0)

        def ASSIGN(self):
            return self.getToken(StoreLangParser.ASSIGN, 0)

        def ENTERO(self):
            return self.getToken(StoreLangParser.ENTERO, 0)

        def SEMI(self):
            return self.getToken(StoreLangParser.SEMI, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_cantidad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCantidad" ):
                listener.enterCantidad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCantidad" ):
                listener.exitCantidad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCantidad" ):
                return visitor.visitCantidad(self)
            else:
                return visitor.visitChildren(self)




    def cantidad(self):

        localctx = StoreLangParser.CantidadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cantidad)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(StoreLangParser.CANTIDAD)
            self.state = 115
            self.match(StoreLangParser.ASSIGN)
            self.state = 116
            self.match(StoreLangParser.ENTERO)
            self.state = 117
            self.match(StoreLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CostoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COSTO(self):
            return self.getToken(StoreLangParser.COSTO, 0)

        def ASSIGN(self):
            return self.getToken(StoreLangParser.ASSIGN, 0)

        def DECIMAL(self):
            return self.getToken(StoreLangParser.DECIMAL, 0)

        def SEMI(self):
            return self.getToken(StoreLangParser.SEMI, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_costo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosto" ):
                listener.enterCosto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosto" ):
                listener.exitCosto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosto" ):
                return visitor.visitCosto(self)
            else:
                return visitor.visitChildren(self)




    def costo(self):

        localctx = StoreLangParser.CostoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_costo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(StoreLangParser.COSTO)
            self.state = 120
            self.match(StoreLangParser.ASSIGN)
            self.state = 121
            self.match(StoreLangParser.DECIMAL)
            self.state = 122
            self.match(StoreLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VentaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VENTA(self):
            return self.getToken(StoreLangParser.VENTA, 0)

        def ID(self):
            return self.getToken(StoreLangParser.ID, 0)

        def LBRACE(self):
            return self.getToken(StoreLangParser.LBRACE, 0)

        def listaItems(self):
            return self.getTypedRuleContext(StoreLangParser.ListaItemsContext,0)


        def RBRACE(self):
            return self.getToken(StoreLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_venta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVenta" ):
                listener.enterVenta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVenta" ):
                listener.exitVenta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVenta" ):
                return visitor.visitVenta(self)
            else:
                return visitor.visitChildren(self)




    def venta(self):

        localctx = StoreLangParser.VentaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_venta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(StoreLangParser.VENTA)
            self.state = 125
            self.match(StoreLangParser.ID)
            self.state = 126
            self.match(StoreLangParser.LBRACE)
            self.state = 127
            self.listaItems()
            self.state = 128
            self.match(StoreLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaItemsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def itemVenta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoreLangParser.ItemVentaContext)
            else:
                return self.getTypedRuleContext(StoreLangParser.ItemVentaContext,i)


        def getRuleIndex(self):
            return StoreLangParser.RULE_listaItems

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaItems" ):
                listener.enterListaItems(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaItems" ):
                listener.exitListaItems(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaItems" ):
                return visitor.visitListaItems(self)
            else:
                return visitor.visitChildren(self)




    def listaItems(self):

        localctx = StoreLangParser.ListaItemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listaItems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 130
                self.itemVenta()
                self.state = 133 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemVentaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRODUCTO(self):
            return self.getToken(StoreLangParser.PRODUCTO, 0)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(StoreLangParser.ASSIGN)
            else:
                return self.getToken(StoreLangParser.ASSIGN, i)

        def ID(self):
            return self.getToken(StoreLangParser.ID, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(StoreLangParser.SEMI)
            else:
                return self.getToken(StoreLangParser.SEMI, i)

        def CANTIDAD(self):
            return self.getToken(StoreLangParser.CANTIDAD, 0)

        def ENTERO(self):
            return self.getToken(StoreLangParser.ENTERO, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_itemVenta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItemVenta" ):
                listener.enterItemVenta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItemVenta" ):
                listener.exitItemVenta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemVenta" ):
                return visitor.visitItemVenta(self)
            else:
                return visitor.visitChildren(self)




    def itemVenta(self):

        localctx = StoreLangParser.ItemVentaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_itemVenta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(StoreLangParser.PRODUCTO)
            self.state = 136
            self.match(StoreLangParser.ASSIGN)
            self.state = 137
            self.match(StoreLangParser.ID)
            self.state = 138
            self.match(StoreLangParser.SEMI)
            self.state = 139
            self.match(StoreLangParser.CANTIDAD)
            self.state = 140
            self.match(StoreLangParser.ASSIGN)
            self.state = 141
            self.match(StoreLangParser.ENTERO)
            self.state = 142
            self.match(StoreLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReporteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPORTE(self):
            return self.getToken(StoreLangParser.REPORTE, 0)

        def tipoReporte(self):
            return self.getTypedRuleContext(StoreLangParser.TipoReporteContext,0)


        def SEMI(self):
            return self.getToken(StoreLangParser.SEMI, 0)

        def filtro(self):
            return self.getTypedRuleContext(StoreLangParser.FiltroContext,0)


        def getRuleIndex(self):
            return StoreLangParser.RULE_reporte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReporte" ):
                listener.enterReporte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReporte" ):
                listener.exitReporte(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReporte" ):
                return visitor.visitReporte(self)
            else:
                return visitor.visitChildren(self)




    def reporte(self):

        localctx = StoreLangParser.ReporteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_reporte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(StoreLangParser.REPORTE)
            self.state = 145
            self.tipoReporte()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==8:
                self.state = 146
                self.filtro()


            self.state = 149
            self.match(StoreLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoReporteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STOCK(self):
            return self.getToken(StoreLangParser.STOCK, 0)

        def VENTAS(self):
            return self.getToken(StoreLangParser.VENTAS, 0)

        def PRODUCTOS(self):
            return self.getToken(StoreLangParser.PRODUCTOS, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_tipoReporte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoReporte" ):
                listener.enterTipoReporte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoReporte" ):
                listener.exitTipoReporte(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoReporte" ):
                return visitor.visitTipoReporte(self)
            else:
                return visitor.visitChildren(self)




    def tipoReporte(self):

        localctx = StoreLangParser.TipoReporteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_tipoReporte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FiltroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATEGORIA(self):
            return self.getToken(StoreLangParser.CATEGORIA, 0)

        def ASSIGN(self):
            return self.getToken(StoreLangParser.ASSIGN, 0)

        def CADENA(self):
            return self.getToken(StoreLangParser.CADENA, 0)

        def PRODUCTO(self):
            return self.getToken(StoreLangParser.PRODUCTO, 0)

        def ID(self):
            return self.getToken(StoreLangParser.ID, 0)

        def getRuleIndex(self):
            return StoreLangParser.RULE_filtro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFiltro" ):
                listener.enterFiltro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFiltro" ):
                listener.exitFiltro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFiltro" ):
                return visitor.visitFiltro(self)
            else:
                return visitor.visitChildren(self)




    def filtro(self):

        localctx = StoreLangParser.FiltroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_filtro)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(StoreLangParser.CATEGORIA)
                self.state = 154
                self.match(StoreLangParser.ASSIGN)
                self.state = 155
                self.match(StoreLangParser.CADENA)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(StoreLangParser.PRODUCTO)
                self.state = 157
                self.match(StoreLangParser.ASSIGN)
                self.state = 158
                self.match(StoreLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





