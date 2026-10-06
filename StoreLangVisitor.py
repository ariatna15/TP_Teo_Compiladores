# Generated from StoreLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .StoreLangParser import StoreLangParser
else:
    from StoreLangParser import StoreLangParser

# This class defines a complete generic visitor for a parse tree produced by StoreLangParser.

class StoreLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StoreLangParser#programa.
    def visitPrograma(self, ctx:StoreLangParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#construccion.
    def visitConstruccion(self, ctx:StoreLangParser.ConstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#producto.
    def visitProducto(self, ctx:StoreLangParser.ProductoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#nombre.
    def visitNombre(self, ctx:StoreLangParser.NombreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#precio.
    def visitPrecio(self, ctx:StoreLangParser.PrecioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#categoria.
    def visitCategoria(self, ctx:StoreLangParser.CategoriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#proveedor.
    def visitProveedor(self, ctx:StoreLangParser.ProveedorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#nombreProveedor.
    def visitNombreProveedor(self, ctx:StoreLangParser.NombreProveedorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#contacto.
    def visitContacto(self, ctx:StoreLangParser.ContactoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#compra.
    def visitCompra(self, ctx:StoreLangParser.CompraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#proveedorRef.
    def visitProveedorRef(self, ctx:StoreLangParser.ProveedorRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#productoRef.
    def visitProductoRef(self, ctx:StoreLangParser.ProductoRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#cantidad.
    def visitCantidad(self, ctx:StoreLangParser.CantidadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#costo.
    def visitCosto(self, ctx:StoreLangParser.CostoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#venta.
    def visitVenta(self, ctx:StoreLangParser.VentaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#listaItems.
    def visitListaItems(self, ctx:StoreLangParser.ListaItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#itemVenta.
    def visitItemVenta(self, ctx:StoreLangParser.ItemVentaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#reporte.
    def visitReporte(self, ctx:StoreLangParser.ReporteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#tipoReporte.
    def visitTipoReporte(self, ctx:StoreLangParser.TipoReporteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreLangParser#filtro.
    def visitFiltro(self, ctx:StoreLangParser.FiltroContext):
        return self.visitChildren(ctx)



del StoreLangParser