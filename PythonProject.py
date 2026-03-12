import streamlit as st

# 1. Our Data Store (Dictionary)
# You can expand this with more verses later!
shloka_db = {
    "stress": {
        "verse": "योगस्थः कुरु कर्माणि सङ्गं त्यक्त्वा धनञ्जय।",
        "meaning": "Perform your duty equipoised, O Arjuna, abandoning all attachment to success or failure."
    },
    "fear": {
        "verse": "भयसाधनानि न सन्ति, आत्मनः शक्तिरेव सर्वम्।",
        "meaning": "There are no tools for fear; only your own inner strength is everything."
    },
    "confusion": {
        "verse": "यदा यदा हि धर्मस्य ग्लानिर्भवति भारत।",
        "meaning": "Whenever there is a decline in righteousness, I manifest myself."
    }
}

# 2. UI Layout
st.set_page_config(page_title="Divine-Guide", page_icon="🕉️")
st.title("🕉️ Divine Guide")
st.subheader("Find wisdom for your modern-day challenges.")

# 3. User Input
mood = st.selectbox("How are you feeling today?", ["Select an option", "stress", "fear", "confusion"])

# 4. Logic to display result
if mood != "Select an option":
    data = shloka_db.get(mood.lower())
    
    st.write("---")
    st.markdown(f"### ✨ Wisdom for {mood.capitalize()}:")
    st.info(data['verse'])
    st.write(f"**Meaning:** {data['meaning']}")
    
    # Simple feature: Audio-like experience
    if st.button("Listen to the essence"):
        st.success("Imagine the calming sound of Sanskrit chants... (Integration pending!)")