import streamlit as st

# 1. 頁面設定 (保持寬版)
st.set_page_config(page_title="易鏡 - 文青卜卦", layout="wide")

# 2. 你的完整 HTML 程式碼字串
html_code = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    </head>
<body>
    ...
</body>
</html>
"""

# 3. 【修正這裡】使用最新的 st.iframe 來建立獨立的沙盒環境
st.iframe(html=html_code, height=1200, scrolling=True)
