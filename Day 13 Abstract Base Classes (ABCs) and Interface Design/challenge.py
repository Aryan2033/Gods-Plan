"""Compliance-focused entrypoint for the modular data pipeline demo.

Intended purpose:
Run a small, documentation-first pipeline that demonstrates modular architecture
for EU AI Act style technical documentation preparation.

Input data requirements:
- Expects a CSV file at data/raw/compliance_input.csv.
- CSV must include a header row with at least: id, feature_1, feature_2.
"""

from pathlib import Path

from src.compliance.cleaning import (
    CSVExtractor,
    ComplianceDataCleaner,
    JSONSink,
    MarkdownComplianceDocumenter,
)
from src.compliance.pipeline import CompliancePipeline


def main() -> None:
    """Run the compliance pipeline and print output locations.

    Intended purpose:
    Provide one command entrypoint to execute extraction, cleansing,
    storage, and reporting.

    Input data requirements:
    - Uses fixed workspace-relative paths.
    - Requires read access to the input CSV and write access to output folders.
    """
    input_path = Path("data/raw/compliance_input.csv")
    output_path = Path("data/processed/compliance/cleaned_records.json")
    report_path = Path("docs/generated/data-cleansing-report.md")

    pipeline = CompliancePipeline(
        extractor=CSVExtractor(),
        cleaner=ComplianceDataCleaner(required_fields=("id", "feature_1", "feature_2")),
        sink=JSONSink(),
        documenter=MarkdownComplianceDocumenter(),
    )
    result = pipeline.run(input_path=input_path, output_path=output_path, report_path=report_path)

    print("Compliance pipeline completed.")
    print(f"Input records: {result['input_count']}")
    print(f"Cleaned records: {result['cleaned_count']}")
    print(f"Output JSON: {output_path}")
    print(f"Report Markdown: {report_path}")


if __name__ == "__main__":
    main()
