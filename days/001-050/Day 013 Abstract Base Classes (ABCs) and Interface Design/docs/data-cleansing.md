# Data Cleansing Procedure

## Intended Purpose
Describe deterministic preprocessing behavior before model use and support compliance documentation.

## Input Data Requirements
- Format: CSV
- Encoding: UTF-8
- Required columns: id, feature_1, feature_2
- Field constraints:
  - id must be non-empty text
  - feature_1 and feature_2 must be numeric

## Cleansing Steps
1. Extract CSV rows into dictionaries.
2. Remove records with missing required fields.
3. Strip whitespace in string values.
4. Convert feature_1 and feature_2 to float.
5. Remove records failing numeric conversion.
6. Save cleaned records in JSON format.
7. Generate a markdown report with input_count, cleaned_count, removed_count.

## Documentation Rule Coverage
All classes and methods in the pipeline package include docstrings that describe:
- Intended purpose
- Input data requirements
