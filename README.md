# Llama 2

Unlock the power of large language models with Llama 2. Our latest release is accessible to individuals, creators, researchers, and businesses of all sizes, enabling them to experiment, innovate, and scale their ideas responsibly.

This repository includes model weights and starter code for pre-trained and fine-tuned Llama language models, ranging from 7B to 70B parameters.

This repository serves as a minimal example for loading [Llama 2](https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/) models and running inference. For more detailed examples leveraging Hugging Face, refer to [llama-recipes](https://github.com/facebookresearch/llama-recipes/).

# vizintel

Querying CSV and Plotting Graphs using LLM (Llama 2)

## Sample Demo

## Overview

Vizual Intelligence uses Llama 2 for interacting with CSV files. The app generates statistical plots based on user prompts. You can ask any statistical question, and it will be answered with visual plots.

## Key Features

- **User-friendly Interface:** We have used Streamlit for a more convenient interface. We can even integrate React.js for further enhancements.
- **CSV File Upload:** Users can upload CSV files containing their datasets directly through the web interface.
- **Plot Generation:** Leveraging the Llama 2 model, the backend dynamically generates insightful plots based on user-defined criteria.
- **Interactive Visualization:** The generated plots are interactive and customizable, allowing users to explore specific data points of interest.

## Pre-requisite

Visit the AI at Meta website, accept our License, and submit the form. Once your request is approved, you will receive a pre-signed URL in your email.

## Installation

To run the project locally, follow these steps:

- I have taken the sample video by running it in my college System with Specigfications Intel i5 processor and Nvidia RTX 4080 GPU.
- This will run only with these Specification to get faster inference.

1. Install Ollama
```bash
curl https://ollama.ai/install.sh
```
2. Start the server
```bash
ollama serve
```
3. Connect to the Ollama server
```bash
service ollama start
```
4. Clone the repository
```bash
git clone https://github.com/Aswin-M-The-Coder/vizintel.git
```
5. Navigate to the project directory
```bash
cd vizintel
```
6. Install dependencies
```bash
pip install -r requirements.txt
```
7. Run the Python app
```bash
cd ollama/
streamlit run ./app.py
```
8. Access the application in your web browser at `http://localhost:8501`

# Usage
- Upload a CSV file containing your dataset through the web interface.
- Generate plots based on your selected criteria.
- Interact with the plots to explore specific data points or trends.

# Contributing
Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
- Make your changes and commit them: `git commit -m 'Add new feature'`.
- Push to the branch: `git push origin feature-name`.
- Submit a pull request detailing your changes.

# Acknowledgements
- Thank you to the creators of Python, Streamlit, and other open-source tools used in this project.
- Special thanks to the Llama 2 model developers for their contributions to data analysis and visualization.
