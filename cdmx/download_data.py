import polars as pl
import requests
from pathlib import Path

def download_incidence():
    # script folder
    SCRIPT_DIR = Path(__file__).resolve().parent
    # script-based routes
    csv_path = SCRIPT_DIR / "data" / "raw_fgj_files.csv"
    parquet_path = SCRIPT_DIR / "data" / "fgj_files.parquet"
    # Create folder
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    #url = "https://repodatos.atdt.gob.mx/api_update/sesnsp/incidencia_delictiva/IDM_NM_dic25.csv"
    url = "https://archivo.datos.cdmx.gob.mx/FGJ/carpetas/carpetasFGJ_acumulado_2025_01.csv"
    print("Downloading ...")
    res = requests.get(url)
    res.raise_for_status()
    
    with open(csv_path, "wb") as f:
        f.write(res.content)
    
    # save as parquet
    df = pl.read_csv(csv_path, encoding="latin-1")
    df.write_parquet(parquet_path)
    print(f"✅ Processed file saved at: {parquet_path}")

    # remove csv file to keep parquet only
    csv_path.unlink(missing_ok=True)
    print("✅ Removed csv file")

if __name__ == "__main__":
    download_incidence()
