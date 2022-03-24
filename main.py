################### KÜTÜPHANELER ###################
import streamlit as st
from pytube import YouTube
import time
from pathlib import Path
import datetime

################### SAYFA AYARLARI ###################
st.set_page_config(
  page_title = 'Youtube Video Downloader',
  page_icon = '✅',
  layout="wide"
 )

################### İNDİRME SAYFASI ###################
try: # Enter your url placeholderı url formatında olmadığı için regex hata veriyordu. Önlemek için try except bloğuna aldım.
    st.markdown("<h1 style='text-align:center;'>You<font color='red'>tube</font> Video <font color='black'>Downloader</font></h1>", unsafe_allow_html=True)
    get_link = st.text_input("URL:", "https://www.youtube.com/watch?v=")

    ys = ""
    yt = YouTube(get_link)
    # st.video(get_link)
    st.markdown("***")
    st.write(" ### Title: ", yt.title)
    st.write(" ### Length: ", str(datetime.timedelta(seconds=yt.length)), " minutes")
    st.markdown("***")

    quality = st.radio(
        " Choose video quality",
        ('High', 'Low', 'Audio Only'))

    if quality == 'High':
        st.write('**High quality** selected.')
        ys = yt.streams.get_highest_resolution()

    elif quality == 'Low':
        st.write('**Low quality** selected.')
        ys = yt.streams.get_lowest_resolution()

    elif quality == "Audio Only":
        st.write("**Audio Only** selected.")
        ys = yt.streams.get_audio_only()

    st.markdown("***")

    downloads_path = str(Path.home() / "Downloads")
    st.download_button("Download", ys.download(downloads_path))

except:
    pass
