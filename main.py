import os
from pathlib import Path

import uvicorn
from dotenv import load_dotenv

from src.app import *

load_dotenv()

if __name__ == "__main__":
    uvicorn.run(
        f"{Path(__file__).stem}:app",
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT")),
        reload=os.getenv("RELOAD"),
        debug=os.getenv("DEBUG"),
        log_level="info",
        workers=int(os.getenv("WORKERS")),
        factory=False,
    )