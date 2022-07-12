import db_module.models
import db_module.processing

clients = {'Stefan': 
                    [
                        db_module.models.Process(
                            [
                                db_module.models.Stage('ingest', 
                                    [
                                        db_module.models.Activity(
                                                'read_first_file', 
                                                db_module.models.Source(
                                                    'iris',
                                                    'csv',
                                                    'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'), 
                                                db_module.processing.first_client_function)
                                    ])
                            ])
                    ]
                
            
        , 'Bob': 
                    [
                        db_module.models.Process(
                            [
                                db_module.models.Stage('ingest', 
                                    [
                                        db_module.models.Activity(
                                                'read_first_file', 
                                                db_module.models.Source(
                                                    'movies',
                                                    'csv',
                                                    'https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv'), 
                                                db_module.processing.second_client_function)
                                    ])
                            ])
                    ]}