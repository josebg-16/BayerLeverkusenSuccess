import pandas as pd

#Shooting Stats
shooting_stats=pd.read_html("https://fbref.com/en/comps/20/2023-2024/2023-2024-Bundesliga-Stats#coverage",attrs={"id":"stats_squads_shooting_for"})[0]
shooting_stats.columns = shooting_stats.columns.droplevel(0)
shooting_stats['Sh/Gls']=round(shooting_stats['Sh']/shooting_stats['Gls'],2)
shooting_stats_selected= shooting_stats[['Squad','G-xG','Sh/Gls']]

#Passing Data
passes_data=pd.read_html("https://fbref.com/en/comps/20/2023-2024/2023-2024-Bundesliga-Stats#coverage",attrs={"id":"stats_squads_possession_for"})[0]
passes_data.columns = passes_data.columns.droplevel(0)
passes_data['PrgCom/90']=passes_data['PrgR']/(passes_data['90s'])
passes_data['PasLastThird/90']=passes_data['Att 3rd']/(passes_data['90s'])

#GK Data
goalkeepers_stats=pd.read_html("https://fbref.com/en/comps/20/2023-2024/2023-2024-Bundesliga-Stats#coverage",attrs={"id":"stats_squads_keeper_for"})[0]
goalkeepers_stats.columns = goalkeepers_stats.columns.droplevel(0)
goalkeepers_stats = goalkeepers_stats.loc[:, ~goalkeepers_stats.columns.duplicated()]
goalkeepers_stats_selected=goalkeepers_stats[['Squad','Save%']]

#Defensive Data

misc_data=pd.read_html("https://fbref.com/en/comps/20/2023-2024/2023-2024-Bundesliga-Stats#coverage",attrs={"id":"stats_squads_misc_for"})[0]
misc_data.columns = misc_data.columns.droplevel(0)
defensive_data=misc_data[['Squad','PKcon','Recov']]
shooting_against=pd.read_html("https://fbref.com/en/comps/20/2023-2024/2023-2024-Bundesliga-Stats#coverage",attrs={"id":"stats_squads_gca_against"})[0]
shooting_against.columns = shooting_against.columns.droplevel(0)
shooting_against['Squad'] = shooting_against['Squad'].str.replace('vs ', '', regex=False)

shooting_stats_against=pd.read_html("https://fbref.com/en/comps/20/2023-2024/2023-2024-Bundesliga-Stats#coverage",attrs={"id":"stats_squads_shooting_against"})[0]
shooting_stats_against.columns = shooting_stats_against.columns.droplevel(0)

defensive_data['A_SCA90']=shooting_against['SCA90']
defensive_data['A_xG']=shooting_stats_against['xG']

#Merging All

final_data=pd.merge(shooting_stats_selected,goalkeepers_stats_selected,on='Squad')
final_data=pd.merge(final_data,defensive_data,on='Squad')
final_data=pd.merge(final_data,passes_data,on='Squad')

current_directory = os.getcwd()
csv_file_path = os.path.join(current_directory, "data.csv")
final_data.to_csv(csv_file_path)

