# Databricks notebook source
import sys

sys.path.append('/Workspace/Repos/db_repo/db/')
# COMMAND ----------
import db_module.processing
import db_module.utils


def first_client_function(src: db_module.processing.Source):
    print(f"source file name: {src.name}")
    print('xxx')

def second_client_function(src: db_module.processing.Source):
    print(f"source file name: {src.name}")
    print('yyy')


first_client = db_module.processing.Client('Stefan', 
                    [
                        db_module.processing.Process(
                            [
                                db_module.processing.Stage('ingest', 
                                    [
                                        db_module.processing.Activity(
                                                'read_first_file', 
                                                db_module.processing.Source('iris','csv','https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'), 
                                                first_client_function)
                                    ])
                            ])
                    ]
                
            )



# COMMAND ----------
