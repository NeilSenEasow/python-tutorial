![image](https://github.com/user-attachments/assets/9a4ee739-22f8-4129-8964-04479370e7b6)

# Income Tax Calculator

A simple web-based application that calculates income tax based on predefined tax slabs. This project uses **Python (Flask)** for the backend and **HTML/CSS/JavaScript** for the frontend.

## Features

- User-friendly interface to input annual income.
- Real-time income tax calculation with dynamic updates.
- Simple and responsive design.

---

## Prerequisites

Ensure you have the following installed on your system:

1. **Python 3.7 or higher**  
2. **pip (Python Package Manager)**  
3. **A web browser**  

---

## Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/income-tax-calculator.git
cd income-tax-calculator
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Server
```bash
python app.py
```

### 5. Open the Application in Your Browser
Navigate to:
```
http://localhost:3000
```

---

## File Structure

```
.
├── app.py                   # Main Flask application
├── requirements.txt         # Dependencies for the project
├── static/
│   └── style.css            # Styling for the application
├── templates/
│   └── index.html           # Frontend for the tax calculator
└── README.md                # This README file
```

---

## How It Works

1. **User Input:** Enter your annual income in the input field.
2. **Tax Calculation:** The application sends the input to the backend using JavaScript (Fetch API).
3. **Backend Logic:** The Flask backend computes the tax based on predefined slabs:
   - ₹0 to ₹2,50,000: No tax
   - ₹2,50,001 to ₹5,00,000: 5% tax
   - ₹5,00,001 to ₹10,00,000: 20% tax
   - Above ₹10,00,000: 30% tax
4. **Display Output:** The calculated tax is displayed dynamically below the form.

---

## Dependencies

The project uses the following Python libraries:

- **Flask**: A micro web framework for Python.

To install all dependencies, run:
```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions, please:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of your feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request on GitHub.

---

## Contact

For any questions or feedback, feel free to reach out!
