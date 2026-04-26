import streamlit as st
import streamlit.components.v1 as components

# 1. 設定頁面為寬版，讓視覺更開闊
st.set_page_config(page_title="易鏡 - 文青卜卦", layout="wide")

# 2. 讀取同一目錄下的 iching.html 檔案
try:
    with open("iching.html", "r", encoding="utf-8") as f:
        html_data = f.read()

    # 3. 透過 components.html 渲染
    # 這裡必須使用 components.html 才能確保 3D 骰子與 JavaScript 動畫不被阻擋
    components.html(html_data, height=1200, scrolling=True)

except FileNotFoundError:
    st.error("找不到 iching.html 檔案，請確認檔案是否有上傳成功。")
