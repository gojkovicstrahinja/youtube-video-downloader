# YouTube Video Downloader

A modern, user-friendly YouTube video downloader with a beautiful GUI interface. Download videos in MP4 format or extract audio as MP3, with support for individual videos and entire playlists.

## Features

✨ **Modern Dark Theme UI** - Beautiful and intuitive interface using CustomTkinter

🎥 **Multiple Formats** - Download videos in MP4 or extract audio as MP3

📋 **Playlist Support** - Download entire playlists with any number of videos

🎯 **Quality Options** - Choose from various video qualities (1080p, 720p, 480p, 360p) or audio bitrates (320kbps, 256kbps, 192kbps, 128kbps)

📁 **Custom Download Location** - Choose where to save your downloads

📊 **Real-time Progress** - Live progress bar and status updates

⚡ **Fast & Reliable** - Built with yt-dlp for optimal performance

## Requirements

- Python 3.7 or higher
- Windows operating system
- Internet connection

## Installation

### Option 1: Automatic Setup (Recommended)

1. Download or clone this repository
2. Double-click `setup.bat` to automatically install all dependencies
3. Double-click `run.bat` to start the application

### Option 2: Manual Installation

1. Open Command Prompt or PowerShell in the project directory
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python youtube_downloader.py
   ```

## Usage

1. **Launch the Application**
   - Double-click `run.bat` or run `python youtube_downloader.py`

2. **Enter YouTube URL**
   - Paste any YouTube video or playlist URL in the input field

3. **Choose Format**
   - Select **MP4** for video downloads
   - Select **MP3** for audio-only downloads

4. **Select Quality**
   - For MP4: Choose from 1080p, 720p, 480p, 360p, or best/worst
   - For MP3: Choose from 320kbps, 256kbps, 192kbps, 128kbps, or best/worst

5. **Playlist Option**
   - Check "Download entire playlist" to download all videos in a playlist
   - Leave unchecked to download only the specific video

6. **Choose Download Location**
   - Click "Browse" to select where files should be saved
   - Default location is your Downloads folder

7. **Start Download**
   - Click the "Download" button
   - Monitor progress with the real-time progress bar

## Supported Sites

While primarily designed for YouTube, this downloader supports many video platforms thanks to yt-dlp, including:

- YouTube (videos and playlists)
- YouTube Music
- Vimeo
- Dailymotion
- And many more...

## File Structure

```
YT video downloader/
├── youtube_downloader.py    # Main application file
├── requirements.txt         # Python dependencies
├── setup.bat               # Automatic setup script
├── run.bat                 # Application launcher
└── README.md               # This file
```

## Dependencies

- **yt-dlp**: Modern YouTube downloader library
- **customtkinter**: Modern GUI framework
- **Pillow**: Image processing library
- **requests**: HTTP library
- **pygame**: Audio support

## Troubleshooting

### Common Issues

**"Python is not installed or not in PATH"**
- Install Python from [python.org](https://python.org)
- Make sure to check "Add Python to PATH" during installation

**"Error installing dependencies"**
- Check your internet connection
- Try running `pip install --upgrade pip` first
- Run Command Prompt as Administrator

**"Download failed"**
- Verify the YouTube URL is correct and accessible
- Check your internet connection
- Some videos may be region-restricted or private

**"FFmpeg not found" (for MP3 conversion)**
- yt-dlp will automatically download FFmpeg when needed
- If issues persist, manually install FFmpeg from [ffmpeg.org](https://ffmpeg.org)

### Performance Tips

- For large playlists, consider downloading during off-peak hours
- Choose lower quality settings for faster downloads
- Ensure sufficient disk space before downloading

## Legal Notice

This tool is for personal use only. Please respect copyright laws and YouTube's Terms of Service. Only download content you have permission to download or that is available under appropriate licenses.

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have suggestions for improvements, please feel free to create an issue or contribute to the project.

---

**Enjoy downloading your favorite YouTube content! 🎉**