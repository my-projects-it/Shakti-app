import streamlit as st
import pandas as pd
import os
from datetime import datetime
import speech_recognition as sr
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
import tempfile
import uuid

# Initialize session state variables
if "stories" not in st.session_state:
    st.session_state.stories = []
if "comments" not in st.session_state:
    st.session_state.comments = {}
if "story_input" not in st.session_state:
    st.session_state.story_input = ""
if "tags_input" not in st.session_state:
    st.session_state.tags_input = ""
if "theme" not in st.session_state:
    st.session_state.theme = "dark"
if "comment_inputs" not in st.session_state:
    st.session_state.comment_inputs = {}
if "audio_processed" not in st.session_state:
    st.session_state.audio_processed = False

# ========== Theme Setup ==========
def set_theme(theme):
    if theme == "dark":
        st.markdown("""
        <style>
            .stApp {
                background-color: #0E1117;
                color: white;
            }
            .stTextArea>div>div>textarea, .stTextInput>div>div>input {
                background-color: #262730;
                color: white;
            }
            h1, h2, h3, h4, h5, h6, p, div, span {
                color: white !important;
            }
        </style>
        """, unsafe_allow_html=True)
    else:  # black mode
        st.markdown("""
        <style>
            .stApp {
                background-color: #000000;
                color: white;
            }
            .stTextArea>div>div>textarea, .stTextInput>div>div>input {
                background-color: #1A1A1A;
                color: white;
            }
            h1, h2, h3, h4, h5, h6, p, div, span {
                color: white !important;
            }
        </style>
        """, unsafe_allow_html=True)

# ========== Page Config ==========
st.set_page_config(
    page_title="Shakti",
    page_icon="📖",
    layout="centered"
)

# ========== Theme Selector ==========
theme_col1, theme_col2 = st.columns([3, 1])
with theme_col2:
    theme = st.selectbox(
        "Theme",
        ["Dark", "Black"],
        index=["Dark", "Black"].index(st.session_state.theme.capitalize()),
        key="theme_select"
    )
    st.session_state.theme = theme.lower()
    set_theme(st.session_state.theme)

# ========== CSV File Setup ==========
CSV_FILE = "anonymous_stories.csv"

def save_story(text, tags):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "story": text.strip(),
        "tags": ",".join(tags)
    }
    try:
        if os.path.exists(CSV_FILE):
            df = pd.read_csv(CSV_FILE)
            df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
        else:
            df = pd.DataFrame([entry])
        df.to_csv(CSV_FILE, index=False)
    except Exception as e:
        st.error(f"Failed to save story: {e}")

def load_stories_from_csv():
    if os.path.exists(CSV_FILE):
        try:
            df = pd.read_csv(CSV_FILE)
            stories = []
            for _, row in df.iterrows():
                tags = []
                if "tags" in row and pd.notna(row["tags"]):
                    tags = [tag.strip() for tag in row["tags"].split(",") if tag.strip()]
                stories.append({
                    "id": str(uuid.uuid4()),
                    "text": row["story"],
                    "tags": tags
                })
            return stories
        except Exception as e:
            st.error(f"Failed to load stories: {e}")
            return []
    return []

if not st.session_state.stories:
    st.session_state.stories = load_stories_from_csv()

# ========== Audio Handling ==========
def handle_audio_file(uploaded_file):
    try:
        # Create temp file with correct extension
        audio_format = uploaded_file.type.split("/")[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{audio_format}") as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name
        
        # Convert to WAV if needed
        if audio_format != "wav":
            audio = AudioSegment.from_file(tmp_path)
            wav_path = tmp_path + ".wav"
            audio.export(wav_path, format="wav")
            os.remove(tmp_path)
            return wav_path
        return tmp_path
        
    except CouldntDecodeError:
        st.error("❌ Unsupported audio format. Please upload MP3 or WAV.")
        return None
    except Exception as e:
        st.error(f"❌ Error processing audio: {str(e)}")
        return None

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="hi-IN")
            return text
    except sr.UnknownValueError:
        st.error("🔇 Could not understand audio - poor quality or wrong language")
        return None
    except sr.RequestError:
        st.error("🌐 Network error - please check your connection")
        return None
    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)

# ========== Language Selection ==========
language = st.selectbox("🌐 Choose Language / भाषा चुनें", ["English", "Hindi", "Tamil", "Bengali"])

