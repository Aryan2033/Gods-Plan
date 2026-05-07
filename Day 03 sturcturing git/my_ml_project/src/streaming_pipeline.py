from pathlib import Path
import logging
import csv

class StreamingPipeline:

    def __init__(self, input_dir:str, output_dir:str):
        self.input_path = Path(input_dir)
        self.output_path = Path(output_dir)

        self.output_path.mkdir(parents=True, exist_ok=True)

        logging.basicConfig(level=logging.INFO)

        self.logger = logging.getLogger("streaming_pipeline")

    # generator function
    def process_rows(self, filename:str):
        full_path = self.input_path / filename #this will create a full path to the file we want to process

        if not full_path.exists():
            self.logger.error(f"File {full_path} does not exist.")
            return
        
        with open(full_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                # transform the row if needed
                row["name"] = row["name"].upper()
                row["salary"] = float(row["salary"]) * 1.1

                # yield the processed row for further processing or writing to output
                yield row

    def run(self, filename:str):
        self.logger.info(f"starting streaming etl for file {filename}")

        stream = self.process_rows(filename)

        for processed_row in stream:
            self.logger.info(f"processed row: {processed_row}")
            # write the processed row to output or further processing

if __name__ == "__main__":

    pipeline=StreamingPipeline(
        input_dir="data/raw", 
        output_dir="data/processed"
                                )

    pipeline.run("data.csv")






