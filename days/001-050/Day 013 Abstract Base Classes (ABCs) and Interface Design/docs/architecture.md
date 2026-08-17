# System Architecture (Compliance-Aware)

## Intended Purpose
This document describes the modular architecture used to support technical documentation obligations for high-risk AI workflows.

## Input Data Requirements
The preprocessing pipeline expects tabular CSV input with the columns:
- id
- feature_1
- feature_2

## Module Design
- DataExtractor: loads raw records from source files.
- DataCleaner: validates required fields, normalizes types, removes invalid records.
- DataSink: stores cleaned records in an auditable format.
- DataDocumenter: writes a cleansing report for compliance traceability.
- CompliancePipeline: orchestrates components through interface-based dependency injection.

## Loose Coupling Decision
The pipeline depends on abstract interfaces, not concrete classes. This supports modular architecture and easier replacement of components without changing orchestration code.

## Compliance Evidence Produced
- Cleaned dataset artifact (JSON)
- Data cleansing report (Markdown)
