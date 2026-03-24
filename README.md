# ai-voice-app

GPU 対応の Devcontainer 上で動作する、XTTS‑v2 を用いた日本語音声合成アプリです。  
パッケージ管理には `uv` を使用し、再現性の高い開発環境を構築しています。

---

## 🚀 機能

- XTTS‑v2 による高品質な日本語音声合成
- 数秒の音声から話者特徴を抽出してクローン音声を生成
- Devcontainer + WSL2 + NVIDIA GPU による高速推論
- `uv` による高速・安定した依存管理

---

## 🧱 開発環境

- Windows 11  
- WSL2（Ubuntu）  
- Docker Desktop（WSL2 backend）  
- NVIDIA Container Toolkit（WSL2 にインストール）  
- GPU: NVIDIA GeForce RTX 3060  
- Python 3.10（コンテナ内）  
- uv（依存管理）

---

## 📦 セットアップ手順

### 1. リポジトリをクローン

```bash
git clone <your-repo-url>
cd ai-voice-app
```

### 2. VSCode で開く → Devcontainer を起動

VSCode のコマンドパレットから:

```
Reopen in Container
```

### 3. 依存インストール

Devcontainer 起動時に自動で `uv sync` が実行されます。

手動で行う場合:

```bash
uv sync
```

### 4. 音声サンプルを配置

```
ai-voice-app/
 └─ voice_sample.wav  ← あなたの声のサンプル
```

### 5. 音声合成を実行

```bash
python main.py
```

`output.wav` が生成されます。

---

## 📁 プロジェクト構成

```
ai-voice-app/
 ├─ .devcontainer/
 │    ├─ devcontainer.json
 │    └─ Dockerfile
 ├─ pyproject.toml
 ├─ main.py
 └─ voice_sample.wav（ユーザーが追加）
```

---

## 📝 main.py の概要

- XTTS‑v2 モデルを GPU にロード
- `voice_sample.wav` から話者特徴を抽出
- 指定テキストをクローン音声で生成

---

## ⚠️ 注意事項

- 他人の声を無断でクローンすることは法律・倫理の両面で問題があります  
- 自分の声、または許可を得た音声のみ使用してください  
- 大きなモデルを扱うため、GPU メモリ使用量に注意してください（RTX 3060 6GB で動作確認済み）

---

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。

```
