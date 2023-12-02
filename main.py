import streamlit as st
from pytube import YouTube
import platform
import os


def get_default_download_path():
    system = platform.system()

    if system == 'Windows':
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == 'Darwin':  # Mac OS
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == 'Linux':
        return os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        # Unsupported operating system
        raise Exception(f"Unsupported operating system: {system}")


def download_video(url, download_path):
    try:
        # Display loading spinner while downloading
        with st.spinner("Downloading..."):
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            video.download(download_path)

        # Remove "Downloading..." text after download is complete
        # st.info("")
        st.success("Download complete!")
    except Exception as e:
        st.error(f"Error: {str(e)}")


def main():
    st.title("YouTube Video Downloader")

    # Input for YouTube URL
    url = st.text_input("Enter YouTube Video URL:")

    download_path = get_default_download_path()

    if st.button("Download"):
        if url and download_path:
            download_video(url, download_path)
        else:
            st.warning(
                "Please provide the YouTube URL")


if __name__ == "__main__":
    main()
