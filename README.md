# Billboard Hot 100 Playlist Creator

This Python script scrapes the Billboard Hot 100 songs for a user-specified date, searches for these songs on Spotify, and creates a playlist of the top tracks. Perfect for reliving the music of your favorite year!

---

## Features

- Scrapes the Billboard Hot 100 for any date in history.
- Searches for songs on Spotify using the Spotify Web API.
- Automatically creates a private playlist with the top tracks.
- Skips unavailable songs gracefully.

---

## Requirements

- Python 3.7 or later
- Spotify Developer Account
- `spotipy` for interacting with Spotify API
- `BeautifulSoup` for web scraping
- `requests` for HTTP requests
- `.env` file to securely store Spotify credentials

---

## Installation

1. Clone the repository

2. Install required Python packages

3. Create a `.env` file in the project directory with your Spotify credentials:
   ```env
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   ```

---

## Usage

1. Run the script:
   ```bash
   main.py
   ```

2. Enter a date in the format `YYYY-MM-DD` when prompted.

3. Check your Spotify account for a new playlist titled `<date> Billboard 100`.

---

## Example Output

```
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 2020-01-01
"Blinding Lights" added to playlist.
"Circles" added to playlist.
"Adore You" doesn't exist in Spotify. Skipped.
...
Playlist '2020-01-01 Billboard 100' created successfully!
```

---

## Notes

- Ensure that the Billboard website structure hasn’t changed. If the script fails, update the CSS selectors in the `soup.select()` method.
- You may hit rate limits if you run the script too frequently. If so, try adding a delay between Spotify API calls.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

---
