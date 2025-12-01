
# 🎧 Spotify Playlist Generator

## 📌 Overview
This project is a **mini data science app** built with **Streamlit** that generates playlists based on user moods.  
It uses **KMeans clustering** on song features (*tempo, energy, danceability*) to group tracks into clusters.  
Users can select a mood (Happy, Sad, Energetic, Calm) and instantly see:
- A **playlist** of songs matching the mood  
- A **scatter plot visualization** showing how songs are grouped  
- A **cluster statistics summary** with average tempo, energy, and danceability  

## ⚡ Features
- **Mood-based playlist generation** using clustering  
- **Interactive Streamlit UI** with sidebar mood selection  
- **Scatter plot visualization** of clusters by tempo & energy  
- **Cluster statistics summary** for analytical insights  
- **Self-contained dataset** (songs defined directly in code, no CSV required)  

## 🛠️ Tech Stack
- **Python**  
- **Streamlit** (UI framework)  
- **scikit-learn** (KMeans clustering)  
- **Matplotlib** (scatter plots)  
- **Pandas** (data handling)  

## 📊 Key Performance Indicators (KPIs)
- **Playlist Accuracy**: Songs grouped correctly into mood clusters (≥80% thematic consistency).  
- **Cluster Balance**: Each cluster contains at least 2–3 songs, avoiding empty groups.  
- **User Interaction**: Mood selection updates playlist instantly (<1s response time).  
- **Visualization Clarity**: Scatter plot labels remain readable and distinct across clusters.  
- **Code Simplicity**: Entire app runs in <100 lines of Python code.  
