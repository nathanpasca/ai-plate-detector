# AI License Plate Recognition System
Python-based license plate recognition system using Google's Gemini AI API to detect and analyze vehicle information from images. This project was developed as part of President University MSIT Machine Learning course assignment to demonstrate practical applications of AI in messaging platforms.

## Prerequisites
Before running this bot, make sure you have:
- Python 3.9+
- Google Cloud account with Gemini AI API access
- PIL (Python Imaging Library)

## Installation
1. Clone repository:
```bash
git clone https://github.com/nathanpasca/ai-plate-detector
cd ai-plate-detector
```

2. Install dependencies:
```bash
pip install google-generativeai
pip install pillow
pip install python-dotenv
```

3. Create `.env` file:
```env
API_KEY=your_gemini_api_key_here
```

## Usage
Run the script:
```bash
python3 main.py
```

The system will:
- Load the image specified in the code
- Process it using Gemini AI
- Output JSON with plate number, vehicle details, and gate timestamps

Example output:
```json
{
    "plat_no": "B 1234 ABC",
    "vehicle": "car",
    "vehicle_type": "sedan",
    "color": "red",
    "gate_open": "2024-12-02 18.15.01",
    "gate_closed": "N/A"
}
```

## Note
Ensure input images are clear and well-lit for optimal recognition accuracy.

## Academic Disclaimer

This project was developed as part of an academic assignment in Machine Learning. While it serves as a practical demonstration of AI concepts, it may need additional features and security measures for production use.

## Acknowledgments
- [Google Gemini AI](https://ai.google.dev/)
- [Python Pillow](https://python-pillow.org/)
