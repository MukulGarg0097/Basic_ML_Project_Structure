# 📦 Python Project Base Template (with `src/` layout)

This repository provides a **reusable base structure** for building Python projects using `setup.py` and the **`src/` layout**.  
It helps you organize code, tests, and docs cleanly while supporting packaging and distribution.

---

## 📂 Project Structure

```
your_project/
│
├── src/                        # Source code root where your package lives here
│   └── __init__.py
│
├── tests/                      # Unit tests (add your test files here)
│
├── docs/                       # Documentation (optional)
│
├── setup.py                    # Packaging script
├── requirements.txt            # Dependencies
├── README.md                   # Project description
├── LICENSE                     # License
└── .gitignore                  # Git ignore rules
```

---

## ⚙️ Installation

Clone this repository and install it in editable mode:

```bash
git clone https://github.com/MukulGarg0097/Basic_ML_Project_Structure.git
cd your_project
pip install -e .
```

This will install the package locally while keeping it editable.  
Any changes you make to the source code inside `src/your_package/` will be reflected immediately.

---

## 🧪 Running Tests

Place your tests inside the `tests/` folder.  
Run them using:

```bash
pytest
```

If you don’t have `pytest` installed:

```bash
pip install pytest
```

---

## 📜 Commands Reference

| Command | Description |
|---------|-------------|
| `pip install -e .` | Install package in editable mode |
| `pytest` | Run all tests in `tests/` |
| `python setup.py sdist bdist_wheel` | Build source and wheel distribution |
| `twine upload dist/*` | Upload package to PyPI (optional) |

---

## 📝 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---
