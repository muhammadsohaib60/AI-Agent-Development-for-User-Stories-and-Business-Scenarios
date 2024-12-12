# AI User Story Agent

This repository is designed for managing AI-generated user stories, personas, and business scenarios based on user-uploaded documents. The application supports text extraction, question-answering, and CSV export functionalities.

## Project Structure

```
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
```

## Features

- **File Upload:** Extracts text content from uploaded PDF files.
- **Question Answering:** Interactive agent for querying extracted data.
- **User Story Generation:** Creates personas, user stories, and business scenarios.
- **Vector Store Integration:** Efficient storage and retrieval of processed data.
- **CSV Export:** Outputs generated content into CSV format for easy sharing.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai_user_story_agent.git
   cd ai_user_story_agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Directory Details

- **`main.py`:** The entry point for the application.
- **`app/`:** Contains all application logic, including modules for file handling, question-answering, and story generation.
  - `file_upload.py`: Extracts text from uploaded PDF files.
  - `question_answer.py`: Manages interactions between the user and the agent.
  - `vector_store.py`: Interfaces with the vector database for efficient data storage and retrieval.
  - `story_generator.py`: Generates user stories, personas, and scenarios based on extracted data.
  - `export.py`: Handles exporting generated content to CSV files.
  - `utils.py`: Provides reusable utility functions.
- **`data/`:** Stores user-uploaded files, processed data, and generated outputs.
  - `uploads/`: Uploaded files from users.
  - `processed/`: Intermediate data for debugging and further processing.
  - `outputs/`: Final generated CSV files.

## Usage

1. Upload a PDF document via the application's interface.
2. Interact with the AI agent to query the content.
3. Generate personas, user stories, and business scenarios.
4. Export the generated content as a CSV file.

## Contributing

Feel free to submit issues or pull requests to improve the project.



---
