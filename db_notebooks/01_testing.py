# Databricks notebook source
import sys

sys.path.append('/Workspace/Repos/db_repo/db/')
# COMMAND ----------
import db_module.models
import db_module.utils

]
# COMMAND ----------
for client in clients:
    print(client.name)
