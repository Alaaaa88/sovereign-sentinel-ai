from neo4j import GraphDatabase

class GraphConnector:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_node(self, node_type, properties):
        with self.driver.session() as session:
            session.execute_write(self._create_and_return, node_type, properties)

    @staticmethod
    def _create_and_return(tx, node_type, props):
        query = f"CREATE (n:{node_type} $props) RETURN n"
        tx.run(query, props=props)
