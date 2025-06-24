import streamlit as st
import psycopg2
import pymongo
import redis
import os

# Connexion à Postgres
postgres_conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST", "postgres"),
    user=os.getenv("POSTGRES_USER", "user"),
    password=os.getenv("POSTGRES_PASSWORD", "password"),
    database=os.getenv("POSTGRES_DB", "real_estate")
)

# Connexion à MongoDB
mongo_client = pymongo.MongoClient(
    host=os.getenv("MONGO_HOST", "mongodb"),
    username=os.getenv("MONGO_USER", "admin"),
    password=os.getenv("MONGO_PASSWORD", "password")
)
mongo_db = mongo_client["your_database_name"]

# Connexion à Redis
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    password=os.getenv("REDIS_PASSWORD", "password"),
    decode_responses=True
)

# Exemple d'utilisation dans Streamlit
st.title("Application de Visualisation")
st.write("Connexion réussie à Postgres, MongoDB et Redis !")

# Exemple de requête Postgres
cursor = postgres_conn.cursor()
cursor.execute("SELECT version();")
st.write("Version Postgres :", cursor.fetchone())
cursor.close()

# Exemple d'accès MongoDB
st.write("Collections MongoDB :", mongo_db.list_collection_names())

# Exemple d'accès Redis
redis_client.set("test_key", "test_value")
st.write("Valeur Redis pour test_key :", redis_client.get("test_key"))

# Fermer les connexions
postgres_conn.close()
mongo_client.close()
redis_client.close()