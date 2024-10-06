class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        # Initialize product details
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        """Show product details."""
        print(f" Product: {self.product_name} | Price: {self.price} shillings | Stock: {self.quantity_in_stock} available")


class ShoppingCart:
    total_carts = 0  # Count of shopping carts created

    def __init__(self):
        self.items = []  # Cart items list
        ShoppingCart.total_carts += 1  # Increment cart count

    def add_to_cart(self, product, quantity):
        "Add product to cart if stock is available."
        if 0 < quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity  # Reduce stock
            print(f"Item Added {quantity} x {product.product_name} to your cart! 🎉")
        else:
            print(f"Sorry, can't add {quantity} of {product.product_name}. Out of stock.")

        #removing items from cart

    def remove_from_cart(self, product):
        "Remove an item from the cart."
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]  # Restore stock
                print(f"Item Removed {product.product_name} from your cart.")
                return
        

    def display_cart(self):
        "Show items in the cart."
        if not self.items:
            print(" Your cart is empty. Add something to cart!")
            return
        print("🛒 Your Shopping Cart:")
        for product, quantity in self.items:
            print(f"- {product.product_name}: {quantity} units")

    def calculate_total(self):
        "Calculate total price."
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

   


# Example usage
if __name__ == "__main__":
    # Create products
    product1 = Product("suitcase", 90000, 5)
    product2 = Product("paint", 100000, 10)
    product3 = Product("earphones", 6000, 20)
    product4 = Product("soap", 3500, 15)
    product5 = Product("blanket", 10000, 10)

    # Display product info
    product1.display_product_info()
    product2.display_product_info()
    product3.display_product_info()

    # Create shopping carts
    cart1 = ShoppingCart()
    

    # Add items to cart1
    cart1.add_to_cart(product1, 2)  # 2 suitcases
    cart1.add_to_cart(product2, 3)  # 3 tins of paint
    cart1.display_cart()

    print(f" Total for cart1: {cart1.calculate_total()} shillings\n")
    
   # Remove an item from cart1
    cart1.remove_from_cart(product2, 1)
    cart1.display_cart()
    print(f" Total for cart1 after removal:{cart1.calculate_total()} shillings")

   
    


