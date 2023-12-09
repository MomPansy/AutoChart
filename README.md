# Fine-Tuning OpenAI's Whisper Model on Singaporean English

## Project Overview
This project aims to fine-tune OpenAI's Whisper model to better understand and transcribe Singaporean English. We utilize the [National Speech Corpus](https://www.imda.gov.sg/how-we-can-help/national-speech-corpus) provided by IMDA for our dataset.

## Pipeline Flow

### Data Preprocessing
The preprocessing stage involves downloading files from a Dropbox link specified in the code. This link will vary depending on the specific section of the dataset being used. To initiate the preprocessing, run the main file under the `preprocessing-pipeline` directory. The details of this process can be viewed in the `DataProcessingPipeline.ipynb` notebook in the repository. 

### Training Pipeline
After preprocessing, we move on to the training pipeline. The training process is conducted on a fraction of the dataset for demonstration purposes. The details of this process can be viewed in the `Training_pipeline.ipynb` notebook in the repository. 

### Model Evaluations and Training Metrics
The evaluations of the model and detailed training metrics can be found on our Hugging Face repository: [Hugging Face Repository - whisperfinetune_modelcheckpoints](https://huggingface.co/Mompansy/whisperfinetune_modelcheckpoints). This includes performance metrics, model checkpoints, and other relevant evaluation data.

## Instructions

### Prerequisites
- Ensure you have Python installed on your system.
- The code is designed to run with Google Drive mounted on macOS. If you're using a different operating system, modifications might be necessary.

### Installation

Before running the project, you'll need to install the necessary dependencies.

#### Installing Dependencies
This project requires certain Python packages to be installed. These dependencies are listed in the `requirements.txt` file. To install them, follow these steps:

1. **Clone the Repository**:
   If you haven't already, clone the repository to your local machine:

   ```bash
   git clone https://github.com/MomPansy/WhisperFineTune.git
   ```

2. **Navigate to the Repository Directory**:
   Change into the repository directory:

   ```bash
   cd YourRepositoryName
   ```

3. **Create a Virtual Environment (Optional but Recommended)**:
   It's a good practice to use a virtual environment for your Python projects. Create one using:

   ```bash
   python -m venv venv
   ```

   Activate it with:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the Dependencies**:
   Install all required packages with the following command:

   ```bash
   pip install -r requirements.txt
   ```

Now, your environment should be set up with all the dependencies needed for the project.

### Running the Code
1. Clone the repository to your local machine.
2. Navigate to the repository's preprocessing-pipeline directory in the command line.
3. Run the main script with your access token:

   ```bash
   python main.py 'YOUR_ACCESS_TOKEN'
   ```

   Replace `'YOUR_ACCESS_TOKEN'` with your actual access token for the Dropbox API.

### Note
The current implementation is tailored for macOS with Google Drive integration. If you are using a different operating system or cloud storage solution, you will need to adjust the file paths and storage configurations accordingly.

This README now includes a reference to your Hugging Face repository for model evaluations and training metrics. Make sure to provide the correct link to the training pipeline notebook and any other relevant resources.
