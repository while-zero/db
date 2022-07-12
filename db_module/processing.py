import db_module.models


def first_client_function(src: db_module.models.Source):
    print(f"source file name: {src.name}")
    print('i\'m printed by the first_client_function')

def second_client_function(src: db_module.models.Source):
    print(f"source file name: {src.name}")
    print('i\'m printed by the second_client_function')
