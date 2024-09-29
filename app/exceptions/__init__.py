from fastapi import FastAPI, HTTPException
import logging

class Error(Exception):
    def __init__(self, message: str, status_code: int):
        logging.error(message)
        self.message = message
        self.status_code = status_code
        self.error()

    def error(self):
        raise HTTPException(self.status_code, detail=self.message)