#!/bin/bash

# Neo4j Config:
#   NEO4J_kafka_group_id: neo4j_local
#   NEO4J_streams_sink_topic_cypher_test: "MERGE (n:Test {id: coalesce(event.id,'NOID')}) SET n += event, n.lastUpdate=datetime()"
#   NEO4J_streams_sink_topic_cypher_product: "MERGE (n:Product {id: coalesce(event.id,'NOID')}) SET n += event, n.lastUpdate=datetime()"
#   NEO4J_streams_sink_topic_cypher_customer: "MERGE (n:Customer {id: coalesce(event.id,'NOID')}) SET n += event, n.lastUpdate=datetime()"
#   NEO4J_streams_sink_topic_cypher_account: "MERGE (n:Account {id: coalesce(event.id,'NOID')}) SET n += event, n.lastUpdate=datetime()"
#   NEO4J_streams_sink_topic_cypher_purchase:
#     "MERGE (product:Product { id: event.product_id })
#      MERGE (company:Company { id: event.company_id })
#      MERGE (customer:Customer { id: event.customer_id })
#      CREATE (purchase:Purchase { id: event.id })
#      SET purchase += event
#      CREATE (purchase)<-[:MADE]-(customer)
#      CREATE (purchase)<-[:SOLD]-(company)
#      CREATE (purchase)<-[:ITEM]-(product)"          
#   NEO4J_streams_sink_enabled: "true"
#   NEO4J_streams_procedures_enabled: "true"
#   NEO4J_streams_source_enabled: "false"
#   NEO4J_streams_source_enable: "false"

# 5 minutes
TIME_MS=300000
# 10 seconds
# TIME_MS=10000

# CUSTOMERS
pipenv run python3 fake.py \
    --topic customer \
    --type customer \
    --mps 5 \
    --ms $TIME_MS >customers.log 2>&1 & 
# BANKS
pipenv run python3 fake.py \
    --topic bank \
    --type bank \
    --mps 5 \
    --ms $TIME_MS >banks.log 2>&1 &
# ACCOUNTS
pipenv run python3 fake.py \
    --topic account \
    --mps 5 \
    --type account \
    --ms $TIME_MS >products.log 2>&1 &
# TRANSFERS
pipenv run python3 fake.py \
    --topic accounttransfer \
    --type accounttransfer \
    --mps 15 \
    --ms $TIME_MS >accounttransfer.log 2>&1 & 
