from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['cassandra-db'])  # Use the container name
session = cluster.connect()

# Create or connect to keyspace and table
KEYSPACE = "user_data_keyspace"
TABLE = "users"

# Ensure keyspace and table exist
session.execute(f"""
    CREATE KEYSPACE IF NOT EXISTS {KEYSPACE} 
    WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}}
""")
session.set_keyspace(KEYSPACE)
session.execute(f"""
    CREATE TABLE IF NOT EXISTS {TABLE} (
        id UUID PRIMARY KEY,
        name text,
        email text
    )
""")
