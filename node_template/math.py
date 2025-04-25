from pyiron_workflow import as_function_node


@as_function_node
def sum(x: float, y: float) -> float:
    result = x + y
    return result


@as_function_node
def product(x: float, y: float) -> float:
    result = x * y
    return result
