import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys

def setup_logging(app_name: str, log_level: str = "INFO"):
    """
    Args:
        app_name: nome para arquivo do log
        log_level: Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Converter string de nível para objeto logging
    level = getattr(logging, log_level.upper(), logging.INFO)
    
    # Criar diretório se não existir
    log_dir = Path(__file__).parent.parent.parent.parent/'logs'
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    handlers = []
    
    # saída padrão
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    handlers.append(console_handler)
    
    # Tamanho maximo do arquivo (10MB)
    rotating_handler = RotatingFileHandler(
        filename=Path(log_dir) / f"{app_name}.log",
        maxBytes=10*1024*1024,
        backupCount=5,
        encoding='utf-8'
    )
    rotating_handler.setFormatter(formatter)
    handlers.append(rotating_handler)
    
    # Configuração principal
    logging.basicConfig(
        level=level,
        handlers=handlers
    )