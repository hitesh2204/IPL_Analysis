import pandas as pd
import streamlit as st
from PIL import Image
#from streamlit_extras.switch_page_button import switch_page


df=pd.read_csv("D:\IPL_streamlit_analysis\IPL_Dataset/deliveries.csv")
df1=pd.read_csv("D:\IPL_streamlit_analysis\IPL_Dataset/ipl.csv")
ipl=df.merge(df1,left_on='match_id',right_on='id')
ipl.head()


#batsman=ipl.groupby('batting_team')
def IPL():
    ### reading image
    image = Image.open("D:\IPL_streamlit_analysis\image-video\IPL1-2024-Squad.jpg")
    st.title(":red[IPL]:green[-]:blue[Analysis] :sunglasses:")
    st.image(image,caption='All IPL teams-captaions')

    ## reading videos.
    video_file = open('D:\IPL_streamlit_analysis\image-video\ipl_video.mp4','rb')
    video_bytes = video_file.read()
    #video_file ='D:\IPL_streamlit_analysis\image-video\ipl_video.mp4'
    st.video(video_bytes,loop=True)
    st.balloons()

## Individual tem analysis function.    
def team_analysis(team):
    if team=='Mumbai Indians':
        st.header(team+"_"+"analysis",divider='rainbow')
        image = Image.open("D:/IPL_streamlit_analysis/image-video/mumbai_indians.jpg")
        st.image(image,caption='Mumbai che por.',width=600)
    if team=='Chennai Super Kings':
        st.header(team+"_"+"analysis",divider='rainbow')
        image = Image.open("D:/IPL_streamlit_analysis/image-video/CSK-2023-1.jpg")
        st.image(image,caption='.Chennai Boys.',width=600)
    if team=='Kolkata Knight Riders':
        st.header(team+"_"+"analysis",divider='rainbow')
        image = Image.open("D:\IPL_streamlit_analysis\image-video\kolkatta1.jpeg")
        st.image(image,caption='Karbo Ladbo Jitbo Reeeeee.',width=600)
    if team=='Sunrisers Hyderabad':
        st.header(team+"_"+"analysis",divider='rainbow')
        image = Image.open("D:/IPL_streamlit_analysis/image-video/hydrabad.jpeg")
        st.image(image,caption='Rise Up to Every Challenge',width=600)
    if team=='Royal Challengers Bangalore':
        st.header(team+"_"+"analysis",divider='rainbow')
        image = Image.open("D:/IPL_streamlit_analysis/image-video/rcb.jpeg")
        st.image(image,caption='Ee Sala Cup Namde',width=600)
    if team=='Delhi Daredevils':
        st.header(team+"_"+"analysis",divider='rainbow')
        image = Image.open("D:\IPL_streamlit_analysis\image-video\delhi1.jpeg")
        st.image(image,caption='This is New Delhi',width=600)
    if team=='Kings XI Punjab':
        st.header(team+"_"+"analysis",divider='rainbow')
        image = Image.open("D:/IPL_streamlit_analysis/image-video/punjab.jpeg")
        st.image(image,caption='This is New Delhi',width=600)
    if team=='Rajasthan Royals':
        st.header(team+"_"+"analysis",divider='rainbow')
        image = Image.open("D:/IPL_streamlit_analysis/image-video/rajasthan.jpeg")
        st.image(image,caption='The royals',width=600)


### This function is used to give the player abtting record against each and every ipl team.
def batsman_record(batsman):
    name=ipl[ipl['batsman']==batsman]
    st.subheader(batsman+"-"+"record against each teams")
    player=name.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).reset_index()
    b_four=ipl[(ipl['batsman_runs']==4) & (ipl['batsman']==batsman)]
    player['No_Of_fours']=b_four.groupby('bowling_team')['batsman_runs'].count().sort_values(ascending=False).reset_index()['batsman_runs']
    b_six=ipl[(ipl['batsman_runs']==6) & (ipl['batsman']==batsman)]
    player['NO_Of_sixes']=b_six.groupby('bowling_team')['batsman_runs'].count().sort_values(ascending=False).reset_index()['batsman_runs']
    name=ipl[ipl['batsman']==batsman]
    player['ball_played']=name.groupby('bowling_team')['ball'].count().reset_index()['ball']
    player['Strike_rate']=player['batsman_runs']/player['ball_played']*100
    return player

### This function return the all player list of individual ipl teams.
def batsman_list(team):
    teams=ipl.groupby('batting_team')
    player_name=list(teams.get_group(team)['batsman'].unique())
    #st.json({'player_names':player_name})
    #for i in player_name:
     #   st.markdown("- " + i)
    name=st.selectbox("Select player",player_name)
    return name

### This fucntion is give the details about IPl teams  and each and every player.
def ipl_analysis():
    st.sidebar.header(":green[IPL]-:red[Menu]",divider='rainbow')
    option=st.sidebar.selectbox(":orange[Select below option for analysis]:sunglasses:",['Overall IPL Analysis','Team analysis'])
    st.sidebar.write('You selected:', option)

    record = None  # Initialize the record variable

    ### Overall analysis
    if option=='Overall IPL Analysis':
        btn=st.sidebar.button("IPL-analysis")
        if btn:
            IPL()

    ### Selecting option
    elif option=='Team analysis':
        team=st.sidebar.selectbox(":green[Select Team]",list(set(ipl['batting_team'])))
        st.sidebar.write('You selected:',team)
        #btn1=st.sidebar.button("Team analysis")
        #if btn1:
        team_analysis(team)
        player_name=batsman_list(team)
        record=batsman_record(player_name)
    return record

if __name__=='__main__':
   ipl_record=ipl_analysis()
   if ipl_record is not None:
       st.write(ipl_record)

    
    
    
   
  



