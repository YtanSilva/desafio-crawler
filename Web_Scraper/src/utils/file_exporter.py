import csv
import json
from dataclasses import asdict
from pathlib import Path
from typing import List, Literal
from models.data_models import Movie

def export_movies_to_file(
    movies: List[Movie],
    filename: str,
    file_format: Literal['csv', 'json', 'both'] = 'both'
) -> None:
    
    # procurando diretorio de destino
    output_dir = Path(__file__).parent.parent.parent/'data'/'data_files'
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Montando csv
    if file_format == 'csv' or file_format == 'both':
        csv_filepath = output_dir / f"{filename}.csv"
        try:
            with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [field.name for field in Movie.__dataclass_fields__.values()]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for movie in movies:
                    writer.writerow(asdict(movie))
            print(f"Dados exportados com sucesso para '{csv_filepath}'")
        except IOError as e:
            print(f"Erro ao escrever no arquivo CSV '{csv_filepath}': {e}")

    # Montando json
    if file_format == 'json' or file_format == 'both':
        json_filename = output_dir / f"{filename}.json"
        try:
            with open(json_filename, 'w', encoding='utf-8') as jsonfile:
                movies_data = [asdict(movie) for movie in movies]
                json.dump(movies_data, jsonfile, indent=4, ensure_ascii=False)
            print(f"Dados exportados com sucesso para '{json_filename}'")
            print(f"Dados exportados com sucesso para '{output_dir}'")
        except IOError as e:
            print(f"Erro ao escrever no arquivo JSON '{json_filename}': {e}")
