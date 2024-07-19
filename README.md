# 🎈 Image Style Transfer

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Download the repository
   ```
   $ git clone https://github.com/aniketyevankar/image-style-transfer.git
   ```

2. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

3. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

### Flow
```mermaid
graph LR
    A((Streamlit App Start)) --> B{Upload Image Option}
    B --> C{Define Style Images}
    C --> D{Load Uploaded Image}
    D --> E{Check if Image and Style are Selected}
    E -- Yes --> F{Apply Style Transfer}
    E -- No --> N((End Flow))
    F --> N((End Flow))
```