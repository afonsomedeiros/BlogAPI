from app.models import Category, User
from settings import ROOT_PATH
import csv


def create():
    print("Criando tabela Category")
    Category.create_table()
    print("Tabela Criada com sucesso.")


def create_categories_test():
    attr = ['name', 'description', 'is_active', 'author']
    file = f"{ROOT_PATH}/data/fakedata/csv/categories.csv"
    with open(file) as f:
        reader = csv.reader(f, delimiter=";")
        count = 0
        for row in reader:
            if count == 0:
                print("Criando dados falsos.")
                count += 1
            else:
                Category(**dict(zip(attr, row))).save()