translations = {
    "English": {
        "title": "Shakti",
        "subtitle": "Your story is still alive",
        "upload_audio": "Upload your voice (MP3, WAV)",
        "write_story": "Write your story",
        "submit": "Submit",
        "success": "Your story has been saved. Thank you!",
        "error": "Please do not submit an empty story.",
        "transcribed": "Transcribed Text (editable):",
        "add_tags": "Add tags (e.g., #domesticviolence, #healingjourney)",
        "enter_tags": "Enter tags separated by commas:",
        "comment_placeholder": "Add a comment to this story:",
        "post_comment": "Post Comment",
        "comment_empty": "Comment cannot be empty.",
        "comment_posted": "Comment posted!",
        "no_stories": "No stories yet. Submit one above to start the conversation."
    },
    "Hindi": {
        "title": "Shakti",
        "subtitle": "हर आवाज़ अब साँस ले रही है",
        "upload_audio": "अपनी आवाज़ अपलोड करें (MP3, WAV)",
        "write_story": "अपनी कहानी लिखें",
        "submit": "सबमिट करें",
        "success": "आपकी कहानी सेव हो गई है। धन्यवाद!",
        "error": "कृपया खाली कहानी सबमिट न करें।",
        "transcribed": "बदला गया टेक्स्ट (संपादन करें):",
        "add_tags": "टैग जोड़ें (जैसे, #domesticviolence, #healingjourney)",
        "enter_tags": "कॉमा से टैग दर्ज करें:",
        "comment_placeholder": "इस कहानी पर टिप्पणी जोड़ें:",
        "post_comment": "टिप्पणी भेजें",
        "comment_empty": "टिप्पणी खाली नहीं हो सकती।",
        "comment_posted": "टिप्पणी भेजी गई!",
        "no_stories": "कोई कहानी नहीं है। ऊपर एक सबमिट करें।"
    },
    "Tamil": {
        "title": "என் கதை உயிருடன் உள்ளது",
        "subtitle": "உங்கள் கதை இன்னும் உயிருடன் உள்ளது",
        "upload_audio": "உங்கள் குரலை பதிவேற்றவும் (MP3, WAV)",
        "write_story": "உங்கள் கதையை எழுதுங்கள்",
        "submit": "சமர்ப்பிக்கவும்",
        "success": "உங்கள் கதை சேமிக்கப்பட்டது. நன்றி!",
        "error": "காலியான கதையை சமர்ப்பிக்க வேண்டாம்.",
        "transcribed": "மாற்றிய உரை (திருத்தக்கூடியது):",
        "add_tags": "டேக்கள் சேர்க்கவும் (எ.கா., #domesticviolence, #healingjourney)",
        "enter_tags": "டேக்களை கமாஸ் கொண்டு பிரித்து உள்ளிடவும்:",
        "comment_placeholder": "இந்த கதைக்கு கருத்து சேர்:",
        "post_comment": "கருத்து பதிவிடு",
        "comment_empty": "கருத்து காலியானதாக இருக்க முடியாது.",
        "comment_posted": "கருத்து பதிவிடப்பட்டது!",
        "no_stories": "கதைகள் இல்லை. மேலே ஒரு கதையை சமர்ப்பிக்கவும்."
    },
    "Bengali": {
        "title": "আমার গল্প এখনও বেঁচে আছে",
        "subtitle": "আপনার কণ্ঠ এখনো জীবিত",
        "upload_audio": "আপনার কণ্ঠ আপলোড করুন (MP3, WAV)",
        "write_story": "আপনার গল্প লিখুন",
        "submit": "জমা দিন",
        "success": "আপনার গল্প সংরক্ষিত হয়েছে। ধন্যবাদ!",
        "error": "অনুগ্রহ করে খালি গল্প জমা দেবেন না।",
        "transcribed": "লিপ্যন্তরিত পাঠ্য (সম্পাদনাযোগ্য):",
        "add_tags": "ট্যাগ যোগ করুন (যেমন, #domesticviolence, #healingjourney)",
        "enter_tags": "কমা দিয়ে ট্যাগ লিখুন:",
        "comment_placeholder": "এই গল্পে মন্তব্য যোগ করুন:",
        "post_comment": "মন্তব্য পোস্ট করুন",
        "comment_empty": "মন্তব্য খালি হতে পারে না।",
        "comment_posted": "মন্তব্য পোস্ট হয়েছে!",
        "no_stories": "কোনো গল্প নেই। উপরে একটি জমা দিন।"
    }
}

T = translations.get(language, translations["English"])

# ========== Submission Handler ==========
def handle_submission():
    tags = [tag.strip().lower() for tag in st.session_state.tags_input.split(",") if tag.strip()]

    if st.session_state.story_input.strip():
        save_story(st.session_state.story_input, tags)

        story_id = str(uuid.uuid4())
        st.session_state.stories.append({
            "id": story_id, 
            "text": st.session_state.story_input.strip(), 
            "tags": tags
        })
        st.session_state.comments[story_id] = []
        
        # Clear inputs
        st.session_state.story_input = ""
        st.session_state.tags_input = ""
        st.session_state.audio_processed = False  # Reset audio processing flag
        st.session_state.submission_success = True  # Flag for successful submission
    else:
        st.session_state.submission_error = True  # Flag for error

