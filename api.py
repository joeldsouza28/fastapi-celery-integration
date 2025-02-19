from fastapi import FastAPI
from pydantic import BaseModel
from worker.worker import send_email
app = FastAPI()


class EmailRequest(BaseModel):
    recipient: str
    subject: str
    message: str


@app.post("/send-email/")
def trigger_email(email: EmailRequest):
    task = send_email.delay(email.recipient, email.subject, email.message)
    return {"task_id": task.id, "message": "Email task started"}