import pandas as pd
import os

os.makedirs('/workspaces/Mlops/02-Experiment_tracking/data', exist_ok=True)

files = [
    'green_tripdata_2021-01',
    'green_tripdata_2021-02',
]

for f in files:
    df = pd.read_parquet(f'/workspaces/Mlops/test/{f}.parquet')
    df.to_csv(f'/workspaces/Mlops/02-Experiment_tracking/data/{f}.csv', index=False)
    print(f'{f}.csv saved ({len(df)} rows)')