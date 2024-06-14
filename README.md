def extract_column_paths(schema, parent_path=""):
    """
    Recursively extract column paths from a DataFrame schema, focusing only on paths that lead to actual data fields,
    and skipping intermediate structural paths unless they contain data themselves.
    :param schema: StructType, the schema of the DataFrame.
    :param parent_path: str, the path prefix for nested structures.
    :return: list of full column paths suitable for DataFrame operations where actual data is stored.
    """
    column_paths = []
    for field in schema.fields:
        current_path = f"{parent_path}.{field.name}" if parent_path else field.name
        if isinstance(field.dataType, StructType):
            # Only add current path if it has simple types directly under it, otherwise recurse
            nested_paths = extract_column_paths(field.dataType, current_path)
            if nested_paths:  # Only add if there are leaf nodes deeper in the hierarchy
                column_paths.extend(nested_paths)
        elif isinstance(field.dataType, ArrayType):
            if isinstance(field.dataType.elementType, StructType):
                nested_paths = extract_column_paths(field.dataType.elementType, current_path)
                if nested_paths:
                    column_paths.extend(nested_paths)
            else:
                column_paths.append(current_path)
        else:
            column_paths.append(current_path)
    return column_paths

