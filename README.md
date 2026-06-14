# Attendexa
 
**Attendexa** is an AI-powered smart attendance system built with Streamlit. It uses face recognition to mark student attendance from classroom photos, with an optional voice-based attendance mode, and gives teachers a clean dashboard to manage subjects, enrollments, and attendance records.
 
---
 
## ✨ Features
 
- **AI Face Recognition Attendance** — Upload classroom photos and let the system automatically detect and mark enrolled students as present.
- **Voice Attendance** — Alternative attendance mode using voice recognition (powered by `librosa` and `resemblyzer`).
- **Teacher Dashboard** — Manage subjects, view enrolled students, and review attendance history.
- **Student Enrollment** — Students join subjects via shareable join codes or QR codes — no manual sign-up forms.
- **Attendance Records** — View attendance summaries grouped by session, subject, and date.
- **Supabase Backend** — All data (teachers, students, subjects, enrollments, attendance logs) is stored in Supabase (PostgreSQL).
---
 
## 🛠 Tech Stack
 
| Layer | Technology |
|---|---|
| Frontend / UI | [Streamlit](https://streamlit.io) |
| Database | [Supabase](https://supabase.com) (PostgreSQL) |
| Face Recognition | `face_recognition`, `dlib` |
| Voice Recognition | `librosa`, `resemblyzer`, `torch` |
| Data Handling | `pandas`, `numpy` |
| QR Codes | `segno` |
 
---
 
## 📂 Project Structure
 
```
attendexa/
├── app.py                          # App entry point
├── requirements.txt
├── .streamlit/
│   └── secrets.toml                # Supabase credentials (not committed)
├── src/
│   ├── components/                 # Reusable UI components & dialogs
│   │   ├── header.py
│   │   ├── footer.py
│   │   ├── subject_card.py
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_add_photo.py
│   │   ├── dialog_share_subject.py
│   │   ├── dialog_attendance_results.py
│   │   ├── dialog_voice_attendance.py
│   │   └── dialog_auto_enroll.py
│   ├── database/
│   │   ├── config.py               # Supabase client setup
│   │   └── db.py                   # Database queries
│   ├── pipelines/
│   │   ├── face_pipeline.py        # Face detection & recognition logic
│   │   └── voice_pipeline.py       # Voice recognition logic
│   ├── screens/
│   │   ├── home_screen.py
│   │   ├── teacher_screen.py
│   │   └── student_screen.py
│   ├── ui/
│   │   └── base_layout.py          # Theming & layout styles
│   └── logo/
│       ├── attendexa_icon.png
│       └── attendexa_icon.svg
```
 
---
 
## 🚀 Getting Started
 
### 1. Clone the repository
```bash
git clone https://github.com/kadekarunakar/Attendexa.git
cd Attendexa
```
 
### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```
 
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
 
### 4. Configure Supabase secrets
Create a `.streamlit/secrets.toml` file in the project root:
```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"
```
 
### 5. Run the app
```bash
streamlit run app.py
```
 
---
 
## ☁️ Deploying to Streamlit Cloud
 
1. Push your repository to GitHub (make sure `.streamlit/secrets.toml` and `venv/` are in `.gitignore`).
2. Create a new app on [Streamlit Cloud](https://share.streamlit.io) and point it to `app.py`.
3. In your app's **Settings → Secrets**, add the same keys from `secrets.toml`:
```toml
   SUPABASE_URL = "your-supabase-url"
   SUPABASE_KEY = "your-supabase-key"
```
4. Save — the app will rebuild and connect to Supabase automatically.
---
 
## 🎨 Branding
 
Attendexa uses a teal (`#14B8A6`), pink (`#F472B6`), and navy (`#0F172A`) color palette, with **Space Grotesk** for headings and **Outfit** for body text.
 
 
