# AI-Agent-Development-for-User-Stories-and-Business-Scenarios

Project Overview

This project creates an intelligent AI agent to generate user personas, user stories, and business scenarios from provided business requirements and uploaded files. The agent leverages natural language processing (NLP) techniques using Python, LangChain, and LangFlow.

Features

File Upload: Users can upload PDF documents for processing.

Conversational Interaction: The agent interacts with users, asking questions to extract detailed business insights.

Data Storage: All user inputs, file data, and responses are stored in a vector database.

Generation of Outputs:

Personas: Descriptions of key stakeholders.

User Stories: "As a persona, I want to perform a task so that I can achieve a goal."

Business Scenarios: Detailed scenarios in Gherkin format.

Export Capability: Outputs can be downloaded as a CSV file.


Repository Structure

ai_user_story_agent/
├── main.py                  # Entry point for the application
├── app/
│   ├── __init__.py          # Initializes the app module
│   ├── file_upload.py       # Handles PDF uploads and text extraction
│   ├── question_answer.py   # Manages agent-user interaction
│   ├── vector_store.py      # Manages vector database interactions
│   ├── story_generator.py   # Generates personas, user stories, and business scenarios
│   ├── export.py            # Handles CSV export
│   └── utils.py             # Utility functions
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
└── data/
    ├── uploads/             # Stores uploaded files
    ├── processed/           # Processed data for debugging
    └── outputs/             # Generated CSV files
