"""Concrete compliance-oriented extraction, cleaning, and reporting classes."""

import csv
import json
from pathlib import Path
from typing import Any

from .interfaces import DataCleaner, DataDocumenter, DataExtractor, DataSink


class CSVExtractor(DataExtractor):
    """Extract records from CSV files.

    Intended purpose:
    Convert CSV rows into dictionaries for downstream cleansing and validation.

    Input data requirements:
    - CSV file must include a header row.
    - Columns should use stable names expected by the cleaner.
    """

    def extract(self, source_path: Path) -> list[dict[str, str]]:
        """Read all CSV rows into a list of dictionaries.

        Intended purpose:
        Standardize loaded raw data into a common in-memory representation.

        Input data requirements:
        - source_path must exist and be a readable CSV file.
        - The file should be UTF-8 encoded text.
        """
        if not source_path.exists():
            return []

        with source_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            return [dict(row) for row in reader]


class ComplianceDataCleaner(DataCleaner):
    """Apply deterministic data-cleansing rules for compliance records.

    Intended purpose:
    Normalize values, remove records missing required fields, and convert
    numeric features to float values.

    Input data requirements:
    - records must include keys listed in required_fields.
    - feature_1 and feature_2 values should be numeric strings.
    """

    def __init__(self, required_fields: tuple[str, ...]) -> None:
        """Store required fields for validation.

        Intended purpose:
        Configure rule-based validation criteria for all records.

        Input data requirements:
        - required_fields must include at least one field name.
        - Field names must match CSV header values.
        """
        self.required_fields = required_fields

    def clean(self, records: list[dict[str, str]]) -> tuple[list[dict[str, Any]], dict[str, int]]:
        """Validate, normalize, and filter records.

        Intended purpose:
        Produce high-quality records and metrics needed for compliance reports.

        Input data requirements:
        - records must be list entries from the extraction stage.
        - Required fields and numeric feature fields must be present when valid.
        """
        cleaned: list[dict[str, Any]] = []
        removed_count = 0

        for record in records:
            if not self._has_required_fields(record):
                removed_count += 1
                continue

            try:
                normalized = {
                    "id": str(record["id"]).strip(),
                    "feature_1": float(str(record["feature_1"]).strip()),
                    "feature_2": float(str(record["feature_2"]).strip()),
                }
            except (ValueError, TypeError, KeyError):
                removed_count += 1
                continue

            cleaned.append(normalized)

        stats = {
            "input_count": len(records),
            "cleaned_count": len(cleaned),
            "removed_count": removed_count,
        }
        return cleaned, stats

    def _has_required_fields(self, record: dict[str, str]) -> bool:
        """Check whether all required fields are present and non-empty.

        Intended purpose:
        Keep validation logic reusable and testable.

        Input data requirements:
        - record must be a dictionary with string keys.
        - required fields must be configured on initialization.
        """
        for field in self.required_fields:
            value = record.get(field)
            if value is None or str(value).strip() == "":
                return False
        return True


class JSONSink(DataSink):
    """Store cleansed records as JSON output.

    Intended purpose:
    Persist normalized records in an auditable and portable format.

    Input data requirements:
    - records must be JSON-serializable dictionaries.
    - output_path must point to a file location.
    """

    def save(self, records: list[dict[str, Any]], output_path: Path) -> None:
        """Write records to a JSON file.

        Intended purpose:
        Create a deterministic output artifact for downstream systems.

        Input data requirements:
        - records must contain primitive JSON-safe values.
        - output_path parent directory must be writable.
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as handle:
            json.dump(records, handle, indent=2)


class MarkdownComplianceDocumenter(DataDocumenter):
    """Write markdown documentation for cleansing statistics.

    Intended purpose:
    Generate concise technical evidence of preprocessing behavior.

    Input data requirements:
    - stats must provide integer values for standard counter keys.
    - report_path must be a markdown file location.
    """

    def write_report(self, stats: dict[str, int], report_path: Path) -> None:
        """Persist cleansing statistics in markdown format.

        Intended purpose:
        Provide a shareable artifact for compliance and audit discussions.

        Input data requirements:
        - stats keys must include input_count, cleaned_count, removed_count.
        - report_path parent directory must be writable.
        """
        report_path.parent.mkdir(parents=True, exist_ok=True)
        content = (
            "# Data Cleansing Report\n\n"
            "## Intended Purpose\n"
            "This report documents preprocessing steps and outcomes for compliance evidence.\n\n"
            "## Input Data Requirements\n"
            "Input dataset must include id, feature_1, and feature_2 columns in CSV format.\n\n"
            "## Results\n"
            f"- input_count: {stats.get('input_count', 0)}\n"
            f"- cleaned_count: {stats.get('cleaned_count', 0)}\n"
            f"- removed_count: {stats.get('removed_count', 0)}\n"
        )
        report_path.write_text(content, encoding="utf-8")
