import logging


logging.basicConfig(
    level=logging.INFO,
    filename="data.log",
    format="%(asctime)s-%(message)s-%(levelname)s"
)

class DataCleaner:
    def load_csv(self,path:str):
        try:

            logging.info("Loading CSV file from path: %s", path)
            with open (path,"r") as f :
                data=f.read()
            return data
    
        except FileNotFoundError:
            logging.error(f" Critical :file not found at path {path}")

        except Exception as e:
            logging.warning(f"An unexpected error occurred while loading the CSV file: {e}")
            return None

data=DataCleaner()
data.load_csv("data.csv")
