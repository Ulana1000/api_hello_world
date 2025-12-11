from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
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



@app.get("/random_quote")
async def get_random_quote() -> dict[str, str]:
quotes = [
"ま",
"み",
"む",
"め"
]
return {"quote": random.choice(quotes)}
