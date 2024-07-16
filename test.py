import streamlit as st
import pandas as pd

df=pd.read_csv("D:\IPL_streamlit_analysis\IPL_Dataset/deliveries.csv")
df1=pd.read_csv("D:\IPL_streamlit_analysis\IPL_Dataset/ipl.csv")
ipl=df.merge(df1,left_on='match_id',right_on='id')
ipl.head()


def batsman_record(batsman):
    name=ipl[ipl['batsman']==batsman]
    #st.subheader(batsman+"-"+"record against each teams")
    player=name.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).reset_index()
    b_four=ipl[(ipl['batsman_runs']==4) & (ipl['batsman']==batsman)]
    player['No_Of_fours']=b_four.groupby('bowling_team')['batsman_runs'].count().sort_values(ascending=False).reset_index()['batsman_runs']
    b_six=ipl[(ipl['batsman_runs']==6) & (ipl['batsman']==batsman)]
    player['NO_Of_sixes']=b_six.groupby('bowling_team')['batsman_runs'].count().sort_values(ascending=False).reset_index()['batsman_runs']
    name=ipl[ipl['batsman']==batsman]
    player['ball_played']=name.groupby('bowling_team')['ball'].count().reset_index()['ball']
    player['Strike_rate']=player['batsman_runs']/player['ball_played']*100
    return player

def batsman_list()
team=ipl.groupby('batting_team')
player=list(team.get_group('Royal Challengers Bangalore')['batsman'].unique())

st.header("IPL Players")
name=st.selectbox("Select player",player)
print()
st.header(name+"-"+"Record against each team")
x=batsman_record(name)
#print(x)
st.write(x)


if __name__=='__main__':
    record=batsman_record('RG Sharma')
    


