import os
import pandas as pd

path = "/home/pranith/Desktop/Development/Player_Performance_Prediction"
check1_path = os.path.join(path, "CHECK1")
check2_path = os.path.join(path, "CHECK2")
check3_path = os.path.join(path, "CHECK3")
output_path = os.path.join(path, "CHECK")

for filename in os.listdir(check1_path):
    if filename.endswith(".csv"):
        file_id = filename.split(".")[0]
        data = pd.read_csv(os.path.join(check3_path, filename))
        df = data.copy()
        df = df.rename(columns={'0': 'Strike_Rate'})

        data1 = pd.read_csv(os.path.join(check1_path, filename))
        df1 = pd.read_csv(os.path.join(check2_path, filename))
        df1['strike_rate'] = df['Strike_Rate']
        df1['bowler'] = data1['bowler']
        df1['type'] = data1['Type']
        df1.to_csv(os.path.join(output_path, f"{file_id}_v1.csv"), index=False)
