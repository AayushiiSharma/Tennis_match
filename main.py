import streamlit as st
import pickle
import numpy as np


# Load your pre-trained model
with open("ball_detections.pkl", "rb") as file:
    model = pickle.load(file)

st.markdown("""
    <style>
    .css-1y0tads {  /* Specific class for the file uploader */
        max-width: 150px;  /* Adjust width as needed */
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
# Title
st.title("Tennis Game Tracking")

# Create layout with columns
col1, col2 = st.columns([3, 3])  # Adjust ratio to control width

# Column 1 - Video Display Area
with col1:
    # Placeholder for video
    video_display = st.empty()  # Empty space to display video
    st.write("Video")  # Placeholder text (you can remove if not needed)

# Column 2 - Control Buttons
with col2:
    # File uploader for input video
    st.markdown("### Select Input File")
    video_file = st.file_uploader("Select Input File", type=["mp4", "mov", "avi", "mkv"], label_visibility='collapsed')
      # Add a custom label above the uploader


    # Button to preview video
    if video_file:
        if st.button("Preview Video"):
            temp_video_path = "uploaded_video.mp4"
            with open(temp_video_path, "wb") as f:
                f.write(video_file.read())
            video_display.video(temp_video_path)

    # Progress placeholder
    progress_placeholder = st.empty()
    progress_placeholder.text("0%")

    # Button to process video
    if st.button("Process Video"):
        # Update progress (for demonstration purposes)
        for percent_complete in range(0, 101, 20):
            progress_placeholder.text(f"{percent_complete}%")
            st.time.sleep(0.5)  # Simulate processing delay
        st.success("Processing complete!")

    # Button to show output
    if st.button("Show Output"):
        st.write("Displaying processed output here...")
        # Add code to display actual output if available
        

    # Button to download output
    if st.button("Download Output"):
        st.write("Download link will appear here.")
        # Add code to generate and provide download link