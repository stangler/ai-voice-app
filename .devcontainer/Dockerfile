FROM python:3.10-slim

# 基本ツール + MeCab と辞書
RUN apt-get update && apt-get install -y \
    git ffmpeg build-essential curl \
    mecab mecab-ipadic-utf8 libmecab-dev \
    && rm -rf /var/lib/apt/lists/*

# uv インストール
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# CUDA 11.8 対応 PyTorch（RTX 3060 に最適）
RUN uv pip install --system torch \
    --index-url https://download.pytorch.org/whl/cu118

WORKDIR /workspace