# Automation Buddy

**Automation Buddy** is an end-to-end regression testing framework for web applications. It simulates real user workflows—login, browsing, add-to-cart, checkout, logout—so you catch UI and functional bugs automatically every time you push code.

---

## 🛠 Features

- **Page Object Model** for maintainable, reusable page abstractions  
- **Selenium + pytest** for reliable browser automation  
- **Headless Chrome (incognito)** with password-manager disabled  
- **HTML test reports** with embedded screenshots on failures  
- **CI/CD ready**: GitHub Actions workflow included  
- **Cross-browser support** (easily extend to Firefox, Edge, etc.)  

---

## 💾 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-org/automation-buddy.git
   cd automation-buddy
    ```
2. **Create & activate virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate    # macOS/Linux
    venv\Scripts\activate       # Windows
    ```
3. **Install dependencies**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

## ▶️ Running Tests Locally
    ```bash
    # run all tests with headful Chrome
    pytest --maxfail=1 --disable-warnings -q

    # run in headless mode (for CI)
    pytest --maxfail=1 --disable-warnings -q --headless
    ```
- HTML report is generated at reports/report.html
- Screenshots on failures are saved under reports/screenshots/

## ⚙️ CI Integration
# This repo includes a GitHub Actions workflow (.github/workflows/ci.yml) that:

- Triggers on every push & pull-request to main

- Spins up Ubuntu, sets up Python and Chrome

- Runs your suite headlessly

- Uploads the HTML report as an artifact

## ➕ Adding New Tests
1. Create a Page Object under pages/

2. Write a pytest module in tests/ (filename test_*.py)

3. Use driver fixture to get a browser instance

4. Run pytest to see your new test in action!

## 🤝 Contributing
Feel free to open issues or submit PRs. For major changes, please open an issue first to discuss your ideas.

