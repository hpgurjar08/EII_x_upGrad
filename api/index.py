from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from backend.services.gemini_service import generate_content_from_gemini
from backend.services.file_parser import extract_text_from_pdf, extract_text_from_docx

app = Flask(__name__)
CORS(app)

def get_content_from_request():
    """Processes the request to get text from the JSON body."""
    data = request.get_json()
    if not data or 'text' not in data or not data['text']:
        abort(400, description="Invalid input. Please provide text in the request body.")
    return data['text']

@app.route("/api")
def index():
    return jsonify(status="success", message="Welcome to the Kerna AI API!")

@app.route("/upload", methods=['POST'])
def upload_file():
    """Handles PDF and DOCX file uploads and extracts text."""
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify(error="No selected file"), 400

    if file:
        filename = file.filename
        text = ""
        if filename.endswith('.pdf'):
            text = extract_text_from_pdf(file)
        elif filename.endswith('.docx'):
            text = extract_text_from_docx(file)
        else:
            return jsonify(error="Unsupported file type. Please upload a PDF or DOCX."), 400
        
        if text.startswith("Error:"):
            return jsonify(error=text), 500

        return jsonify(extracted_text=text)

@app.route("/api/summarize", methods=['POST'])
def summarize_content():
    content_to_process = get_content_from_request()
    summary_prompt = """
    You are an expert multidisciplinary academic researcher. Your task is to analyze the provided text and generate a specialized summary tailored to its subject matter.
    **Step 1: Deep Analysis & Classification**
    Silently analyze the text to determine its primary domain (e.g., Mathematics, Natural Science, Philosophy, History, General Factual Information).
    **Step 2: Adopt a Summarization Persona & Style**
    Based on the domain, adopt the corresponding style:
    - **If Mathematics/Logic:** Summarize with a focus on logical structure, axioms, and deductive reasoning.
    - **If Science/Philosophy:** Summarize from a research-oriented perspective, focusing on the core thesis, evidence, and implications.
    - **If History/Social Sciences:** Summarize by highlighting key events, causal relationships, and historical context.
    - **If General Factual text:** Summarize with high confidence and clarity, like an encyclopedia entry.
    **Step 3: Generate the Summary**
    Now, generate the final summary. It must be concise, intellectually deep, and perfectly aligned with the persona you have adopted. Do not state the domain you chose; let the style of your summary reflect your analysis.
    """
    summary_result = generate_content_from_gemini(prompt=summary_prompt, original_text=content_to_process)
    return jsonify(result=summary_result)

@app.route("/translate", methods=['POST'])
def translate_content():
    language = request.args.get('language', 'Hindi') 
    content_to_process = get_content_from_request()
    translation_prompt = f"""
    You are an expert linguist and professional translator. Your task is to provide a high-quality, nuanced translation of the provided text into {language}.
    **Step 1: Analyze Context and Tone**
    Silently analyze the source text to identify its domain (e.g., technical, literary, conversational) and tone (e.g., formal, informal).
    **Step 2: Prioritize Meaning and Nuance**
    Your primary goal is to convey the original meaning and intent naturally. Do not perform a rigid, word-for-word translation. For idioms or cultural phrases, find the closest natural-sounding equivalent in {language}.
    **Step 3: Maintain Register and Accuracy**
    Preserve the original text's register. Pay special attention to technical terms, ensuring they are translated with the highest accuracy.
    **Step 4: Generate the Translation**
    Provide the final, polished translation. It should read as if originally written by a native speaker of {language}.
    """
    translation_result = generate_content_from_gemini(prompt=translation_prompt, original_text=content_to_process)
    return jsonify(result=translation_result)

@app.route("/generate-quiz", methods=['POST'])
def create_quiz():
    content_to_process = get_content_from_request()
    quiz_prompt = """
    You are an expert instructional designer. Your goal is to create a comprehensive quiz of 5 to 6 questions that assesses a learner's depth and clarity of understanding, moving beyond simple rote memorization.
    **Step 1: Identify Core Learning Objectives**
    Silently identify the 5-6 most critical learning objectives from the text.
    **Step 2: Design Application-Based Questions**
    Design 5 to 6 multiple-choice questions that test the application or analysis of concepts. Each question must have one correct answer and three plausible but incorrect "distractor" options representing common misconceptions. Vary the difficulty.
    **Step 3: Structure the Output**
    Format the output as a clean, numbered list. For each question, list the question, the four options (A, B, C, D), and clearly indicate the correct answer.
    """
    quiz_result = generate_content_from_gemini(prompt=quiz_prompt, original_text=content_to_process)
    return jsonify(result=quiz_result)

@app.route("/generate-flashcards", methods=['POST'])
def create_flashcards():
    content_to_process = get_content_from_request()
    flashcard_prompt = """
    You are a learning science expert. Your task is to extract the most critical concepts from the text and structure them as a set of effective flashcards for studying.
    **Step 1: Isolate Core Concepts**
    Silently identify the most important, standalone concepts (key terms, principles, definitions).
    **Step 2: Create "Front" and "Back" of Cards**
    For each concept, create a "Front" (the term or a question) and a "Back" (the concise definition or answer).
    **Step 3: Format the Output**
    Present the final list of flashcards using the strict format:
    Front: [Term or Question]
    Back: [Definition or Answer]
    ---
    (Repeat for all concepts)
    """
    flashcard_result = generate_content_from_gemini(prompt=flashcard_prompt, original_text=content_to_process)
    return jsonify(result=flashcard_result)
