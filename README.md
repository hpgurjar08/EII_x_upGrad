# Forge AI 🤖

**Instantly Transform Educational Content into Dynamic Learning Assets.**

Forge AI is an intelligent content repurposing engine designed for the modern educator. By leveraging the power of Google's Gemini API, it takes any piece of educational content—from pasted text to PDF/DOCX documents—and instantly forges it into a suite of ready-to-use learning materials.

---

## 1. Problem Statement

In today's diverse learning landscape, educators, instructional designers, and content creators spend countless hours manually adapting lesson plans for different needs. A single piece of content often needs to be:

* **Summarized** for quick reviews.
* Turned into a **quiz** for knowledge assessment.
* Broken down into **flashcards** for studying.
* **Translated** for a global audience.

This repetitive, time-consuming work is a major pain point that stifles creativity and slows down the pace of educational development.

---

## 2. Our Solution: Forge AI

Forge AI is a web-based tool that automates this entire workflow. It serves as a centralized, AI-powered engine that provides users with the tools they need to repurpose their content with a single click. Our solution is fast, intuitive, and designed to seamlessly integrate into an educator's existing workflow, saving them time and effort.

---

## 3. Key Features

Forge AI is packed with features designed to create a comprehensive set of learning materials from a single source:

* **Multiple Input Sources:**
    * **Pasted Text:** Directly paste any amount of text for processing.
    * **File Uploads:** Upload `.pdf` and `.docx` documents to extract and process text directly from your course materials.

* **AI-Powered Content Generation:**
    * **Intelligent Summarization:** Creates academic-quality summaries that adapt in style to the subject matter.
    * **Dynamic Quiz Generation:** Produces 5-6 multiple-choice questions that test for deep understanding, not just rote memorization.
    * **Instant Flashcard Creation:** Extracts key terms and concepts, formatting them perfectly for study.
    * **Nuanced Translation:** Provides context-aware translations that preserve the tone and meaning of the original text.

* **Polished User Experience:**
    * **Dual Theme:** A beautiful and responsive interface with both Light and Dark modes.
    * **Interactive UI:** Features subtle animations and an interactive cursor glow for a modern feel.
    * **Convenience Tools:** Includes "Copy to Clipboard" and "Download as .txt" buttons for easy sharing and saving of generated content.

---

## 4. Target User & Pain Points

Our primary target users are:

* **Educators & University Professors:**
    * **Pain Point:** Overloaded with administrative work and have limited time to create diverse and engaging study materials for their students.
* **Corporate L&D Specialists:**
    * **Pain Point:** Need to quickly adapt training materials for different departments, formats, and learning styles.
* **Students & Lifelong Learners:**
    * **Pain Point:** Want to quickly process dense information and create their own study aids (summaries, flashcards) from articles, papers, and notes.

---

## 5. Technology Stack

* **Backend:** Python, Flask
* **AI Engine:** Google Gemini Pro API via `google-generativeai`
* **File Processing:** `PyPDF2`, `python-docx`
* **Frontend:** HTML5, CSS3, JavaScript
* **Styling:** Modern CSS with variables, animations, and a responsive grid layout.

---

## 6. Setup & Installation

To run this project locally, follow these steps:

1.  **Prerequisites:**
    * Python 3.8+
    * A code editor like VS Code

2.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd hackathonEII
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    # Create the environment
    python -m venv venv
    # Activate on Windows
    .\venv\Scripts\activate
    # Activate on macOS/Linux
    source venv/bin/activate
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your API Key:**
    * Create a `.env` file in the project root.
    * Add your Gemini API key to it:
        ```
        GOOGLE_API_KEY="your_api_key_here"
        ```

6.  **Run the application:**
    * **Start the Backend:**
        ```bash
        flask --app backend.app run
        ```
    * **Open the Frontend:**
        Navigate to the `frontend/` folder and open the `index.html` file in your web browser.

---

## 7. Plan for Scale (Future Roadmap)

Forge AI has a strong foundation with significant potential for growth:

* **Audio Summaries (Text-to-Speech):** Integrate a TTS engine to provide audio versions of summaries, enhancing accessibility.
* **AI-Generated Mind Maps:** Generate structured data representing the key concepts and visualize it as a mind map using a library like Mermaid.js.
* **Web Page Scraper:** Allow users to input a URL of an article, and have the backend automatically scrape and process its content.
* **User Accounts & History:** Implement a database and user authentication to allow users to save, organize, and revisit their generated content.

---

## 8. Business Model & Monetization

We propose a **Freemium SaaS model** to attract a large user base while creating clear revenue streams.

* **Free Tier:**
    * Allows users to process a limited amount of content per day.
    * Core features like Summarize and Translate are available.
* **Pro Subscription (Monthly/Yearly):**
    * Unlimited content processing.
    * Access to premium features (Quiz, Flashcards, Mind Maps).
    * File uploads of larger sizes.
* **Teams/Enterprise Tier:**
    * B2B licensing for educational institutions and corporate teams.
    * Includes team management, custom branding, and API access.