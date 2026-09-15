import streamlit as st

# ตั้งค่าหน้าเว็บเป็นแบบ Wide (ขยายเต็มจอ)
st.set_page_config(page_title="Mendle Test", layout="wide")

# --- CSS ปรับแต่ง UI ให้ตรงตามดีไซน์ ---
st.markdown("""
    <style>
    /* ซ่อน Header และ Footer หลักของ Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* ตกแต่งปุ่มช้อยส์ */
    div.stButton > button {
        width: 100%;
        height: 50px;
        font-size: 18px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# --- แบ่ง Layout เป็น 2 ฝั่ง (ซ้าย: นิ่ง / ขวา: Scroll ตามหน้าเว็บ) ---
left_col, right_col = st.columns([1, 2.5], gap="large")

# ==================== ฝั่งซ้าย (Sidebar/Fixed Control) ====================
with left_col:
    st.title("หน้า UI")
    
    # ส่วนเลือกระดับความยาก
    st.subheader("ความยาก")
    difficulty = st.radio(
        label="เลือกระดับชั้น",
        options=["ประถม", "มัธยม", "มหาลัย"],
        label_visibility="collapsed"
    )
    
    st.write("---")
    
    # แสดงรูป / GIF ฝั่งซ้าย
    st.caption("รูป / GIF")
    # สามารถเปลี่ยนเป็น st.image("path_to_gif.gif") ได้
    st.image("https://via.placeholder.com/300x250.png?text=Image+/+GIF", use_column_width=True)


# ==================== ฝั่งขวา (Scrollable Question Area) ====================
with right_col:
    st.title("Mendle test")
    
    # ----- ข้อที่ 1 -----
    st.markdown("### 1. คำถามข้อที่ 1")
    
    # แสดงรูปภาพของคำถามที่ 1
    st.image("https://via.placeholder.com/600x250.png?text=รูปภาพคำถาม+ข้อ+1", use_column_width=True)
    
    # ปุ่มกด 4 ช้อยส์ (จัดเป็น 2 คอลัมน์ x 2 แถว)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ชั้น 1", key="q1_opt1"):
            st.success("คุณเลือก ชั้น 1")
    with col2:
        if st.button("ชั้น 2", key="q1_opt2"):
            st.success("คุณเลือก ชั้น 2")
            
    col3, col4 = st.columns(2)
    with col3:
        if st.button("ชั้น 3", key="q1_opt3"):
            st.success("คุณเลือก ชั้น 3")
    with col4:
        if st.button("ชั้น 4", key="q1_opt4"):
            st.success("คุณเลือก ชั้น 4")

    st.write("---")

    # ----- ข้อที่ 2 -----
    st.markdown("### 2. คำถามข้อที่ 2")
    
    # แสดงรูปภาพของคำถามที่ 2
    st.image("https://via.placeholder.com/600x250.png?text=รูปภาพคำถาม+ข้อ+2", use_column_width=True)
    
    # ปุ่มกด 4 ช้อยส์
    col5, col6 = st.columns(2)
    with col5:
        if st.button("ชั้น 1", key="q2_opt1"):
            st.success("คุณเลือก ชั้น 1")
    with col6:
        if st.button("ชั้น 2", key="q2_opt2"):
            st.success("คุณเลือก ชั้น 2")
            
    col7, col8 = st.columns(2)
    with col7:
        if st.button("ชั้น 3", key="q2_opt3"):
            st.success("คุณเลือก ชั้น 3")
    with col8:
        if st.button("ชั้น 4", key="q2_opt4"):
            st.success("คุณเลือก ชั้น 4")
