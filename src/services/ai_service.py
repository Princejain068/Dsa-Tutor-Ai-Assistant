import os
import json
import google.generativeai as genai
import re

from dotenv import load_dotenv
from src.models.response_model import AnalyzeResponse

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemma-4-31b-it")


def analyze_solution(problem: str, code: str):

    prompt = f"""
Return ONLY valid JSON.

Schema:

{{
  "correctness": "string",
  "time_complexity": "string",
  "space_complexity": "string",
  "better_approach": "string",
  "edge_cases": ["string"],
  "hints": ["string"],
  "teaching": "string"
}}

Problem:
{problem}

Code:
{code}
"""

    try:

        response = model.generate_content(
            prompt,
            generation_config={
                "response_mime_type": "application/json"
            }
        )

        print("\nRAW GEMINI RESPONSE:\n")
        print(response.text)

        matches = re.findall(r'\{[\s\S]*\}', response.text)

        if not matches:
            raise Exception("No valid JSON found")

        json_text = matches[-1]

        data = json.loads(json_text)

        validated = AnalyzeResponse(**data)

        return validated.model_dump()

    except Exception as e:

        print("\nERROR:\n", str(e))

        return {
            "correctness": "Error",
            "time_complexity": "",
            "space_complexity": "",
            "better_approach": "",
            "edge_cases": [],
            "hints": [],
            "teaching": str(e)
        }