from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_index() -> str:
    return """
    <html>
      <head>
        <title>FastAPI Hello</title>
      </head>
      <body>
        <h1>Welcome</h1>
        <p>Open the interactive API docs at http://URL/docs.</p>
      </body>
    </html>
    """
from datetime import datetime

@app.get("/greet/{name}")
async def greet_user(name: str) -> dict[str, str]:
    return {
"message": f" {name} ",
"timestamp": datetime.now().strftime("%H:%M:%S")
}
