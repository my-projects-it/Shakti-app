import streamlit as st
import pandas as pd
import os
from datetime import datetime
import speech_recognition as sr
from pydub import AudioSegment
import tempfile

# ========== Page Config ==========
st.set_page_config(
    page_title="Meri Kahaani Zinda Hai",
    page_icon="📖",
    layout="centered"
)

# ========== CSV File Setup ==========
CSV_FILE = "anonymous_stories.csv"

def save_story(text):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "story": text.strip()
    }
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    else:
        df = pd.DataFrame([entry])
    df.to_csv(CSV_FILE, index=False)

# ========== Audio Conversion ==========
def convert_to_wav(uploaded_file):
    audio_format = uploaded_file.type.split("/")[-1]
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix="." + audio_format)
    temp_input.write(uploaded_file.read())
    temp_input.flush()

    audio = AudioSegment.from_file(temp_input.name)
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio.export(temp_wav.name, format="wav")
    return temp_wav.name

# ========== Audio Transcription ==========
def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data, language="hi-IN")

# ========== Language Selection ==========
language = st.selectbox("🌐 Choose Language / भाषा चुनें", ["English", "Hindi", "Tamil", "Bengali"])

translations = {
    "English": {
        "title": "Meri Kahaani Zinda Hai",
        "subtitle": "Your story is still alive",
        "upload_audio": "Upload your voice (MP3, WAV, M4A)",
        "write_story": "Write your story",
        "submit": "Submit",
        "success": "Your story has been saved. Thank you!",
        "error": "Please do not submit an empty story.",
        "transcribed": "Transcribed Text (editable):"
    },
    "Hindi": {
        "title": "मेरी कहानी ज़िंदा है",
        "subtitle": "हर आवाज़ अब साँस ले रही है",
        "upload_audio": "अपनी आवाज़ अपलोड करें (MP3, WAV, M4A)",
        "write_story": "अपनी कहानी लिखें",
        "submit": "सबमिट करें",
        "success": "आपकी कहानी सेव हो गई है। धन्यवाद!",
        "error": "कृपया खाली कहानी सबमिट न करें।",
        "transcribed": "बदला गया टेक्स्ट (संपादन करें):"
    },
    "Tamil": {
        "title": "என் கதை உயிருடன் உள்ளது",
        "subtitle": "உங்கள் கதை இன்னும் உயிருடன் உள்ளது",
        "upload_audio": "உங்கள் குரலை பதிவேற்றவும் (MP3, WAV, M4A)",
        "write_story": "உங்கள் கதையை எழுதுங்கள்",
        "submit": "சமர்ப்பிக்கவும்",
        "success": "உங்கள் கதை சேமிக்கப்பட்டது. நன்றி!",
        "error": "காலியான கதையை சமர்ப்பிக்க வேண்டாம்.",
        "transcribed": "மாற்றிய உரை (திருத்தக்கூடியது):"
    },
    "Bengali": {
        "title": "আমার গল্প এখনও বেঁচে আছে",
        "subtitle": "আপনার কণ্ঠ এখনো জীবিত",
        "upload_audio": "আপনার কণ্ঠ আপলোড করুন (MP3, WAV, M4A)",
        "write_story": "আপনার গল্প লিখুন",
        "submit": "জমা দিন",
        "success": "আপনার গল্প সংরক্ষিত হয়েছে। ধন্যবাদ!",
        "error": "অনুগ্রহ করে খালি গল্প জমা দেবেন না।",
        "transcribed": "লিপ্যন্তরিত পাঠ্য (সম্পাদনাযোগ্য):"
    }
}

T = translations[language]

# ========== Header ==========
st.markdown(f"""
    <div style='text-align: center; padding: 10px;'>
        <h1 style='color:#4a2c2a;'>📖 {T['title']}</h1>
        <h4 style='color:#555;'>{T['subtitle']}</h4>
    </div>
""", unsafe_allow_html=True)
st.markdown("---")

# ========== Audio Upload ==========
st.subheader("🎙️ " + T['upload_audio'])
uploaded_audio = st.file_uploader(label="", type=["mp3", "wav", "m4a", "ogg"])

story = ""

if uploaded_audio:
    st.info("⏳ Transcribing audio...")
    try:
        wav_path = convert_to_wav(uploaded_audio)
        text = transcribe_audio(wav_path)
        st.success("✅ Transcription successful!")
        story = st.text_area(T["transcribed"], value=text, height=200)
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
        story = ""

# ========== Text Area ==========
st.subheader("✍️ " + T['write_story'])
story_text = st.text_area(label="", value="", height=300)

if not story and story_text:
    story = story_text

# ========== Submit Button ==========
if st.button("📤 " + T['submit']):
    if story.strip():
        save_story(story)
        st.success("✅ " + T['success'])
    else:
        st.warning("⚠️ " + T['error'])

st.markdown("---")
st.caption("📜 हर शब्द मेरा है, हर लाइन मेरा सच — मेरी कहानी ज़िंदा है।")

