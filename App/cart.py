class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart

    def add_product(self, producto):
        id = str(producto.id)
        if id not in self.cart.keys():
            self.cart[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else:
            self.cart[id]["cantidad"] += 1
            self.cart[id]["precio"] = producto.precio
            self.cart[id]["acumulado"] += producto.precio
        self.save_cart()

    def save_cart(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def delete_product(self, producto):
        id = str(producto.id)
        if id in self.cart:
            del self.cart[id]
            self.save_cart()

    def subtract(self, producto):
        id = str(producto.id)
        if id in self.cart.keys():
            self.cart[id]["cantidad"] -= 1
            self.cart[id]["acumulado"] -= producto.precio
            if self.cart[id]["cantidad"] <= 0: self.delete_product(producto)
            self.save_cart()

    def clean(self):
        self.session["cart"] = {}
        self.session.modified = True