import streamlit as st

# 1. 頁面設定 (保持不變)
st.set_page_config(page_title="易鏡 - 文青卜卦", layout="wide")

# 2. 你的完整 HTML 程式碼字串 (保持不變)
html_code = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>易鏡</title>
    </body>
</html>
"""

# 3. 【修改這裡】移除原本的 components.html(...)
# 改用新的官方建議語法來渲染 HTML 字串
st.html(html_code)
