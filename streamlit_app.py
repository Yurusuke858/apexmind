import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="ApexMind", layout="wide")
st.title("ApexMind β版")

# アップロード欄
uploaded_file = st.file_uploader("ログファイルをアップロードしてください（csv/json/ibt）", type=["csv", "json", "ibt"])

if uploaded_file:
    st.success(f"{uploaded_file.name} を受け取りました ✅")

    # 保存先のパスを生成
    save_dir = "uploads"
    os.makedirs(save_dir, exist_ok=True)
    
    # タイムスタンプを含めたファイル名にする（重複防止）
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    save_path = os.path.join(save_dir, f"{timestamp}_{uploaded_file.name}")

    # 保存処理
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info(f"ファイルを保存しました： `{save_path}`")
