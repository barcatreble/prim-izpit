class Market:
    def __init__(self, barcod, name, manufacturer, price, quantity):
        self.barcod = barcod
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity

    def sale(self,quantity):
        self.quantity -= quantity
        return self.quantity
    
    def discount(self):
        if self.price>=30 and self.price<=50:
            self.price = 0.95 * self.price
        elif self.price >=10 and self.price<=30:
            self.price = 0.93 * self.price
        elif self.price<=10 or self.price>=50:
            self.price = self.price

product_list = []
n = int(input("Въведи брой елементи:"))
print("Въведи данните за продуктите в следния ред: баркод, име, производител, цена, количество")
for i in range(1, n+1):
    product = Market(input(), input(), input(), float(input()), int(input()))
    product_list.append(product)

def search_by_barcod(product_list, barcod):
    if product.barcod == barcod:
        print(f"Име на продукт: {product.name}\nПроизводител: {product.manufacturer}\nЦена: {product.price}\nКоличество: {product.quantity}")
    else:
        print("Wrong barcod!")
        print("Налични баркодове:")
        for product in product_list:
            print(product.barcod)
        
def search_by_manufacturer(product_list, manufacturer):
    manufacturer_products = []
    sum = 0
    count = 0
    for product in product_list:
        if product.manufacturer == manufacturer:
            sum+=product.price
            count+=1
    avg_price = sum/count
    for product in product_list:
        if product.manufacturer == manufacturer and product.price <= avg_price:
            manufacturer_products.append(product)

        return manufacturer_products

def sort_by_quantity(product_list):
    sorted_list = sorted(product_list, key=lambda product: product.quantity)
    for product in sorted_list:
        print(product)

    return sorted_list
        
def delete_by_name(product_list, name):
    del_products_list = []
    for product in product_list:
        if product.name == name and product.quantity<=3:
            del_products_list.append(product)

    return del_products_list
