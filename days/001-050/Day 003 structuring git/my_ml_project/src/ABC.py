from abc import ABC , abstractmethod
from pathlib import Path
import logging

class BasePipeline(ABC):
    """Base class for file pipelines.

    Intended purpose: define the shared contract for extract, transform, and
    load steps across pipeline implementations.

    Input data requirements: subclasses must accept an input directory and an
    output directory, and the input directory should contain the file selected
    by ``filename`` when ``run`` is called.
    """

    def __init__(self,input_dir,output_dir):
        """Initialize pipeline paths and logger.

        Intended purpose: prepare the input and output locations used by the
        pipeline and configure logging for pipeline activity.

        Input data requirements: ``input_dir`` and ``output_dir`` must be valid
        path-like values that can be resolved by :class:`pathlib.Path`.
        """
        self.input_path=Path(input_dir)
        self.output_path=Path(output_dir)
        self.output_path.mkdir(parents=True,exist_ok=True)
        logging.basicConfig(level=logging.INFO)
        self.logger=logging.getLogger(__name__)

    @abstractmethod
    def extract(self,filename):
        """Read raw input data for the requested file.

        Intended purpose: load the source file into memory so downstream
        transformation can operate on it.

        Input data requirements: ``filename`` must identify a file inside the
        configured input directory.
        """
        pass

    @abstractmethod
    def transform(self,data):
        """Clean or reshape extracted data.

        Intended purpose: convert raw input data into the normalized form that
        should be written to the output file.

        Input data requirements: ``data`` must contain the records returned by
        ``extract``.
        """
        pass

    @abstractmethod
    def load(self,data,filename):
        """Persist transformed data to the output location.

        Intended purpose: write the processed content to disk under a derived
        output filename.

        Input data requirements: ``data`` must already be transformed, and
        ``filename`` must be suitable for deriving the output name.
        """
        pass

    def run(self,filename):
        """Execute the full pipeline for one input file.

        Intended purpose: coordinate extraction, transformation, and loading
        for a single source file.

        Input data requirements: ``filename`` must refer to an existing file in
        the configured input directory.
        """

        self.logger.info(f"starting pipeline for {filename}")
        data=self.extract(filename)
        transformed_data=self.transform(data)
        self.load(transformed_data,filename)
        self.logger.info(f"finished pipeline for {filename}")

class CSVPipeline(BasePipeline):
    """CSV pipeline implementation.

    Intended purpose: read plain-text CSV-style input, normalize each line, and
    save the cleaned result.

    Input data requirements: source files must exist in the input directory and
    contain line-based text data suitable for stripping and uppercasing.
    """

    def extract(self,filename):
        """Read the raw file contents from the input directory.

        Intended purpose: fetch the file contents as a list of lines for later
        cleaning.

        Input data requirements: ``filename`` must point to a file inside the
        configured input directory.
        """

        full_path=self.input_path/filename
        if not full_path.exists():
            self.logger.error(f"file {full_path} does not exist.")
            return []

        with open(full_path,"r") as f:
            data=f.readlines()

        return data
    
    def transform(self,data):
        """Normalize each input line.

        Intended purpose: remove surrounding whitespace and convert each line
        to uppercase so downstream output is standardized.

        Input data requirements: ``data`` must be an iterable of text lines.
        """

        cleaned=[]

        for line in data:
            cleaned_line=line.strip().upper()
            cleaned.append(cleaned_line)

        return cleaned
    
    def load(self,data,filename):
        """Write the cleaned lines to the output directory.

        Intended purpose: persist the transformed data under a ``cleaned_``
        prefixed filename.

        Input data requirements: ``data`` must be an iterable of strings, and
        ``filename`` must be suitable for building the output path.
        """
        output_file=self.output_path/f"cleaned_{filename}"

        with open(output_file,"w") as f:
            for line in data:
                f.write(line+"\n")
        self.logger.info(f"saved cleaned data to {output_file}")


if __name__=="__main__":
    pipeline=CSVPipeline(input_dir="data/raw",output_dir="data/processed")
    pipeline.run("data.csv")
       
       
   

