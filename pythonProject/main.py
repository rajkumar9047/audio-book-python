import PyPDF2
from gtts import gTTS
import os

def pdf_to_audio(pdf_file, audio_file):
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        # Extract text from each page
        for page in reader.pages:
            text += page.extract_text() + "\n"

    # Check if text was extracted
    if not text.strip():
        print("No text found in the PDF.")
        return

    # Convert text to audio
    tts = gTTS(text=text, lang='en')
    tts.save(audio_file)
    print(f"Audio file saved as '{audio_file}'")

if __name__ == "__main__":
    pdf_file = "book.pdf"  # Replace with your PDF file path
    audio_file = "output_audio.mp3"  # Output audio file name
    pdf_to_audio(pdf_file, audio_file)
