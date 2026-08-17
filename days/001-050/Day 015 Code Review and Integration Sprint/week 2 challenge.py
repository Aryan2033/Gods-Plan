from abc import ABC, abstractmethod
import logging
import time
#interface design
class BaseProcessor(ABC):
    @abstractmethod
    def process_element(self,item:dict) -> dict:#function accept item as dict and return dict
        pass

#concrete implementation of the interface with validation logic    
class IndustrialDataProcessor(BaseProcessor):
    def process_element(self, item: dict) -> dict:
        if "value" in item and item["value"]>=0:
            item["value"] = round(item["value"]*1.19,2)
            return item
        raise ValueError(f"invalid item value {item.get('value')}")
    
#safe rsource management using context manager day 12

class OperationalSession:

    def __init__(self,session_name:str):
        self.name = session_name
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        
        self.logger=logging.getLogger(self.name)

    def __enter__(self):
        self.logger.info(f"Starting session: {self.name}")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.logger.error(f"an error occured in session {self.name}: {exc_val}")
        else:
            self.logger.info(f"Ending session: {self.name}")
        
        return False #propagate exception if any
    
#stream injestion day11

    def stream_sensor_data(self,batch_size:int):
        '''stimulate zero ram  streaming data generation'''
        for idx in range(batch_size):
            yield {"id": 1000+idx, "value": float(idx*10)}

if __name__=="__main__":

    processor=IndustrialDataProcessor()
    with OperationalSession("Industrial Data Processing") as session:
        data_stream=session.stream_sensor_data(batch_size=5)

        for raw_records in data_stream:
            try:
                processed_record=processor.process_element(raw_records)
                session.logger.info(f"processed record: {processed_record}")
            except ValueError as e:
                session.logger.warning(f"skipping record due to error: {e}")



        


    
