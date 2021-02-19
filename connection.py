from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_configuration = {
    'secure_connect_bundle': 'secure-connect-elko.zip'
}
auth_provider = PlainTextAuthProvider('elko','elkoelko')

# cluster = Cluster(['192.168.0.1', '192.168.0.2'], port=..., ssl_context=...)
cluster = Cluster(cloud=cloud_configuration, auth_provider= auth_provider)
session = cluster.connect()

data = session.execute("select release_version from system.local").one()
print(data[0])







