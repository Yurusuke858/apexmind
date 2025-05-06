import streamlit as st
import pandas as pd
import os
import mimetypes
from datetime import datetime

st.set_page_config(page_title="ApexMind", layout="wide")
st.title("ApexMind β版")

# アップロード欄
uploaded_file = st.file_uploader("ログファイルをアップロードしてください（csv/json/ibt）", type=["csv", "json", "ibt"])

# ファイル形式判定関数
def detect_file_type(file):
    filename = file.name.lower()
    if filename.endswith(".ibt"):
        return "ibt"
    elif filename.endswith(".json"):
        return "json"
    elif filename.endswith(".csv"):
        return "csv"
    else:
        mime, _ = mimetypes.guess_type(filename)
        if mime == "application/json":
            return "json"
        elif mime == "text/csv":
            return "csv"
        return "unknown"

# アップロードされた場合の処理
if uploaded_file:
    st.success(f"{uploaded_file.name} を受け取りました ✅")

    # 🔍 ファイル形式判定
    file_type = detect_file_type(uploaded_file)
    st.write(f"判定されたファイル形式: `{file_type}`")

    # 📁 保存処理
    save_dir = "uploads"
    os.makedirs(save_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    save_path = os.path.join(save_dir, f"{timestamp}_{uploaded_file.name}")
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.info(f"ファイルを保存しました： `{save_path}`")

