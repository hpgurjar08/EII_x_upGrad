document.addEventListener("DOMContentLoaded", () => {
    
    // THEME SWITCHER LOGIC 
    const themeToggle = document.getElementById("theme-toggle");
    const body = document.body;
    const applyTheme = (theme) => {
        body.classList.toggle('dark-mode', theme === 'dark');
        themeToggle.checked = theme === 'dark';
    };
    const savedTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    applyTheme(savedTheme);
    themeToggle.addEventListener("change", () => {
        const newTheme = themeToggle.checked ? 'dark' : 'light';
        localStorage.setItem('theme', newTheme);
        applyTheme(newTheme);
    });

    // INTERACTIVE CURSOR GLOW LOGIC 
    const cursorGlow = document.getElementById('cursor-glow');
    window.addEventListener('mousemove', (e) => {
        const x = e.clientX - cursorGlow.offsetWidth / 2;
        const y = e.clientY - cursorGlow.offsetHeight / 2;
        cursorGlow.style.transform = `translate(${x}px, ${y}px)`;
    });

    // REFERENCES & API URL 
    const API_URL = "http://127.0.0.1:5000";
    const textInput = document.getElementById("text-input");
    const fileInput = document.getElementById("file-input");
    const fileNameSpan = document.getElementById("file-name");
    const actionButtons = document.querySelectorAll(".actions button");
    const outputText = document.getElementById("output-text");
    const loadingSpinner = document.getElementById("loading-spinner");
    const resultActions = document.querySelector(".result-actions");
    const copyButton = document.getElementById("copy-button");
    const downloadButton = document.getElementById("download-button");

    // FILE UPLOAD LOGIC 
    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            const file = fileInput.files[0];
            fileNameSpan.textContent = file.name;
            textInput.value = '';
            
            const formData = new FormData();
            formData.append('file', file);

            loadingSpinner.style.display = 'flex';
            outputText.textContent = "";
            resultActions.style.display = 'none';
            textInput.placeholder = "Extracting text from file...";

            fetch(`${API_URL}/upload`, {
                method: 'POST',
                body: formData,
            })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(err => { throw new Error(err.error) });
                }
                return response.json();
            })
            .then(data => {
                textInput.value = data.extracted_text;
                textInput.placeholder = "Paste your lecture transcript or long text here...";
            })
            .catch(error => {
                console.error('File Upload Error:', error);
                outputText.textContent = `Error: ${error.message}`;
            })
            .finally(() => {
                loadingSpinner.style.display = 'none';
            });
        } else {
            fileNameSpan.textContent = 'No file selected';
        }
    });

    // UX BUTTONS LOGIC 
    copyButton.addEventListener('click', () => {
        navigator.clipboard.writeText(outputText.textContent).then(() => {
            const originalText = copyButton.querySelector('span').textContent;
            copyButton.querySelector('span').textContent = 'Copied!';
            setTimeout(() => {
                copyButton.querySelector('span').textContent = originalText;
            }, 2000);
        });
    });

    downloadButton.addEventListener('click', () => {
        const text = outputText.textContent;
        const blob = new Blob([text], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'Kerna-AI-Output.txt';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    });

    // API CALLING LOGIC 
    async function callApi(endpoint, body) {
        loadingSpinner.style.display = "flex";
        outputText.textContent = "";
        resultActions.style.display = 'none';
        outputText.style.animation = 'none';

        try {
            const response = await fetch(`${API_URL}/${endpoint}`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(body),
            });
            
            if (!response.ok) {
                const contentType = response.headers.get("content-type");
                let errorText;
                if (contentType && contentType.indexOf("application/json") !== -1) {
                    const errorData = await response.json();
                    errorText = errorData.description || errorData.error || `HTTP error! Status: ${response.status}`;
                } else {
                    errorText = `Server error: ${response.status} ${response.statusText}. Check the Flask terminal for details.`;
                }
                throw new Error(errorText);
            }

            const data = await response.json();
            outputText.textContent = data.result;
            if (data.result) {
                resultActions.style.display = 'flex';
            }
            outputText.style.animation = 'fadeIn 0.5s ease-in-out';
        } catch (error) {
            console.error("API Error:", error);
            outputText.textContent = `Error: ${error.message}`;
        } finally {
            loadingSpinner.style.display = "none";
        }
    }

    actionButtons.forEach(button => {
        button.addEventListener("click", () => {
            const endpoint = button.dataset.endpoint;
            const text = textInput.value;

            if (!text) {
                alert("Please provide content by pasting text or uploading a file.");
                return;
            }

            const requestBody = { text: text };
            callApi(endpoint, requestBody);
        });
    });
});