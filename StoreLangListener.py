# Generated from StoreLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .StoreLangParser import StoreLangParser
else:
    from StoreLangParser import StoreLangParser

# This class defines a complete listener for a parse tree produced by StoreLangParser.
class StoreLangListener(ParseTreeListener):

    # Enter a parse tree produced by StoreLangParser#programa.
    def enterPrograma(self, ctx:StoreLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by StoreLangParser#programa.
    def exitPrograma(self, ctx:StoreLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by StoreLangParser#construccion.
    def enterConstruccion(self, ctx:StoreLangParser.ConstruccionContext):
        pass

    # Exit a parse tree produced by StoreLangParser#construccion.
    def exitConstruccion(self, ctx:StoreLangParser.ConstruccionContext):
        pass


    # Enter a parse tree produced by StoreLangParser#producto.
    def enterProducto(self, ctx:StoreLangParser.ProductoContext):
        pass

    # Exit a parse tree produced by StoreLangParser#producto.
    def exitProducto(self, ctx:StoreLangParser.ProductoContext):
        pass


    # Enter a parse tree produced by StoreLangParser#nombre.
    def enterNombre(self, ctx:StoreLangParser.NombreContext):
        pass

    # Exit a parse tree produced by StoreLangParser#nombre.
    def exitNombre(self, ctx:StoreLangParser.NombreContext):
        pass


    # Enter a parse tree produced by StoreLangParser#precio.
    def enterPrecio(self, ctx:StoreLangParser.PrecioContext):
        pass

    # Exit a parse tree produced by StoreLangParser#precio.
    def exitPrecio(self, ctx:StoreLangParser.PrecioContext):
        pass


    # Enter a parse tree produced by StoreLangParser#categoria.
    def enterCategoria(self, ctx:StoreLangParser.CategoriaContext):
        pass

    # Exit a parse tree produced by StoreLangParser#categoria.
    def exitCategoria(self, ctx:StoreLangParser.CategoriaContext):
        pass


    # Enter a parse tree produced by StoreLangParser#proveedor.
    def enterProveedor(self, ctx:StoreLangParser.ProveedorContext):
        pass

    # Exit a parse tree produced by StoreLangParser#proveedor.
    def exitProveedor(self, ctx:StoreLangParser.ProveedorContext):
        pass


    # Enter a parse tree produced by StoreLangParser#nombreProveedor.
    def enterNombreProveedor(self, ctx:StoreLangParser.NombreProveedorContext):
        pass

    # Exit a parse tree produced by StoreLangParser#nombreProveedor.
    def exitNombreProveedor(self, ctx:StoreLangParser.NombreProveedorContext):
        pass


    # Enter a parse tree produced by StoreLangParser#contacto.
    def enterContacto(self, ctx:StoreLangParser.ContactoContext):
        pass

    # Exit a parse tree produced by StoreLangParser#contacto.
    def exitContacto(self, ctx:StoreLangParser.ContactoContext):
        pass


    # Enter a parse tree produced by StoreLangParser#compra.
    def enterCompra(self, ctx:StoreLangParser.CompraContext):
        pass

    # Exit a parse tree produced by StoreLangParser#compra.
    def exitCompra(self, ctx:StoreLangParser.CompraContext):
        pass


    # Enter a parse tree produced by StoreLangParser#proveedorRef.
    def enterProveedorRef(self, ctx:StoreLangParser.ProveedorRefContext):
        pass

    # Exit a parse tree produced by StoreLangParser#proveedorRef.
    def exitProveedorRef(self, ctx:StoreLangParser.ProveedorRefContext):
        pass


    # Enter a parse tree produced by StoreLangParser#productoRef.
    def enterProductoRef(self, ctx:StoreLangParser.ProductoRefContext):
        pass

    # Exit a parse tree produced by StoreLangParser#productoRef.
    def exitProductoRef(self, ctx:StoreLangParser.ProductoRefContext):
        pass


    # Enter a parse tree produced by StoreLangParser#cantidad.
    def enterCantidad(self, ctx:StoreLangParser.CantidadContext):
        pass

    # Exit a parse tree produced by StoreLangParser#cantidad.
    def exitCantidad(self, ctx:StoreLangParser.CantidadContext):
        pass


    # Enter a parse tree produced by StoreLangParser#costo.
    def enterCosto(self, ctx:StoreLangParser.CostoContext):
        pass

    # Exit a parse tree produced by StoreLangParser#costo.
    def exitCosto(self, ctx:StoreLangParser.CostoContext):
        pass


    # Enter a parse tree produced by StoreLangParser#venta.
    def enterVenta(self, ctx:StoreLangParser.VentaContext):
        pass

    # Exit a parse tree produced by StoreLangParser#venta.
    def exitVenta(self, ctx:StoreLangParser.VentaContext):
        pass


    # Enter a parse tree produced by StoreLangParser#listaItems.
    def enterListaItems(self, ctx:StoreLangParser.ListaItemsContext):
        pass

    # Exit a parse tree produced by StoreLangParser#listaItems.
    def exitListaItems(self, ctx:StoreLangParser.ListaItemsContext):
        pass


    # Enter a parse tree produced by StoreLangParser#itemVenta.
    def enterItemVenta(self, ctx:StoreLangParser.ItemVentaContext):
        pass

    # Exit a parse tree produced by StoreLangParser#itemVenta.
    def exitItemVenta(self, ctx:StoreLangParser.ItemVentaContext):
        pass


    # Enter a parse tree produced by StoreLangParser#reporte.
    def enterReporte(self, ctx:StoreLangParser.ReporteContext):
        pass

    # Exit a parse tree produced by StoreLangParser#reporte.
    def exitReporte(self, ctx:StoreLangParser.ReporteContext):
        pass


    # Enter a parse tree produced by StoreLangParser#tipoReporte.
    def enterTipoReporte(self, ctx:StoreLangParser.TipoReporteContext):
        pass

    # Exit a parse tree produced by StoreLangParser#tipoReporte.
    def exitTipoReporte(self, ctx:StoreLangParser.TipoReporteContext):
        pass


    # Enter a parse tree produced by StoreLangParser#filtro.
    def enterFiltro(self, ctx:StoreLangParser.FiltroContext):
        pass

    # Exit a parse tree produced by StoreLangParser#filtro.
    def exitFiltro(self, ctx:StoreLangParser.FiltroContext):
        pass



del StoreLangParser