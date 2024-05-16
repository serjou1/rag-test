from pydantic import BaseModel


class FindEpisodeRequest(BaseModel):
    episode_description: str
