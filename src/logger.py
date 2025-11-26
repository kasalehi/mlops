import logging
from pathlib import Path
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir=Path(__file__).resolve().parent.parent / 'logs' 
logs_dir.mkdir(exist_ok=True)
log_path_file=logs_dir / LOG_FILE
logging.basicConfig(
    filename=log_path_file,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"  ,
    level=logging.INFO
)
