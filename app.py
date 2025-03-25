from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

app = FastAPI()

# Set your default prefix (e.g., 12ft.io, Scribe.rip, etc.)
DEFAULT_PREFIX = "https://readmedium.com/en/"  # Change this if needed

# Serve static files (for HTML)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/redirect")
async def redirect_to_modified_url(url: str = Form(...)):
    """Takes user input URL and redirects to the prefixed URL."""
    modified_url = DEFAULT_PREFIX + url
    print(modified_url)
    return RedirectResponse(url=modified_url)


@app.get("/")
async def homepage(request: Request):
    """Serve the simple HTML form."""
    return RedirectResponse(url="/static/index.html")
