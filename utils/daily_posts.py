# thirdparty
from celery import Celery
from services.news_feed_service import get_news_feed

app = Celery("tasks", broker=BROKER_URI)


@app.task
def send_daily_posts(user_id: int):
    posts = get_news_feed(user_id, skip=0, limit=5)
    print(f"Latest posts for user {user_id}: {posts}")
