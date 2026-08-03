from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# temporary database
script_database = []

class Episode(BaseModel):
    volume_number: int
    episode_title: str
    page_count: int

# Add a new episode draft to database
@app.post("/episodes")
def add_episode(epi: Episode):
    new_episode_data = {
        "id": len(script_database)+1,
        "Volume": epi.volume_number,
        "title": epi.episode_title,
        "pages": epi.page_count
    }

    # Add new episode to the database
    script_database.append(new_episode_data)

    return{
        "message": "Episode saved successfully",
        "Saved_info": new_episode_data
    }

# Fetch episodes
@app.get("/episodes")
def get_episodes():
    return {
        "total_episodes": len(script_database),
        "Episodes": script_database
    }

