### MedicalChatbot Project

## Overview
The **MedicalChatbot** project leverages state-of-the-art AI techniques to build a chatbot capable of answering medical-related queries. It uses advanced natural language processing (NLP) tools and models for semantic understanding and integrates with vector databases for efficient information retrieval. The user-friendly frontend is built with Flask, HTML, and CSS for seamless interaction.

## Workflow
1. **Loading Dataset and Splitting Text into Chunks**:
   - Functions used:
     - \`langchain.document_loaders.PyPDFLoader\`
     - \`langchain.document_loaders.DirectoryLoader\`
   - Text splitting:
     - \`langchain.text_splitter.RecursiveCharacterTextSplitter\`

2. **Converting Text Chunks into Vector Embeddings**:
   - **Model Used (HuggingFace)**:
     - \`all-MiniLM-L6-v2\`: A sentence-transformers model that maps sentences and paragraphs into a 384-dimensional dense vector space for tasks like clustering and semantic search.

3. **Storing Vector Embeddings in Pinecone Vector Database**:
   - Efficient storage and retrieval of embeddings for fast and accurate responses.

4. **Integrating Large Language Model (LLM)**:
   - **Model Used**:
     - OpenAI's GPT for generating responses based on semantic understanding of user queries.

5. **Frontend Development**:
   - Built with **Flask** for the backend server and **HTML** and **CSS** for a user-friendly interface.

6. **Dataset Used**:
   - **The GALE ENCYCLOPEDIA of MEDICINE**: A comprehensive dataset of medical information.

## Features
- NLP-driven chatbot for medical-related questions.
- Uses sentence-transformer embeddings for semantic search.
- Scalable vector database integration with Pinecone.
- LLM-powered intelligent responses via OpenAI.
- Interactive web-based user interface using Flask, HTML, and CSS.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - LangChain
  - Sentence-Transformers
  - Pinecone
  - Flask
- **Frontend**:
  - HTML, CSS
- **Model**:
  - \`all-MiniLM-L6-v2\`
  - OpenAI GPT
- **Dataset**: The GALE ENCYCLOPEDIA of MEDICINE

## Installation
1. Clone the repository:
   \`\`\`bash
   git clone <repository-link>
   cd MedicalChatbot
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Set up API keys:
   - OpenAI API key for LLM integration.
   - Pinecone API key for vector database.

4. Run the application:
   \`\`\`bash
   python app.py
   \`\`\`

## Usage
- Open your browser and navigate to \`http://127.0.0.1:8080\` to interact with the chatbot.

## Future Enhancements
- Extend dataset for broader medical domains.
- Add support for multi-language queries.
- Enhance UI/UX for better interaction.

## Contact
For questions or contributions, reach out to [Aditya Kumar] at [(https://www.linkedin.com/in/kumaraditya23/)]
