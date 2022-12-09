from os.path import join
from pathlib import Path

MODEL_PATH: str = "/workspace/data-centric-deep-learning/course/week2/pipeline_project/artifacts/ckpts/regression_flow/epoch=9-step=15000.ckpt"

# Use redis as the broker
BROKER_URL: str = 'redis://localhost:6379/0'

# Use redis as the backend cache as well
BACKEND_URL: str = 'redis://localhost:6379/0'