def handle_comment(story_id):
    comment_key = f"comment_input_{story_id}"
    if comment_key in st.session_state:
        comment = st.session_state[comment_key]
        if comment.strip():
            if story_id not in st.session_state.comments:
                st.session_state.comments[story_id] = []
            st.session_state.comments[story_id].append(comment.strip())
            st.session_state[comment_key] = ""  # Clear the comment input
            st.session_state.comment_posted = story_id  # Flag which comment was posted
        else:
            st.session_state.comment_empty = story_id  # Flag which comment was empty

# ========== UI Components ==========
st.markdown(f"""
    <div style='text-align: center; padding: 10px;'>
        <h1 style='color:white;'>📖 {T['title']}</h1>
        <h4 style='color:#DDD;'>{T['subtitle']}</h4>
    </div>
""", unsafe_allow_html=True)
st.markdown("---")

# Audio Upload Section - Only process if new audio is uploaded
uploaded_audio = None
if not st.session_state.audio_processed:
    st.subheader("🎙️ " + T['upload_audio'])
    uploaded_audio = st.file_uploader(
        label=T['upload_audio'], 
        type=["mp3", "wav"],
        key="audio_uploader"
    )

if uploaded_audio and not st.session_state.audio_processed:
    with st.spinner("🔊 Processing audio..."):
        audio_path = handle_audio_file(uploaded_audio)
        if audio_path:
            text = transcribe_audio(audio_path)
            if text:
                st.session_state.story_input = text
                st.session_state.audio_processed = True  # Mark audio as processed
                st.success("✅ Transcription complete!")

# Story Input Section
story_label = T['transcribed'] if st.session_state.story_input else T['write_story']
st.subheader("✍️ " + story_label)
st.text_area(
    label="", 
    height=300, 
    key="story_input",
    value=st.session_state.story_input
)

# Tags Input
st.subheader("🏷️ " + T["add_tags"])
st.text_input(
    T["enter_tags"], 
    key="tags_input",
    value=st.session_state.tags_input
)

# Submit Button
if st.button("📤 " + T['submit'], on_click=handle_submission):
    pass  # The actual handling is done in the callback

# Show submission messages if they exist
if hasattr(st.session_state, 'submission_success') and st.session_state.submission_success:
    st.success("✅ " + T['success'])
    del st.session_state.submission_success  # Clear the flag

if hasattr(st.session_state, 'submission_error') and st.session_state.submission_error:
    st.warning("⚠️ " + T['error'])
    del st.session_state.submission_error  # Clear the flag

st.markdown("---")

# Community Stories Section
st.header("📚 Community Stories")

if not st.session_state.stories:
    st.info(T["no_stories"])
else:
    for story_obj in reversed(st.session_state.stories):
        st.markdown(f"### 🗣️ {story_obj['text']}")
        if story_obj.get("tags"):
            tags_display = " ".join([f"`#{tag}`" for tag in story_obj["tags"]])
            st.markdown(f"**Tags:** {tags_display}")

        # Comment Section
        with st.form(key=f"comment_form_{story_obj['id']}"):
            # Create a unique key for each comment input
            comment_key = f"comment_input_{story_obj['id']}"
            
            # Initialize if not exists
            if comment_key not in st.session_state:
                st.session_state[comment_key] = ""
                
            comment_input = st.text_input(
                "💬 " + T["comment_placeholder"],
                key=comment_key,
                value=st.session_state[comment_key]
            )
            
            # Submit button with callback
            submitted = st.form_submit_button(
                T["post_comment"],
                on_click=handle_comment,
                args=(story_obj['id'],)
            )

        # Show comment messages if they exist for this story
        if hasattr(st.session_state, 'comment_posted') and st.session_state.comment_posted == story_obj['id']:
            st.success("💬 " + T["comment_posted"])
            del st.session_state.comment_posted  # Clear the flag
            
        if hasattr(st.session_state, 'comment_empty') and st.session_state.comment_empty == story_obj['id']:
            st.warning("⚠️ " + T["comment_empty"])
            del st.session_state.comment_empty  # Clear the flag

        # Display Comments
        comments = st.session_state.comments.get(story_obj['id'], [])
        if comments:
            st.markdown("**🧵 Comments:**")
            for c in comments:
                st.markdown(f"- {c}")

        st.markdown("---")