import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import threading
import os
import sys
from pathlib import Path

class YouTubeDownloader:
    def __init__(self):
        # Set appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("YouTube Video Downloader")
        self.root.geometry("900x750")  # Increased size to show all content
        self.root.resizable(True, True)
        self.root.minsize(800, 700)  # Set minimum size
        
        # Variables
        self.download_path = tk.StringVar(value=str(Path.home() / "Downloads"))
        self.url_var = tk.StringVar()
        self.format_var = tk.StringVar(value="mp4")
        self.quality_var = tk.StringVar(value="720p")
        self.is_playlist = tk.BooleanVar()
        
        # Progress variables
        self.progress_var = tk.DoubleVar()
        self.status_var = tk.StringVar(value="Ready to download")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self.root)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Main container inside scrollable frame
        main_frame = ctk.CTkFrame(self.scrollable_frame)
        main_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Title
        title_label = ctk.CTkLabel(
            main_frame, 
            text="YouTube Video Downloader",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.pack(pady=(20, 30))
        
        # URL input section
        url_frame = ctk.CTkFrame(main_frame)
        url_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        url_label = ctk.CTkLabel(url_frame, text="YouTube URL:", font=ctk.CTkFont(size=14, weight="bold"))
        url_label.pack(anchor="w", padx=20, pady=(20, 5))
        
        self.url_entry = ctk.CTkEntry(
            url_frame,
            textvariable=self.url_var,
            placeholder_text="Paste YouTube video or playlist URL here...",
            height=40,
            font=ctk.CTkFont(size=12)
        )
        self.url_entry.pack(fill="x", padx=20, pady=(0, 20))
        
        # Options section
        options_frame = ctk.CTkFrame(main_frame)
        options_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        options_label = ctk.CTkLabel(options_frame, text="Download Options:", font=ctk.CTkFont(size=14, weight="bold"))
        options_label.pack(anchor="w", padx=20, pady=(20, 10))
        
        # Format and quality row
        format_frame = ctk.CTkFrame(options_frame)
        format_frame.pack(fill="x", padx=20, pady=(0, 10))
        
        # Format selection
        format_label = ctk.CTkLabel(format_frame, text="Format:", font=ctk.CTkFont(size=12))
        format_label.pack(side="left", padx=(20, 10), pady=15)
        
        format_menu = ctk.CTkOptionMenu(
            format_frame,
            variable=self.format_var,
            values=["mp4", "mp3"],
            command=self.on_format_change
        )
        format_menu.pack(side="left", padx=(0, 20), pady=15)
        
        # Quality selection
        quality_label = ctk.CTkLabel(format_frame, text="Quality:", font=ctk.CTkFont(size=12))
        quality_label.pack(side="left", padx=(20, 10), pady=15)
        
        self.quality_menu = ctk.CTkOptionMenu(
            format_frame,
            variable=self.quality_var,
            values=["1080p", "720p", "480p", "360p", "best", "worst"]
        )
        self.quality_menu.pack(side="left", padx=(0, 20), pady=15)
        
        # Playlist checkbox
        playlist_check = ctk.CTkCheckBox(
            options_frame,
            text="Download entire playlist (if URL is a playlist)",
            variable=self.is_playlist,
            font=ctk.CTkFont(size=12)
        )
        playlist_check.pack(anchor="w", padx=20, pady=(0, 20))
        
        # Download path section
        path_frame = ctk.CTkFrame(main_frame)
        path_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        path_label = ctk.CTkLabel(path_frame, text="Download Location:", font=ctk.CTkFont(size=14, weight="bold"))
        path_label.pack(anchor="w", padx=20, pady=(20, 5))
        
        path_input_frame = ctk.CTkFrame(path_frame)
        path_input_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.path_entry = ctk.CTkEntry(
            path_input_frame,
            textvariable=self.download_path,
            height=35,
            font=ctk.CTkFont(size=11)
        )
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=10)
        
        browse_btn = ctk.CTkButton(
            path_input_frame,
            text="Browse",
            command=self.browse_folder,
            width=80,
            height=35
        )
        browse_btn.pack(side="right", padx=(5, 10), pady=10)
        
        # Progress section
        progress_frame = ctk.CTkFrame(main_frame)
        progress_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        progress_label = ctk.CTkLabel(progress_frame, text="Progress:", font=ctk.CTkFont(size=14, weight="bold"))
        progress_label.pack(anchor="w", padx=20, pady=(20, 5))
        
        self.progress_bar = ctk.CTkProgressBar(progress_frame, height=20)
        self.progress_bar.pack(fill="x", padx=20, pady=(0, 10))
        self.progress_bar.set(0)
        
        self.status_label = ctk.CTkLabel(
            progress_frame,
            textvariable=self.status_var,
            font=ctk.CTkFont(size=11)
        )
        self.status_label.pack(anchor="w", padx=20, pady=(0, 20))
        
        # Download button - Made more prominent
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(fill="x", padx=20, pady=(10, 20))
        
        self.download_btn = ctk.CTkButton(
            button_frame,
            text="🚀 DOWNLOAD VIDEO 🚀",
            command=self.start_download,
            height=60,
            width=300,
            font=ctk.CTkFont(size=18, weight="bold"),
            fg_color="#1f538d",
            hover_color="#14375e",
            corner_radius=10
        )
        self.download_btn.pack(pady=20, expand=True)
        
        # Add instruction label
        instruction_label = ctk.CTkLabel(
            button_frame,
            text="👆 Click the blue button above to start downloading! 👆",
            font=ctk.CTkFont(size=12),
            text_color="#7CC7FF"
        )
        instruction_label.pack(pady=(0, 15))
        
    def on_format_change(self, choice):
        if choice == "mp3":
            self.quality_menu.configure(values=["320kbps", "256kbps", "192kbps", "128kbps", "best", "worst"])
            self.quality_var.set("320kbps")
        else:
            self.quality_menu.configure(values=["1080p", "720p", "480p", "360p", "best", "worst"])
            self.quality_var.set("720p")
    
    def browse_folder(self):
        folder = filedialog.askdirectory(initialdir=self.download_path.get())
        if folder:
            self.download_path.set(folder)
    
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            try:
                if 'total_bytes' in d:
                    progress = d['downloaded_bytes'] / d['total_bytes']
                elif 'total_bytes_estimate' in d:
                    progress = d['downloaded_bytes'] / d['total_bytes_estimate']
                else:
                    progress = 0
                
                self.progress_var.set(progress)
                self.progress_bar.set(progress)
                
                filename = d.get('filename', 'Unknown')
                if len(filename) > 50:
                    filename = filename[:47] + "..."
                
                self.status_var.set(f"Downloading: {filename}")
                self.root.update_idletasks()
            except:
                pass
        elif d['status'] == 'finished':
            self.status_var.set(f"Finished: {os.path.basename(d['filename'])}")
            self.root.update_idletasks()
    
    def download_video(self):
        try:
            url = self.url_var.get().strip()
            if not url:
                messagebox.showerror("Error", "Please enter a YouTube URL")
                return
            
            download_path = self.download_path.get()
            if not os.path.exists(download_path):
                os.makedirs(download_path)
            
            # Configure yt-dlp options
            ydl_opts = {
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'progress_hooks': [self.progress_hook],
            }
            
            format_choice = self.format_var.get()
            quality = self.quality_var.get()
            
            if format_choice == "mp3":
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': quality.replace('kbps', '') if 'kbps' in quality else '192',
                    }]
                })
            else:
                if quality == "best":
                    ydl_opts['format'] = 'best[ext=mp4]'
                elif quality == "worst":
                    ydl_opts['format'] = 'worst[ext=mp4]'
                else:
                    height = quality.replace('p', '')
                    ydl_opts['format'] = f'best[height<={height}][ext=mp4]/best[ext=mp4]'
            
            # Handle playlist option
            if not self.is_playlist.get():
                ydl_opts['noplaylist'] = True
            
            self.status_var.set("Starting download...")
            self.download_btn.configure(state="disabled", text="Downloading...")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            self.progress_bar.set(1.0)
            self.status_var.set("Download completed successfully!")
            messagebox.showinfo("Success", "Download completed successfully!")
            
        except Exception as e:
            error_msg = str(e)
            self.status_var.set(f"Error: {error_msg}")
            messagebox.showerror("Download Error", f"An error occurred:\n{error_msg}")
        
        finally:
            self.download_btn.configure(state="normal", text="Download")
            self.progress_bar.set(0)
    
    def start_download(self):
        # Run download in separate thread to prevent UI freezing
        download_thread = threading.Thread(target=self.download_video)
        download_thread.daemon = True
        download_thread.start()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    print("Starting YouTube Downloader...")
    print("If you don't see the application window, check your taskbar or try Alt+Tab")
    app = YouTubeDownloader()
    print("Application window created successfully!")
    print("The download button should be visible as a large blue button with rocket emojis")
    app.run()