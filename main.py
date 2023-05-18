from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
import requests

app = FastAPI()


class DataModel(BaseModel):
    hf_pipeline: str
    model_deployed_url: str
    inputs: Any
    parameter: Any


@app.post("/predict")
async def root(data: DataModel):
    pipeline = data.hf_pipeline.lower().replace(" ", "")
    if pipeline == "zeroshotclassification":
        API_URL = data.model_deployed_url
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query(
            {
                "inputs": data.inputs,
                "parameters": data.parameter,
            }
        )
        return output
    if pipeline == "objectdetection":
        API_URL = data.model_deployed_url
        headers = {"Authorization": "Bearer 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"}

        def query(filename):
            with open(filename, "rb") as f:
                data = f.read()
            response = requests.post(API_URL, headers=headers, data=data)
            return response.json()

        output = query("cats.jpg")
    if pipeline == "textgeneration":
        API_URL = data.model_deployed_url
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query(
            {
                "inputs": data.inputs,
            }
        )
        return output
    if pipeline == "tokenclassification":
        API_URL = data.model_deployed_url
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query(
            {
                "inputs": data.inputs,
            }
        )
        return output
