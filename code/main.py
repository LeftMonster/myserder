# -*- coding: utf-8 -*
import os

import gradio as gr
import pandas as pd
import uuid
import requests
import threading
import logging

# from util.logger_util import logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

file_lock = threading.Lock()

with gr.Blocks(title="AI Shell") as app:
    with gr.Tab("图生视频") as media_handler:

        with gr.Tab("任务提交"):
            pass

        with gr.Tab("记录"):
            df = pd.DataFrame()
            # df = df.sort_values(by='提交时间', na_position='last', ascending=False)


if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=80)
