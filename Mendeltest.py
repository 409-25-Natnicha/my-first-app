import time
import streamlit as st

st.title("📚 Mendel test")

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""

def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False

@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()

    if u_ans1 == "25%" or "25":
        st.success("✅ ข้อ 1: ถูกต้อง เก่งมากจ้า")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ผิดจ้า (คุณตอบ '{u_ans1}')")

    if u_ans2 == "50%" or "50":
        st.success("✅ ข้อ 2: ถูกต้อง เก่งมากจ้า")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ผิดจ้า (คุณตอบ '{u_ans2}')")

    if u_ans3 == "เอนไซม์ตัดจำเพาะ":
        st.success("✅ ข้อ 3: ถูกต้อง เก่งมากจ้า")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ผิดจ้า (คุณตอบ '{u_ans3}')")

    if u_ans4 == "Incomplete dominant" or "incomplete dominant":
        st.success("✅ ข้อ 4: ถูกต้อง เก่งมากจ้า")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ผิดจ้า (คุณตอบ '{u_ans4}')")

    if u_ans4 == "0%" or "0":
        st.success("✅ ข้อ 5: ถูกต้อง เก่งมากจ้า")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ผิดจ้า (คุณตอบ '{u_ans5}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")
    if 0 <= score <= 1:
        st.write(f"**คะแนนที่คุณได้:** {score} / 5 คะแนน")
        st.warning("“💀มันจบละครับนาย” คุณแทบไม่มีความรู้ด้านพันธุศาสตร์เลย แม้แต่เด็ก ป.6 ก็คงตอบได้เยอะกว่าคุณ คุณควรพัฒนาตนเองนะ")

    elif 2 <= score <= 3:
        st.write(f"**คะแนนที่คุณได้:** {score} / 5 คะแนน")
        st.info("“ของเขาดีจริง” คุณมีความรู้เรื่องนี้พอสมควรเลยหละ ดีมาก")

    elif 4 <= score <= 5:
        st.balloons() 
        st.write(f"**คะแนนที่คุณได้:** {score} / 5 คะแนน")
        st.success("“🎉เวรี่กู๊ดด” คุณเก่งเรื่องพันธุศาสตร์มาก")
        
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

timer_placeholder = st.empty()

st.divider()

ans1 = st.text_input(
    "ข้อ 1: ถั่วลันเตาสีเหลือง (Y) เป็นลักษณะเด่นกว่าสีเขียว (y) ถ้าผสม Yy × Yy ลูกจะมีโอกาสเป็นสีเขียวกี่เปอร์เซ็นต์ ?",
    value=st.session_state.ans1_val,
)

ans2 = st.text_input(
    "ข้อ 2: กำหนดให้ต้นสูง (T) เป็นลักษณะเด่น และต้นเตี้ย (t) เป็นลักษณะด้อย ถ้าผสม Tt × tt ลูกจะมีจีโนไทป์และฟีโนไทป์อย่างไร (%) ?",
    value=st.session_state.ans2_val,
)

ans3 = st.text_input(
    "ข้อ 3: ถ้านักวิทยาศาสตร์ต้องการตัด DNA บริเวณที่กำหนดอย่างจำเพาะ สามารถใช้เทคโนโลยีใด ? ",
    value=st.session_state.ans3_val,
)

ans4 = st.text_input(
    "ข้อ 4: การผสม รุ่น P ที่มีดอกสีแดงและสีขาวได้รุ่นลูก F1 ดอกสีชมพูทั้งหมด การถ่ายทอดลักษณะทางพันธุกรรมนี้คืออะไร ?",
    value=st.session_state.ans4_val,
)

ans5 = st.text_input(
    "ข้อ 5: หากพ่อมีหมู่เลือด A ซึ่งแม่ของพ่อหมู่เลือด O และแม่มีหมู่เลือด B ลูกที่เกิดมามีโอกาสเป็นหมู่เลือด O กี่เปอร์เซ็นต์ ?",
    value=st.session_state.ans5_val,
)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(90 - (time.time() - st.session_state.start))
    if time_left > 0:
        timer_placeholder.error(f"⏳ เหลือเวลา: {time_left} วินาที")
        time.sleep(1)
        st.rerun()
    else:
        st.session_state.is_ended = True
        st.rerun()

if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5)
