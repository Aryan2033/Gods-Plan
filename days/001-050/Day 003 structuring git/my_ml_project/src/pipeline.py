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
    # choose input directory: prefer original 'data/raw', fallback to generated 'data/processed/raw'
    from pathlib import Path as _Path
    chosen_input = "data/raw" if _Path("data/raw").exists() else "data/processed/raw"
    pipeline = DataPipeline(input_dir=chosen_input, output_dir="data/processed")
    pipeline.logger.info(f"Using input directory: {chosen_input}")
    pipeline.run("data.csv")