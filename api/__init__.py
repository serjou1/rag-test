from contextlib import contextmanager

from fastapi import FastAPI

from api.schemas.find_episode_request import FindEpisodeRequest
from api.schemas.question_request import QuestionRequest

from modules.llm import SpHelper

sp_helper = SpHelper()
sp_helper.initialize()

app = FastAPI()


@app.get("/ask-question")
def ask_question(
        question_request: QuestionRequest
):
    return sp_helper.ask(question_request.question)


@app.get("/find-episode")
def find_episode(
        find_episode_request: FindEpisodeRequest
):
    return sp_helper.find_episode(find_episode_request.episode_description)
