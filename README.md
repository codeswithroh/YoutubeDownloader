# YouTube Downloader

## Overview

YouTube Downloader is a simple Python application that allows you to download YouTube videos easily. The application uses Streamlit for the user interface and leverages the power of the `pytube` library for video downloading.

## Prerequisites

Before running the application, make sure you have the following installed on your system:

- Python (version 3.6 or later)
- Git

## Getting Started

Follow the steps below to set up and run the YouTube Downloader:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### On Windows

```bash
venv\Scripts\activate

or

source venv/Scripts/activate
```

#### On macOS and Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run main.py
```

This command will launch the application in your default web browser.

## Usage

1. Enter the URL of the YouTube video you want to download.
2. Choose the desired video quality and format.
3. Click the "Download" button to start the download.

## Contributing

If you'd like to contribute to the development of YouTube Downloader, feel free to fork the repository and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
