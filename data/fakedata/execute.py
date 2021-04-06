from . import users, categories, subcategories, posts

print("Executando funções para Usuários")

users.create()
users.create_superuser()
users.create_users_test()

print("Executando funções para Categorias")

categories.create()
categories.create_categories_test()

print("Executando funções para Subcategorias")

subcategories.create()
subcategories.create_subcategories_test()

print("Executando funções para Posts")
posts.create()
posts.create_posts_test()
