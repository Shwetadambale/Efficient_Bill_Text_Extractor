##  Text Extraction From Store Bills.

Manual data entry of retail store bills is time-consuming and prone to errors. This project aims to automate the extraction of text information from store bills using OCR techniques.

### Problem Statement: 

Manually entering data from retail store bills is:
- **Extremely Time-Consuming: It takes a significant amount of time to manually enter data from each bill.
- **Prone to Errors: Human errors during manual data entry lead to inaccuracies.

### Project Overview :

This project utilizes Optical Character Recognition (OCR) techniques and regular expressions for text extraction from retail store bills. It comprises the following key components:
- *Data Preprocessing using Regular Expressions*: Utilizes regular expressions to preprocess the bill images/text before extraction.
- *OCR-based Text Extraction*: Implements OCR techniques to extract text information from bill images.
- *Automation of Data Entry*: Automates the extraction process to minimize manual intervention.

### Features: 

- *Efficiency*: Automation reduces the time required for data entry significantly.
- *Accuracy*: OCR techniques, along with regex-based preprocessing, minimize errors in data extraction.
- *Scalability*: Capable of handling various bill formats and scales efficiently.

### Technologies Used

- OCR Library: *PaddleOCR*
- Regular Expressions: Used for preprocessing tasks such as cleaning and formatting text data.
- Programming Language: Python
- Database : *SQL

### Usage

Follow these steps to use the project:
- Clone the Repository: Clone this repository to your local machine.
- Install Dependencies: Install the necessary libraries or tools using the provided requirements file.
- Preprocessing with Regular Expressions: Utilize the regex scripts in /preprocessing to clean and format text data before OCR.
- OCR Text Extraction: Run the OCR process using the provided scripts in /OCR_extraction.
- Access Extracted Text: Extracted text data will be available in [specified output format or location].

### Installation: 

The Code is written in Python 3.9. If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

pip install -r requirements.txt 

### Future Improvements: 

Potential areas for enhancement include:
- Improved Preprocessing: Enhance regex patterns for more robust data cleaning and formatting.
- Handling Different Bill Formats: Extend OCR capabilities to handle diverse store bill formats.
- Integration with Database: Implement integration to store extracted data directly into a database.

### Author: 

Shweta Dambale 

### License:

This project is licensed under the MIT License, which means you are free to use, modify, and distribute the code for both commercial and non-commercial purposes.

### Acknowledgments:

We would like to thank the open-source community, contributors, and data providers for making this project possible.

### Contact: 

For questions, suggestions, or collaboration inquiries, please contact [Shweta Dambale] at [shwetadambale123@gmail.com].
