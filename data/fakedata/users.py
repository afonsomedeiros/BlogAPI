from app.models import User
from settings import ROOT_PATH
import csv


def create():
    print("Criando tabela User")
    User.create_table()
    print("Tabela Criada com sucesso.")


def create_superuser():
    print("Criando super usuário.")
    user = User(name="Afonso", last_name="Medeiros", status=0,
                email="afonso@afonso.com", password="123456")
    user.gen_hash()
    user.save()
    print("Usuário criado.")


def create_users_test():
    file = f"{ROOT_PATH}/data/fakedata/csv/users.csv"
    with open(file) as f:
        reader = csv.reader(f, delimiter=";")
        count = 0
        for row in reader:
            if count == 0:
                print("Criando dados falsos.")
                count += 1
            else:
                user = User(name=row[0], last_name=row[1], status=row[2],
                            email=row[3], password=row[4], birthday=row[5])
                user.gen_hash()
                user.save()
                count += 1
        print("Usuários falsos criados com sucesso.")
