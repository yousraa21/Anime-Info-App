# Anime-Info-App
This is a Python application that displays information about an anime, including the number of episodes, status, seasons, genre, and the manga chapter to start reading from after finishing the anime. The app uses the AniList API and Tkinter for the GUI.
## Features

    Search for an anime and get details such as episodes, status, seasons, and genre.
    Find out where to pick up the manga after finishing the anime.
    User-friendly interface with Tkinter.
## Installation
### Requirements

    Python 3.x
    tkinter library
    requests library
    pandas library
    Pillow library
### Setup

    1 Clone the repository:```git clone https://github.com/yourusername/anime-info-app.git
    cd anime-info-app```
    2 Install the required packages: ```pip install tkinter requests pandas pillow```
    3 Place the necessary image files (search field.png, search_icon.png, logo.png, big box.png, small box.png) in the project directory.
    4 Ensure you have the anime data.xlsx file in the project directory, which contains the manga chapter data. This dataset is a small one created specifically for this project.
### Usage

   1 Run the application: ```python animecode.py```
   2 Enter the name of the anime in the search field and click the search icon.
   3 The app will display the number of episodes, status, seasons, genre, and the manga chapter to start reading from after the anime.
## API Used

This app uses the AniList GraphQL API to fetch anime information.
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Acknowledgments

    AniList for their API.
    The Tkinter library for the GUI components.
    yousra lat for developing the app.
    Special mention for the anime data.xlsx dataset created specifically for this project.
