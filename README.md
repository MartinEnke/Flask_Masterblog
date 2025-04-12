# The Quiet Almanac

*A minimalist, local blog built with Flask — a space to write, reflect, and quietly archive the miraculous ordinary.*

![Banner](static/images/almanac.png)

---

## ✨ Features

- 🖊 **Add Posts** — with title, author, content, and automatic date  
- 🛠 **Edit & Update** — including a visible "last updated" timestamp  
- ❤️ **Like System** — likes update in real-time (AJAX) without page reload  
- 🔍 **Post Filters** — sort by **Newest**, **Oldest**, or **Most Liked**  
- 🧭 **Clean Layout** — styled interface with subtle effects & responsive grid  
- 🗂 **JSON-based storage** — no database needed

---

## 🚀 Quick Start

### 1. Clone the repository

git clone https://github.com/your-username/quiet-almanac.git

cd quiet-almanac


### 2. Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Flask
pip install flask

Then visit http://localhost:5016 in your browser ✨


🧱 Project Structure
quiet-almanac/
├── app.py                 # Main Flask application
├── blog_posts.json        # Local data store
├── static/
│   ├── css/style.css      # Main styling
│   └── images/            # Banner/logo graphics
└── templates/
    ├── index.html         # Homepage
    ├── show.html          # Post list + filters
    ├── add.html           # Add new post
    └── update.html        # Edit existing post



 ### Ideas for Future Features

👤 User login / authentication

🌙 Dark mode toggle

🗂 Categories / tags

🔎 Search functionality

☁️ Switch to SQLite or cloud database

✉️ Contact or submission form


📜 License
This project is open source and available under the MIT License.


Created by Martin Enke, 2025