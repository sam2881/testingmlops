# PySpark JSON Schema Processing

## Overview

This project automates the process of converting JSON schemas into PySpark schemas and utilizes these schemas to process JSON data within PySpark. This involves reading JSON schemas, converting them into PySpark compatible formats, and dynamically generating PySpark scripts to process the data based on these schemas.

## Configuration

### `config.yaml`

This configuration file stores the paths for the JSON schema, PySpark script output, PySpark schema module, and JSON data input. Here's an example of what it might look like:

```yaml
json_schema_path: 'path/to/json_schema.json'
pyspark_script_output_path: 'path/to/generated_script.py'
pyspark_schema_path: 'path/to/generated_schema.py'
json_data_input_path: 'path/to/json_data.json'
