from fastapi import FastAPI
from pydantic import BaseModel
from worker.worker import send_email
app = FastAPI()

@app.post("/send-email/")
def trigger_email(user_id: str):
    task = send_email.delay(user_id)
    return {"task_id": task.id, "message": "Email task started"}