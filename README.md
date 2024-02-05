# Introduction

Our project, **AutoChart**, is inspired by the critical challenges faced by the Emergency and Family Medicine Departments, characterized by a severe manpower shortage leading to prolonged patient wait times and doctor burnout. **AutoChart** aims to alleviate these pressures by streamlining medical documentation processes.

## Inspiration

The heartbreak over manpower shortages in critical healthcare departments motivated us. These shortages result in patients enduring long wait times in discomfort and doctors experiencing extreme burnout, primarily due to the overwhelming burden of charting and medical documentation.

Our goal is to lighten doctors' workloads and expedite patient treatment with our innovative solution.

## What It Does

**AutoChart** transforms doctor-patient conversations into transcribed, well-organized, medically precise charts. This process involves:

- **Transcribing** the conversation using OpenAI's Whisper model.
- **Organizing** the transcription into a structured medical chart with the help of OpenAI's GPT-4 model.

![Screenshot](/photo_2024-02-06_00-34-00.jpg "Sample Use Case")


## How We Built It

Our development process included:

- **Leveraging OpenAI's Whisper Model**: Fine-tuned for Singaporean English using the [Singapore ASR dataset](https://www.imda.gov.sg/how-we-can-help/national-speech-corpus).
- **Utilizing OpenAI's GPT-4**: For formatting the conversation into a medical chart.

## Challenges We Ran Into

- The **size of the ASR dataset** was formidable at 1.5TB, leading us to use only a small sample.
- **Data transformation** required converting pure audio data into an amplitude array at a 16000Hz sampling rate, demanding significant computational resources.
- **Extended training time** for the Whisper model due to its complexity and the high computational resources required.

## Accomplishments We're Proud Of

- **Successful Application Implementation**: Hosted on Huggingface Spaces.
- **Effective Training**: Achieved with the Whisper model.

## What We Learned

Our journey taught us valuable lessons in audio data processing, including:

- Transforming audio data into an amplitude array.
- Utilizing the log-mel spectrogram to reduce audio data dimensionality.
- Fine-tuning the Whisper model for enhanced audio data interpretation.

## What's Next for AutoChart

Moving forward, we aim to:

- **Collaborate with Medical Professionals**: To refine the document's precision.
- **Explore Integration Opportunities**: In hospitals and clinical settings.
- **Pursue Regulatory Approvals**: Such as FDA/ISO13485 certifications, to facilitate medical industry adoption.

## Conclusion

**AutoChart** represents a significant step forward in addressing the pressing challenges within the healthcare documentation process. By leveraging advanced AI technologies, we envision a future where healthcare professionals can focus more on patient care and less on administrative tasks.

## Application 
[AutoChart Medical Charting](https://huggingface.co/spaces/Mompansy/AutoChart)

The link to the huggingface repo is here, it is set to private as it is using my personal openAI api so if you would like to try the app for yourself please contact me.

---

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

---

[WhisperFineTune Transcription App](https://huggingface.co/spaces/Mompansy/WhisperFineTune)

Feel free to test the app with your own audio samples to see how effectively the model transcribes Singaporean English.


