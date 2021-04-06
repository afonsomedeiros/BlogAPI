from app.models import Post
from settings import ROOT_PATH
import csv


def create():
    print("Criando tabela Post")
    Post.create_table()
    print("Tabela Criada com sucesso.")


def create_posts_test():
    attr = ['title', 'content', 'author', 'subcategory', "status"]
    file = f"{ROOT_PATH}/data/fakedata/csv/posts.csv"
    with open(file) as f:
        reader = csv.reader(f, delimiter=";")
        count = 0
        for row in reader:
            if count == 0:
                print("Criando dados falsos.")
                count += 1
            else:
                Post(**dict(zip(attr, row))).save()
