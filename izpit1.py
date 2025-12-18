#1
import random
while True:
    try:
        n = int(input("Въведи цяло число между 10 и 50: "))
        if 10<n<50:
            break
        else:
            print(f"Числото {n} не е в интервала (10,50)!")

    except:
        print("Трябва да въведете число!")

mylst_1 = []   
a = random.randint(-2500, -1300)
b= random.randint(1111, 4444)
for num in range(n):
    num = int(input())
    if a < num < b:
        mylst_1.append(num)
print(mylst_1)

count = 0
for num in mylst_1:
    des = num % 10
    if num < 0 and (des % 4 == 0 or des % 5 == 0):
        count+=1
print(f"Броят на отрицателните числа, кратни на 4 или 5 е: {count}")

sum1=0
count1 = 0
for num in mylst_1:
    if 10<=num<=99 and num % 2 == 0:
        sum1 += num
        count1+=1
avg = sum1/count1
print(f"Средноаритметичното на двуцифрените четни елементи е: {avg}")

mylst_2 = []
for num in mylst_2:
    if 100<=num<=999 and num % 3 == 0:
        mylst_2.append(num)
print(mylst_2)

count1 = 0
for i in range(len(mylst_2)):
    if mylst_2[i] % 2 == 1 and i % 2 == 0:
        count1+=1
print(f"Броят на нечетните числа с четен индекс е: {count1}")

for i in range(len(mylst_2)):
    if i % 2 == 1:
        mylst_2[i] = 13
print(mylst_2)

dulj = 0
if len(mylst_1) > len(mylst_2):
    dulj = mylst_1
elif len(mylst_1) < len(mylst_2):
    dulj = mylst_2

dulj.pop[0]
dulj.pop[-1]

#2
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
    for product in product_list:
        if product.barcod == barcod:
            print(f"Име на продукт: {product.name}\nПроизводител: {product.manufacturer}\nЦена: {product.price}\nКоличество: {product.quantity}")
            break
    else:
        print("Wrong barcod!")
        print("Налични баркодове: ")
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
        print(f"Име на продукт: {product.name}\nПроизводител: {product.manufacturer}\nЦена: {product.price}\nКоличество: {product.quantity}")
    return sorted_list
        
def delete_by_name(product_list, name):
    del_products_list = []
    for product in product_list:
        if product.name == name and product.quantity<=3:
            del_products_list.append(product)
    return del_products_list