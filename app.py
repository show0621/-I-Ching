import streamlit as st
import streamlit.components.v1 as components

# 設定頁面寬度為寬版模式，讓視覺更開闊
st.set_page_config(page_title="易鏡 - 文青卜卦", layout="wide")

# 將 HTML 代碼放入變數 (這裡放入剛才生成的完整內容)
html_code = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>易鏡</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* CSS 內容... */
    </style>
</head>
<body>
    <script>
        // JavaScript 邏輯...
    </script>
</body>
</html>
"""

# 在 Streamlit 中呈現
# height 可以根據內容長度調整，以避免出現內部捲軸
components.html(html_code, height=1200, scrolling=True)
