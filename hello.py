import pandas as pd
data = pd.read_csv("/workspace/Player_Performance_Prediction/Demo/335982.csv")

df = data.copy()
df_details = data[data["player_dismissed"].notnull()]
df_details.loc[df["player_dismissed"].notnull(), "player_name"] = df["player_dismissed"]
df_ = df_details[['player_name','bowler','wicket_type']].copy()

df['out'] = df["player_dismissed"].notnull()
bowler = df[df['out'] == True]["bowler"]
dismissal_kind = df[df['out'] == True]["wicket_type"]

# # for index, row in df[df['out'] == True].iterrows():                               
# #     print(f"Batsman was dismissed by {row['bowler']} ({row['wicket_type']})")
bowler = pd.DataFrame(bowler)
bowler['Type'] = dismissal_kind
bowler['striker'] = df_['player_name']
# print(bowler)  

total_runs = pd.read_csv("/workspace/Player_Performance_Prediction/CHECK/335982.csv")

# Merge total_runs and bowler dataframes on 'striker' column
merged_df = pd.merge(total_runs, bowler, on='striker', how='outer')

# Fill missing values with 0
merged_df.fillna(0, inplace=True)

print(merged_df)


