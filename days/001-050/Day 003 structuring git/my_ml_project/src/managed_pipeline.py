from pathlib import Path
import logging

#managed pipeline class
class ManagedPipeline:


    def __init__(self, filepath, mode):
        self.filepath= filepath
        self.mode=mode
        self.file=None

        logging.basicConfig(level=logging.INFO)
        self.logger=logging.getLogger("managed_pipeline")

    #enter method to open the file

    def __enter__(self):

        logging.info(f"Opneing the file {self.filepath}")

        self.file=open(self.filepath,self.mode)

        return self.file

    #exit method to close the file

    def __exit__(self,exc_value,exc_type,traceback):

        

        if exc_type:
            self.logger.error(f"error occured: {exc_value}")

        if self.file:
            self.file.close()
            self.logger.info(f"closed the file {self.filepath}")

            #false means that we want to propagate the exception if it occurred, true means we want to suppress it
        return False


#secure pipeline

class Securepipeline:

    def __init__(self,input_dir):
        self.input_path=Path(input_dir)

        logging.basicConfig(level=logging.INFO)
        self.logger=logging.getLogger("secure_pipeline")

    #proccess the file securely

    def process(self,filename):

        fullpath=self.input_path/filename

        if not fullpath.exists():
            self.logger.error(f"file {fullpath} does not exist.")
            
            return
        
    #safe file handling

        with ManagedPipeline(fullpath,"r") as f:
            for line in f:
                cleaned_line=line.strip()
                self.logger.info(f"processed line: {cleaned_line}")

                #stimulate an error for demonstration
                if "error "  in cleaned_line:
                    raise ValueError("simulated error in processing line")
                

if __name__=="__main__":
    pipeline=Securepipeline(input_dir="data/raw")
    pipeline.process("data.csv")
        
    
