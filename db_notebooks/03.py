# Databricks notebook source
import sys

sys.path.append('/Workspace/Repos/db_repo/db/')

# COMMAND ----------

from db_module.clients_database import clients

# COMMAND ----------

client_names = [client for client in clients.keys()]

# COMMAND ----------

dbutils.widgets.dropdown(
  name='cl',
  defaultValue=client_names[0],
  choices=client_names,
  label='Client'
)

# COMMAND ----------

selected_client = dbutils.widgets.get('cl')
print(f"selected client: {selected_client}")
for client_name, processes in clients.items():
    if selected_client == client_name:
        print(client_name)
        processes[0].stages[0].activities[0].action(processes[0].stages[0].activities[0].source)

# COMMAND ----------


