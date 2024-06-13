# Project Documentation

## Overview
This project involves dynamically generating PySpark schemas from JSON schemas and using these schemas to process JSON data in PySpark. The process includes reading JSON schemas, converting them into PySpark schemas, generating a PySpark script automatically from these schemas, and executing data transformations.

## Files and Components

### JSON Schema File (`schema.json`)
- **Purpose**: Defines the structure of JSON data.
- **Location**: Specified in the configuration file.

### Configuration File (`config.yaml`)
- **Purpose**: Stores paths and configurations like the path to the JSON schema, the output paths for the PySpark script, and the PySpark schema file.
- **Contents**:
  ```yaml
  json_schema_path: 'path/to/schema.json'
  pyspark_script_output_path: 'path/to/output_script.py'
  pyspark_schema_path: 'path/to/schema_module.py'
  json_data_input_path: 'path/to/input_data.json'

  Python Utility Scripts
schema_generator.py:

Purpose: Contains functions to read the JSON schema, resolve references, convert it to a PySpark schema, and generate a Python module that includes this schema.
Functions:
read_json_file(file_path): Reads a JSON file and returns its content.
resolve_reference(ref, definitions): Resolves $ref in JSON schemas.
convert_to_spark_schema(json_schema, definitions): Converts JSON schema to PySpark StructType.
generate_pyspark_schema(schema_dict): Processes the schema dictionary and handles definitions.
generate_schema_file(schema, schema_file_path): Generates a Python file from a PySpark schema for import in other scripts.
data_processing.py:

Purpose: Uses the generated PySpark schema to load JSON data into a DataFrame, performs transformations, and outputs the results.
Functions:
extract_column_paths(schema, parent_path): Extracts column paths from a PySpark schema for data selection.
flatten(df): Flattens nested structures in a DataFrame.
generate_select_expression(df): Generates a select expression for DataFrame columns with proper aliasing.
generate_select_expression_from_list(column_names): Similar to generate_select_expression but takes a list of column names directly.
Generated PySpark Script (output_script.py)
Purpose: Automatically generated script that reads data using the schema, applies transformations, and displays the results.

from pyspark.sql import SparkSession
from schema_module import get_schema  # Imports the generated schema
from pyspark.sql.functions import col, explode_outer

spark = SparkSession.builder.appName("JsonToDataFrame").getOrCreate()
schema = get_schema()
df = spark.read.schema(schema).json("path/to/input.json")
df.select(...).show()

