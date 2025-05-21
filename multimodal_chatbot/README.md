### MP4 - multimodal chatbot

Created by Group 4 – Alberte & Felicia
We used pair programming to create this project. Felicia wrote the code while Alberte contributed through discussion and review.

Github Link: https://github.com/FeliciaFavrholdt/DAT-BI-MP4

This project is a multimodal chatbot application built with Streamlit, supporting conversational interaction with various content types:

- PDF documents

- Text files (.txt, .docx)

- CSV data

- Images (.jpg, .png)

- Web pages via URL

It uses Retrieval-Augmented Generation (RAG) and local LLMs via Ollama, enabling private, offline document analysis and Q&A.

### Features
- Clean, modern multi-page UI with separate upload interfaces

- Support for uploading and indexing multiple files at once

- #### Local LLMs:
- phi: fast, efficient for text

- llava: for image understanding

Persistent vector storage using Chroma

Easy reset of all stored data

Modular, scalable code using reusable functions

Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/multimodal-chatbot.git
cd multimodal-chatbot
2. Create and Activate Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate         # macOS/Linux
venv\Scripts\activate            # Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Install Poppler (for PDF support)
macOS: brew install poppler

Ubuntu: sudo apt-get install poppler-utils

Windows: Download poppler and add to PATH

5. Pull Required LLMs
Make sure Ollama is installed and running, then:

bash
Copy code
ollama pull phi
ollama pull llava
Run the Application
bash
Copy code
streamlit run app.py
Use the sidebar to select upload pages.

Folder Structure
kotlin
Copy code
multimodal_chatbot/
├── app.py
├── utils.py
├── requirements.txt
├── README.md
├── data/
├── media/
├── vector_store/
└── pages/
    ├── 1_Upload_PDF.py
    ├── 2_Upload_Image.py
    ├── 3_Upload_Text.py
    ├── 4_Upload_CSV.py
    └── 5_Web_URL.py
License
This project is for academic and educational use. Feel free to adapt it.

