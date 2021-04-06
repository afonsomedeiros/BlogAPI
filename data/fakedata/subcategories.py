from app.models import Subcategory, User
from settings import ROOT_PATH
import csv


def create():
    print("Criando tabela Subcategory")
    Subcategory.create_table()
    print("Tabela Criada com sucesso.")


def create_subcategories_test():
    attr = ['name', 'description', 'is_active', 'author', 'category']
    file = f"{ROOT_PATH}/data/fakedata/csv/subcategories.csv"
    with open(file) as f:
        reader = csv.reader(f, delimiter=";")
        count = 0
        for row in reader:
            if count == 0:
                print("Criando dados falsos.")
                count += 1
            else:
                Subcategory(**dict(zip(attr, row))).save()
