"""Pipeline orchestration for compliance-aware preprocessing."""

from pathlib import Path

from .interfaces import DataCleaner, DataDocumenter, DataExtractor, DataSink


class CompliancePipeline:
    """Coordinate extraction, cleansing, storage, and reporting modules.

    Intended purpose:
    Keep pipeline orchestration loosely coupled by depending only on interfaces.

    Input data requirements:
    - input_path must point to a supported raw data file.
    - output_path and report_path must be writable targets.
    """

    def __init__(
        self,
        extractor: DataExtractor,
        cleaner: DataCleaner,
        sink: DataSink,
        documenter: DataDocumenter,
    ) -> None:
        """Configure the pipeline with modular components.

        Intended purpose:
        Enable interchangeable implementations while preserving a stable flow.

        Input data requirements:
        - Each component must implement its respective abstract interface.
        - Components must be ready for synchronous local execution.
        """
        self.extractor = extractor
        self.cleaner = cleaner
        self.sink = sink
        self.documenter = documenter

    def run(self, input_path: Path, output_path: Path, report_path: Path) -> dict[str, int]:
        """Execute the full preprocessing flow.

        Intended purpose:
        Produce cleansed output plus a documentation artifact in one run.

        Input data requirements:
        - input_path must reference a valid raw data source.
        - output_path and report_path directories must be creatable.
        """
        records = self.extractor.extract(input_path)
        cleaned_records, stats = self.cleaner.clean(records)
        self.sink.save(cleaned_records, output_path)
        self.documenter.write_report(stats, report_path)
        return stats
