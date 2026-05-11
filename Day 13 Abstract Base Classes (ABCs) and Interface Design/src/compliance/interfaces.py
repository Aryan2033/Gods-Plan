"""Abstract interfaces for a compliance-aware data processing pipeline."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class DataExtractor(ABC):
    """Define how raw records are loaded from a source.

    Intended purpose:
    Provide a standard extraction contract so pipeline orchestration can remain
    independent from file format details.

    Input data requirements:
    - source_path must point to an existing readable file.
    - The file format must match the concrete extractor implementation.
    """

    @abstractmethod
    def extract(self, source_path: Path) -> list[dict[str, str]]:
        """Load records from a source file.

        Intended purpose:
        Return raw records in a normalized list-of-dictionaries shape.

        Input data requirements:
        - source_path must be a valid file path.
        - The source file must contain parseable structured data.
        """


class DataCleaner(ABC):
    """Define how records are validated and cleansed.

    Intended purpose:
    Apply deterministic rules for removing invalid data and normalizing values.

    Input data requirements:
    - records must be a list of dictionaries with string keys.
    - Required fields must be present according to implementation rules.
    """

    @abstractmethod
    def clean(self, records: list[dict[str, str]]) -> tuple[list[dict[str, Any]], dict[str, int]]:
        """Clean records and return metrics about removed records.

        Intended purpose:
        Separate valid, normalized data from invalid data while capturing counts
        needed for technical documentation.

        Input data requirements:
        - records must be loaded records from the extraction stage.
        - Fields used for validation must be accessible by key.
        """


class DataSink(ABC):
    """Define how cleansed records are stored.

    Intended purpose:
    Provide a pluggable output mechanism without coupling pipeline logic to one
    storage implementation.

    Input data requirements:
    - records must already be validated and normalized.
    - output_path must be writable.
    """

    @abstractmethod
    def save(self, records: list[dict[str, Any]], output_path: Path) -> None:
        """Persist cleansed records to an output target.

        Intended purpose:
        Materialize cleansed records for downstream model development or audit.

        Input data requirements:
        - records must be JSON-serializable for JSON implementations.
        - output_path parent directory must be creatable.
        """


class DataDocumenter(ABC):
    """Define how data-cleansing steps are documented.

    Intended purpose:
    Generate technical traceability artifacts required for compliance evidence.

    Input data requirements:
    - stats must include integer counters for records processed and removed.
    - report_path must be writable.
    """

    @abstractmethod
    def write_report(self, stats: dict[str, int], report_path: Path) -> None:
        """Write a human-readable cleansing report.

        Intended purpose:
        Capture data quality actions and outcomes in a reproducible document.

        Input data requirements:
        - stats must contain input_count, cleaned_count, and removed_count keys.
        - report_path parent directory must be creatable.
        """
