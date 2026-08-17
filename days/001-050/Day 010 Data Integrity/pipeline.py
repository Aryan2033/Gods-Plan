from pathlib import Path
import logging
import yaml

class DataPipeline:
    def __init__(self,input_dir:str,output_dir:str):
        self.input_path = Path(input_dir)
        self.output_path = Path(output_dir)
    
        self.output_path.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(level=logging.INFO)
        self.logger=logging.getLogger(__name__)#returns a Logger object for name


    def run(self,filename):
        self.logger.info(f"Processing file: {filename}")
        
        #1 extract data
        full_path=self.input_path/filename

        if not full_path.exists():
            self.logger.error(f"File {full_path} does not exist.")
            return
        #2 transform data
        self.logger.info(f"Transforming data from file: {filename}")

        #3 load data
        target=self.output_path/f"cleaned_{filename}"
        self.logger.info(f"Saving production ready data to: {target}")

if __name__=="__main__":
    # Load settings from config.yaml when available, otherwise use sensible defaults
    config_path = Path("config.yaml")
    config = {}
    if config_path.exists():
        with open(config_path, "r") as f:
            config = yaml.safe_load(f) or {}

    input_dir = config.get("input_dir", "data/raw")
    output_dir = config.get("output_dir", "data/processed")
    filename = config.get("filename", "data.csv")

    # prefer the configured input if it exists; otherwise fall back to known locations
    from pathlib import Path as _Path
    chosen_input = input_dir if _Path(input_dir).exists() else ("data/processed/raw" if _Path("data/processed/raw").exists() else input_dir)

    pipeline = DataPipeline(input_dir=chosen_input, output_dir=output_dir)
    pipeline.logger.info(f"Using input directory: {chosen_input}")
    pipeline.run(filename)