This repository contains a project to develop an intelligent agent capable of generating personas, user stories, and business scenarios based on uploaded business requirements and file attachments. The agent uses conversational AI to interact with users and create structured outputs in formats like Gherkin for business scenarios.


Features : 
Upload and Process Documents: Accepts PDF documents and extracts business requirements text.

Conversational Interaction: Uses AI to ask specific questions about the business and gathers user responses.

Data Storage: Stores documents, requirements, and responses in a vector database for efficient querying.

Persona and Story Generation: Creates personas, user stories, and Gherkin-based business scenarios.

CSV Export: Outputs generated data into a structured CSV format for easy download.


Project Structure :

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
