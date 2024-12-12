# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iTJKE0-11XA8ptImnqEakYKb4fsYDtm5
"""

from app.file_upload import handle_upload
from app.question_answer import start_interaction
from app.story_generator import generate_artifacts
from app.export import export_to_csv

if __name__ == "__main__":
    print("Welcome to the AI User Story Agent!")
    pdf_path = input("Upload your PDF file path: ")
    requirements = input("Enter your business requirements: ")

    # Step 1: Handle PDF Upload
    extracted_text = handle_upload(pdf_path)

    # Step 2: Start Q&A Interaction
    answers = start_interaction()

    # Step 3: Generate Personas, User Stories, and Scenarios
    personas, user_stories, scenarios = generate_artifacts(extracted_text, requirements, answers)

    # Step 4: Export Artifacts to CSV
    export_to_csv(personas, user_stories, scenarios)
    print("Generated artifacts have been saved in the 'data/outputs/' directory.")