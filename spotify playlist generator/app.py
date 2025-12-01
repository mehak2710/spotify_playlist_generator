import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Define dataset directly in code
songs = [
    {"title": "Happy", "artist": "Pharrell Williams", "tempo": 160, "energy": 0.85, "danceability": 0.90},
    {"title": "Someone Like You", "artist": "Adele", "tempo": 68, "energy": 0.40, "danceability": 0.35},
    {"title": "Blinding Lights", "artist": "The Weeknd", "tempo": 171, "energy": 0.95, "danceability": 0.80},
    {"title": "Shape of You", "artist": "Ed Sheeran", "tempo": 96, "energy": 0.80, "danceability": 0.85},
    {"title": "Lose Yourself", "artist": "Eminem", "tempo": 171, "energy": 0.92, "danceability": 0.70},
    {"title": "Perfect", "artist": "Ed Sheeran", "tempo": 63, "energy": 0.45, "danceability": 0.40},
    {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "tempo": 115, "energy": 0.88, "danceability": 0.89},
    {"title": "Let Her Go", "artist": "Passenger", "tempo": 75, "energy": 0.50, "danceability": 0.45},
    {"title": "Believer", "artist": "Imagine Dragons", "tempo": 125, "energy": 0.90, "danceability": 0.75},
    {"title": "Stay", "artist": "Rihanna ft. Mikky Ekko", "tempo": 84, "energy": 0.55, "danceability": 0.50},
]

# Convert to DataFrame
df = pd.DataFrame(songs)

st.title("🎧 Spotify Playlist Generator ")

# Sidebar: choose mood
mood = st.sidebar.selectbox("Choose a mood", ["Happy", "Sad", "Energetic", "Calm"])

# Clustering
features = df[['tempo', 'energy', 'danceability']]
kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(features)

# Map moods to clusters
mood_map = {"Happy":0, "Sad":1, "Energetic":2, "Calm":3}
chosen_cluster = mood_map[mood]

# Show playlist
st.subheader(f"Playlist for {mood} mood")
playlist = df[df['cluster'] == chosen_cluster][['title', 'artist']]
st.write(playlist)

# Scatter plot visualization
st.subheader("🎨 Cluster Visualization")
fig, ax = plt.subplots()
scatter = ax.scatter(df['tempo'], df['energy'], c=df['cluster'], cmap='viridis', s=100)

# Add labels
for i, row in df.iterrows():
    ax.text(row['tempo']+1, row['energy']+0.01, row['title'], fontsize=8)

ax.set_xlabel("Tempo (BPM)")
ax.set_ylabel("Energy")
ax.set_title("Song Clusters by Tempo & Energy")
st.pyplot(fig)

# WordCloud visualization
st.subheader("☁️ WordCloud for Playlist")
text = " ".join(playlist['title'].tolist() + playlist['artist'].tolist())
wordcloud = WordCloud(width=600, height=400, background_color="white").generate(text)

fig_wc, ax_wc = plt.subplots()
ax_wc.imshow(wordcloud, interpolation="bilinear")
ax_wc.axis("off")
st.pyplot(fig_wc)
