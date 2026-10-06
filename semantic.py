from StoreLangVisitor import StoreLangVisitor


class SemanticAnalyzer(StoreLangVisitor):

    def __init__(self):
        super().__init__()
        self.productos = {}
        self.proveedores = {}
        self.operaciones = {}
        self.errors = []

    def error(self, mensaje):
        self.errors.append(mensaje)

    def analizar_declaraciones(self, tree):
        for construccion in tree.construccion():
            if construccion.producto():
                ctx = construccion.producto()
                identificador = ctx.ID().getText()
                if identificador in self.productos:
                    self.error(f"Producto duplicado: '{identificador}'")
                else:
                    self.productos[identificador] = ctx

            elif construccion.proveedor():
                ctx = construccion.proveedor()
                identificador = ctx.ID().getText()
                if identificador in self.proveedores:
                    self.error(f"Proveedor duplicado: '{identificador}'")
                else:
                    self.proveedores[identificador] = ctx

    def analizar_referencias(self, tree):
        for construccion in tree.construccion():

            if construccion.compra():
                ctx = construccion.compra()
                operacion_id = ctx.ID().getText()
                self.validar_operacion(operacion_id, "compra")

                proveedor_id = ctx.proveedorRef().ID().getText()
                producto_id = ctx.productoRef().ID().getText()

                if proveedor_id not in self.proveedores:
                    self.error(f"Proveedor inexistente en compra "
                               f"'{operacion_id}': '{proveedor_id}'")

                if producto_id not in self.productos:
                    self.error(f"Producto inexistente en compra "
                               f"'{operacion_id}': '{producto_id}'")

                cantidad = int(ctx.cantidad().ENTERO().getText())
                if cantidad <= 0:
                    self.error(f"La cantidad de la compra "
                               f"'{operacion_id}' debe ser mayor que 0")

            elif construccion.venta():
                ctx = construccion.venta()
                operacion_id = ctx.ID().getText()
                self.validar_operacion(operacion_id, "venta")

                for item in ctx.listaItems().itemVenta():
                    producto_id = item.ID().getText()
                    cantidad = int(item.ENTERO().getText())

                    if producto_id not in self.productos:
                        self.error(f"Producto inexistente en venta "
                                   f"'{operacion_id}': '{producto_id}'")

                    if cantidad <= 0:
                        self.error(f"La cantidad de la venta "
                                   f"'{operacion_id}' debe ser mayor que 0")

    def validar_operacion(self, identificador, tipo):
        if identificador in self.operaciones:
            self.error(f"ID de operación duplicado: '{identificador}'")
        else:
            self.operaciones[identificador] = tipo

    def analizar(self, tree):
        self.analizar_declaraciones(tree)
        self.analizar_referencias(tree)
        return self.errors