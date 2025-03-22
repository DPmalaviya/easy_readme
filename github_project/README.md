# RAG_dashboard: Your Retrieval-Augmented Generation Dashboard

## Overview

This repository provides a powerful and user-friendly dashboard built with Streamlit for performing Retrieval-Augmented Generation (RAG).  Upload your PDF documents, and instantly query them to receive accurate, context-aware answers.  RAG_dashboard leverages the power of Langchain, Chroma, and your choice of embedding and language models (OpenAI, Hugging Face, Ollama) to deliver a seamless and efficient RAG experience.

## Key Features

* **Intuitive Streamlit Interface:** Easily upload PDFs, select model parameters, and query your documents through a clean and interactive dashboard.
* **Flexible Embedding & LLM Selection:** Choose between OpenAI embeddings, Hugging Face embeddings, and various LLMs (GPT-3.5 Turbo, LLaMA 3.1, Mistral, GPT-4) to tailor the pipeline to your needs and budget.
* **Customizable Chunking:** Employ either `RecursiveCharacterTextSplitter` or `SemanticChunker` for optimal document splitting.
* **Multiple Prompt Templates:** Select from pre-built prompt templates or customize your own to fine-tune the question-answering process.
* **Source Attribution:**  Clearly see the source documents used to generate each answer, ensuring transparency and traceability.
* **Efficient Vector Database:**  ChromaDB is used for fast and efficient similarity search, allowing for quick retrieval of relevant information.
* **Extensible Design:** Easily integrate new features and functionalities.

## Folder Structure

```
├── .gitignore              
├── RAG_dash.py             # Main Streamlit application
├── compare_embeddings.py   # Example script for embedding comparison
├── create_database.py      # Script for creating the vector database
├── query_data.py           # Script for querying the vector database
├── requirements.txt        
├── streamlit_game.py       # Example Streamlit app (game manuals)
├── streamlit_storm.py      # Example Streamlit app (research papers)
└── README.md               
```

## Prerequisites

* Python 3.8 or higher
* pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Avadh-Ladani-0/RAG_dashboard.git
   cd RAG_dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up API keys:

   * **OpenAI:** Obtain your API key from the [OpenAI platform](https://platform.openai.com/) and create a `.env` file in the project root directory with `OPENAI_API_KEY=<your_api_key>`.
   * **Ollama:** Download and install Ollama, then configure your LLAMA 3.1 and Mistral models.  Ensure your Ollama environment is correctly set up.

## Usage

### Running the Main Application

Launch the Streamlit dashboard:

```bash
streamlit run RAG_dash.py
```

This will open a browser window with the interactive dashboard.  Upload your PDFs, adjust settings, and start querying!

### Additional Scripts and Demo Applications

* **`create_database.py`**:  Use this script to independently create or update your vector database.
* **`compare_embeddings.py`**: A simple example demonstrating embedding comparison.
* **`query_data.py`**:  Allows querying the database from the command line.
* **`streamlit_game.py` and `streamlit_storm.py`**: Explore these example Streamlit apps showcasing different use cases (game manuals and research papers, respectively).  Run them using `streamlit run <filename>.py`.

## Project Flow

1. **Document Preparation:** Upload your PDF documents to the application.
2. **Database Creation:** The `RAG_dash.py` script (or `create_database.py`) will process the documents, create embeddings, and populate the Chroma vector database.
3. **Querying:** Enter your question into the Streamlit interface.
4. **Answer Retrieval:** The RAG pipeline retrieves relevant information from the database and uses the selected LLM to generate a response.
5. **Output:** The answer, along with its source documents, is displayed.


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgments

* OpenAI
* Hugging Face
* Langchain
* ChromaDB
* Ollama


For any questions or issues, please open an issue on GitHub or contact Avadh Ladani at avadhladani2002@gmail.com.
