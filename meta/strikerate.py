import os
import pandas as pd

# Specify the input and output folders
input_folder = "/home/pranith/Desktop/Development/Player_Performance_Prediction/Data/csv_files"
output_folder = "/home/pranith/Desktop/Development/Player_Performance_Prediction/CHECK3"

output_file = "Sr.csv"
output_path = os.path.join("/home/pranith/Desktop/Development/Player_Performance_Prediction", output_file)

# Iterate through all files in the input folder
for file in os.listdir(input_folder):
    # Only consider CSV files
    if file.endswith(".csv"):
        # Read in the CSV file
        df = pd.read_csv(os.path.join(input_folder, file))

        # Perform some operations on the dataframe, such as filtering rows or calculating values
        data = df.copy()
        data = data.fillna(0)

        # Strike rate
        strikerate = pd.DataFrame((data.groupby(['batting_team', 'bowling_team', 'match_id', 'start_date','striker'])['runs_off_bat'].sum() / data.groupby(['batting_team', 'bowling_team', 'match_id','start_date', 'striker'])['ball'].nunique()) * 100)
        strikerate = strikerate.rename(columns={"runs_off_bat": "strike_rate"})

        # Fifties
        # fifties = pd.DataFrame(data.groupby(['batting_team', 'bowling_team', 'match_id', 'start_date','striker'])['runs_off_bat'].sum() >= 50)
        # fifties = fifties.rename(columns={"runs_off_bat": "50"})

        # # Hundreds
        # hundreds = pd.DataFrame(data.groupby(['batting_team', 'bowling_team', 'match_id','start_date', 'striker'])['runs_off_bat'].sum() >= 100)
        # hundreds = hundreds.rename(columns={"runs_off_bat": "100"})

        # # Duck
        # duck = pd.DataFrame(data.groupby(['batting_team', 'bowling_team', 'match_id','start_date', 'striker'])['runs_off_bat'].sum() == 0)
        # duck = duck.rename(columns={"runs_off_bat": "duck"})

        # df["out"] = pd.DataFrame(data.groupby(['batting_team', 'bowling_team', 'match_id','start_date', 'striker'])["player_dismissed"].notnull()
        # bowler = df[df['out'] == True]["bowler"]
        # dismissal_kind = df[df['out'] == True]["wicket_type"]

        strikerate.to_csv("Sr.csv")
        sr = pd.read_csv("/home/pranith/Desktop/Development/Player_Performance_Prediction/Sr.csv")
        # strikerate.to_csv(output_path)

        # Read in the output CSV file
        # sr = pd.read_csv(output_path)
        
        # sr['0']
        # df_details = data[data["player_dismissed"].notnull()]
        # df_details.loc[df["player_dismissed"].notnull(), "player_name"] = df["player_dismissed"]
        # df_ = df_details[['player_name','bowler','wicket_type']].copy()

        # df['out'] = df["player_dismissed"].notnull()
        # bowler = df[df['out'] == True]["bowler"]
        # dismissal_kind = df[df['out'] == True]["wicket_type"]

        # # for index, row in df[df['out'] == True].iterrows():                               
        # #     print(f"Batsman was dismissed by {row['bowler']} ({row['wicket_type']})")
        # bowler = pd.DataFrame(bowler)
        # bowler['Type'] = dismissal_kind
        # bowler['striker'] = df_['player_name']

        # total_runs['Balls'] = balls_faced
        # total_runs['Fours'] = fours
        # total_runs['Sixes'] = sixes
        # # total_runs['SR'] = sr['0']
        # total_runs['Fifties'] = fifties
        # total_runs['Hundreds'] = hundreds
        # total_runs['Duck'] = duck
        # total_runs
        merged_df = sr.copy()
        # merged_df = pd.merge(total_runs,bowler,on='striker', how='outer')

        # Fill missing values with 0
        merged_df = merged_df.fillna(0)

        # Make a copy of the dataframe
        df1 = merged_df.copy()

        # Replace boolean values with 1 or 0
        # df1['Hundreds'] = df1['Hundreds'].replace({True: 1, False: 0})
        # df1['Fifties'] = df1['Fifties'].replace({True: 1, False: 0})
        # df1['Duck'] = df1['Duck'].replace({True: 1, False: 0})
        # df1['Sixes'] = df1['Sixes'].replace({True: 1, False: 0})

        # Save the modified dataframe to a CSV file
        df1.to_csv("df.csv")

        # Read the CSV file into a new dataframe
        sample = pd.read_csv("/home/pranith/Desktop/Development/Player_Performance_Prediction/df.csv")

        # Calculate the dreamll score
        # dreamll_score = sample['Batsman_runs'] + sample['Sixes']*2 + sample['Fours'] + sample['Fifties']*8 + sample['Hundreds']*16 - sample['Duck']*2 + 4

        # Add the dreamll score to the dataframe
        # sample['dreamll_score'] = dreamll_score


        # Save the resulting dataframe to a CSV file in the output folder
        sample.to_csv(os.path.join(output_folder, file))


# Set the input and output folders
input_folder = "/home/pranith/Desktop/Development/Player_Performance_Prediction/CHECK3"
output_folder = "/home/pranith/Desktop/Development/Player_Performance_Prediction/CHECK3"

# Iterate over the files in the input folder
for file in os.listdir(input_folder):
    # Skip files that are not CSV files
    if not file.endswith(".csv"):
        continue

    # Load the Cile
    df = pd.read_csv(os.path.join(input_folder, file))

    # Drop the "Column Name" column from the DataFrame
    df = df.drop("Unnamed: 0", axis=1)

    # Save the resulting DataFrame to a CSV file in the output folder
    df.to_csv(os.path.join(output_folder, file), index=False)

# Set the input folder
# folder = "/home/pranith/Desktop/Development/Player_Performance_Prediction/CHECK3"

# Initialize an empty list to store the dataframes
# df_list = []

# # Iterate through all files in the folder
# for file in os.listdir(folder):
#     # Only consider CSV files
#     if file.endswith(".csv"):
#         # Read in the CSV file
#         df = pd.read_csv(os.path.join(folder, file))
#         if 'Unnamed: 0.1' in df.columns:
#             df = df.drop('Unnamed: 0', axis=1)
#         # Add the dataframe to the list
#         df_list.append(df)

# Concatenate all dataframes into a single dataframe
# df = pd.concat(df_list)

# Write the combined data to a new CSV file 
# df.to_csv("Batsman_stats_summary_file.csv", index=False)
# pd.options.display.max_rows = None

check = pd.read_csv("/home/pranith/Desktop/Development/Player_Performance_Prediction/CHECK3/335983.csv")
print(check)