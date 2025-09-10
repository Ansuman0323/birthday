from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the main page of the birthday website.
    Automatically loads photos and music from static folders.
    Customize the variables below for your girlfriend.
    """
    # CUSTOMIZE THESE VARIABLES FOR YOUR GIRLFRIEND
    name = "My Love"  # Change to her actual name
    anniversary_date = "2025-02-14"  # Change to your relationship start date (YYYY-MM-DD)
    favorite_song = "Main_Agar_Kahoon"  # Change to your song title
    birthday_message = "You are the most amazing person in my life! 💕"  # Personal message
    
    # PHOTO CONFIGURATION
    # Put your photos in: static/images/
    # Supported formats: jpg, jpeg, png, gif
    image_folder = 'static/images'
    photos = []
    photo_captions = [
        "Latest Memory ❤️",
        "Adventure Together 🌟", 
        "Perfect Day 🌅",
        "Making Memories 💕",
        "Beautiful Moments 🌺",
        "Forever & Always 🏖️"
    ]
    
    if os.path.exists(image_folder):
        image_files = []
        for filename in os.listdir(image_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                image_files.append(filename)
        
        # Sort files to maintain consistent order
        image_files.sort()
        
        # Create photo data with captions
        for i, filename in enumerate(image_files):
            photos.append({
                'url': f"/{image_folder}/{filename}",
                'caption': photo_captions[i] if i < len(photo_captions) else f"Memory {i+1} 💖"
            })
    
    # MUSIC CONFIGURATION
    # Put your song in: static/audio/
    # Supported formats: mp3, wav, ogg
    audio_folder = 'static/audio'
    song_url = None
    
    if os.path.exists(audio_folder):
        for filename in os.listdir(audio_folder):
            if filename.lower().endswith(('.mp3', '.wav', '.ogg')):
                song_url = f"/{audio_folder}/{filename}"
                break  # Use the first audio file found
    
    # CALCULATE RELATIONSHIP STATS
    try:
        start_date = datetime.strptime(anniversary_date, "%Y-%m-%d")
        today = datetime.now()
        total_days = (today - start_date).days
        
        years = total_days // 365
        remaining_days = total_days % 365
        months = remaining_days // 30
        days = remaining_days % 30
        hours = today.hour
        
        relationship_stats = {
            'years': years,
            'months': months, 
            'days': days,
            'hours': hours,
            'total_days': total_days
        }
    except:
        # Fallback if date parsing fails
        relationship_stats = {
            'years': 1,
            'months': 6,
            'days': 15,
            'hours': 12,
            'total_days': 500
        }
    
    # MEMORY TIMELINE
    memories = [
        {
            'title': '💫 The Day We Met',
            'description': 'It feels like yesterday when our paths crossed for the first time. That magical moment when I knew you were someone special who would change my life forever.'
        },
        {
            'title': '💕 Our First Date', 
            'description': 'The butterflies, the laughter, the way time seemed to stop when I looked into your eyes. That perfect evening that marked the beginning of our beautiful journey together.'
        },
        {
            'title': '🌟 This Moment',
            'description': 'Here we are, celebrating another year of your amazing life. Every day with you is a gift, and I\'m grateful for every laugh, every adventure, and every quiet moment we share.'
        }
    ]
    
    return render_template('index.html', 
                         name=name,
                         anniversary_date=anniversary_date,
                         favorite_song=favorite_song,
                         birthday_message=birthday_message,
                         photos=photos,
                         song_url=song_url,
                         relationship_stats=relationship_stats,
                         memories=memories)

@app.route('/upload-instructions')
def instructions():
    """
    Shows instructions for adding photos and music.
    Visit: http://localhost:5000/upload-instructions
    """
    instructions_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Upload Instructions</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 2rem; max-width: 800px; margin: 0 auto; }
            .folder { background: #f0f0f0; padding: 1rem; margin: 1rem 0; border-radius: 8px; }
            .code { background: #e8e8e8; padding: 0.5rem; border-radius: 4px; font-family: monospace; }
            .success { color: green; font-weight: bold; }
            .warning { color: orange; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>🎉 How to Add Your Photos and Music</h1>
        
        <h2>📁 Create These Folders:</h2>
        <div class="folder">
            <strong>your-project/</strong><br>
            ├── main.py<br>
            ├── templates/<br>
            │   └── index.html<br>
            └── <strong>static/</strong><br>
            &nbsp;&nbsp;&nbsp;&nbsp;├── <strong>images/</strong> ← Put your photos here<br>
            &nbsp;&nbsp;&nbsp;&nbsp;└── <strong>audio/</strong> ← Put your song here
        </div>
        
        <h2>📸 For Photos:</h2>
        <ol>
            <li>Create folder: <span class="code">static/images/</span></li>
            <li>Add your photos (JPG, PNG, GIF)</li>
            <li>Name them simply: <span class="code">photo1.jpg, photo2.jpg</span> etc.</li>
            <li>Recommended size: 800x600 pixels</li>
        </ol>
        
        <h2>🎵 For Music:</h2>
        <ol>
            <li>Create folder: <span class="code">static/audio/</span></li>
            <li>Add your song file (MP3, WAV, OGG)</li>
            <li>Name it simply: <span class="code">our_song.mp3</span></li>
        </ol>
        
        <h2>⚙️ Customize Your Website:</h2>
        <p>Edit these variables in <strong>main.py</strong>:</p>
        <div class="code">
            name = "Her Name Here"<br>
            anniversary_date = "2023-01-01"  # Your actual date<br>
            favorite_song = "Song Title"<br>
            birthday_message = "Your personal message"
        </div>
        
        <h2>🚀 After Adding Files:</h2>
        <ol>
            <li>Restart your Flask server (Ctrl+C then <span class="code">python main.py</span>)</li>
            <li>Refresh the website</li>
            <li class="success">Your photos and music will automatically appear!</li>
        </ol>
        
        <p><a href="/" style="background: #667eea; color: white; padding: 1rem 2rem; text-decoration: none; border-radius: 50px;">← Back to Birthday Website</a></p>
    </body>
    </html>
    """
    return instructions_html

if __name__ == '__main__':
    # Create static folders if they don't exist
    os.makedirs('static/images', exist_ok=True)
    os.makedirs('static/audio', exist_ok=True)
    
    print("🎉 Birthday Website Starting...")
    print("📁 Static folders created automatically")
    print("📋 Visit http://localhost:5000/upload-instructions for setup help")
    print("💕 Visit http://localhost:5000 for the birthday website")
    
    # The debug=True option automatically reloads the server when you
    # make changes to your code, which is great for development.
    app.run(debug=True)