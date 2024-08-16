from pprint import pprint
import os
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    def get_products(self):
        __file_name = 'products.txt'
        file_content = []
        if __file_name in os.listdir(os.getcwd()):
            file = open(__file_name, 'r')
            file_content = file.read()
            file.close()
        return file_content


    def add(self, *products):
        __file_name = 'products.txt'
        for i in products:
            if i.name in self.get_products():
                print(f'Продукт {i.name} уже есть в магазине.')
            else:
                file = open(__file_name, 'a', encoding='utf-8')
                i = str(i)
                file.write(i)
                file.write('\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)
print(s1.get_products())
