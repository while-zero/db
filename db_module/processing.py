import db_module.models


def first_client_function(src: db_module.models.Source):
    print(f"source file name: {src.name}")
    print('xxx')

def second_client_function(src: db_module.models.Source):
    print(f"source file name: {src.name}")
    print('yyy')
