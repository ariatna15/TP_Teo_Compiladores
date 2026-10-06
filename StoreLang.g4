
grammar StoreLang;


// ==== PARSER

programa
    : construccion* EOF
    ;

construccion
    : producto
    | proveedor
    | compra
    | venta
    | reporte
    ;


// ----  PRODUCTO

producto
    : PRODUCTO ID LBRACE nombre precio categoria RBRACE
    ;

nombre
    : NOMBRE ASSIGN CADENA SEMI
    ;

precio
    : PRECIO ASSIGN DECIMAL SEMI
    ;

categoria
    : CATEGORIA ASSIGN CADENA SEMI
    ;


// ----  PROVEEDOR

proveedor
    : PROVEEDOR ID LBRACE nombreProveedor contacto RBRACE
    ;

nombreProveedor
    : NOMBRE ASSIGN CADENA SEMI
    ;

contacto
    : CONTACTO ASSIGN CADENA SEMI
    ;


// ----  COMPRA

compra
    : COMPRA ID LBRACE proveedorRef productoRef cantidad costo RBRACE
    ;

proveedorRef
    : PROVEEDOR ASSIGN ID SEMI
    ;

productoRef
    : PRODUCTO ASSIGN ID SEMI
    ;

cantidad
    : CANTIDAD ASSIGN ENTERO SEMI
    ;

costo
    : COSTO ASSIGN DECIMAL SEMI
    ;


// ----  VENTA

venta
    : VENTA ID LBRACE listaItems RBRACE
    ;

listaItems
    : itemVenta+
    ;

itemVenta
    : PRODUCTO ASSIGN ID SEMI
      CANTIDAD ASSIGN ENTERO SEMI
    ;


// ----  REPORTE

reporte
    : REPORTE tipoReporte filtro? SEMI
    ;

tipoReporte
    : STOCK
    | VENTAS
    | PRODUCTOS
    ;

filtro
    : CATEGORIA ASSIGN CADENA
    | PRODUCTO ASSIGN ID
    ;


// ==== LEXER

// ----  Palabras reservadas
PRODUCTO    : 'producto';
PROVEEDOR   : 'proveedor';
COMPRA      : 'compra';
VENTA       : 'venta';
REPORTE     : 'reporte';

NOMBRE      : 'nombre';
PRECIO      : 'precio';
CATEGORIA   : 'categoria';
CONTACTO    : 'contacto';

CANTIDAD    : 'cantidad';
COSTO       : 'costo';

STOCK       : 'stock';
VENTAS      : 'ventas';
PRODUCTOS   : 'productos';

// ----  Símbolos
LBRACE      : '{';
RBRACE      : '}';
ASSIGN      : '=';
SEMI        : ';';

// ----  Valores
DECIMAL
    : [0-9]+ '.' [0-9]+
    ;

ENTERO
    : [0-9]+
    ;

CADENA
    : '"' ~[\r\n"]* '"'
    ;

ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

// ----  Espacios y comentarios
WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '//' ~[\r\n]* -> skip
    ;
