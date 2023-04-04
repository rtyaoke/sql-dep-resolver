import os
from collections import defaultdict

from sql_metadata import Parser


def extract_dependencies(file_path):
    dependencies = []

    with open(file_path, 'r') as file:
        content = file.read()
        parsed_sql = Parser(content)
        dependencies = [table.split(".")[-1] for table in parsed_sql.tables]

    return set(dependencies)


def build_dependency_graph(path):
    graph = defaultdict(list)
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.sql'):
                file_path = os.path.join(root, file)
                dependencies = extract_dependencies(file_path)
                graph[file.split('.')[0]].extend(
                    [dep for dep in dependencies if dep + '.sql' in files])
    return graph


def find_execution_order(graph):
    execution_order = []
    visited = set()

    def visit(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                visit(neighbor)
            execution_order.append(node)

    for node in graph:
        visit(node)

    return execution_order


def find_specific_execution_order(graph, specific_sql):
    execution_order = []
    visited = set()

    def visit(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                visit(neighbor)
            execution_order.append(node)

    visit(specific_sql)

    return execution_order


if __name__ == "__main__":
    path = "sql"  # SQLファイルが格納されているディレクトリを指定してください。
    dependency_graph = build_dependency_graph(path)
    # execution_order = find_execution_order(dependency_graph)
    execution_order = find_specific_execution_order(dependency_graph, 'e')
    print("Execution order:", execution_order)
