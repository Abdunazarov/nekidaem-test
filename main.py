# thirdparty
from fastapi import FastAPI

# project
from routers import blogs, users, subscriptions, news_feed

app = FastAPI()

app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(subscriptions.router)
app.include_router(news_feed.router)
