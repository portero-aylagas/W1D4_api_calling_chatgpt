from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import uuid

TRACKER_PATH = Path("logs/token_usage.csv")
TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)

def init_tracker_file(path=TRACKER_PATH):
    if not path.exists():
        df = pd.DataFrame(columns=[
            "timestamp",
            "call_id",
            "model",
            "endpoint",
            "row_idx",
            "prompt_tokens",
            "completion_tokens",
            "total_tokens",
            "input_cost_usd",
            "output_cost_usd",
            "total_cost_usd",
            "has_image",
            "image_count",
            "prompt_chars",
            "response_chars",
            "success",
            "error_type",
            "error_message",
        ])
        df.to_csv(path, index=False)
