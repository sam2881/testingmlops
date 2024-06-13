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
