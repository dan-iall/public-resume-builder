# Quarto Resume Builder 🚀

A powerful, data-driven resume generation system built with **Python** and **Quarto**. This tool allows you to treat your resume as code, version control your career history, and generate beautiful, ATS-friendly PDFs tailored to specific roles or companies.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Quarto](https://img.shields.io/badge/Quarto-1.3%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🌟 Why Use This?

* **Data-Driven**: Separate content (`JSON`) from design (`Jinja2`/`Quarto`), enabling easy updates without formatting headaches.
* **Version Control**: Manage different versions of your resume (e.g., Data Analyst vs. Product Manager) as separate subdirectories.
* **Tailored Outputs**: Quickly generate custom PDFs for specific job applications.
* **Professional Design**: Uses LaTeX under the hood via Quarto for crisp, professional typography.

## 📂 Repository Structure

```text
public-resume-builder/
├── builder.py            # 🛠️ The build script
├── resources/            # 📚 Helper resources and examples
├── cv_versions/          # 📄 Resume versions live here
│   ├── example_candidate/  # 🟢 Start here! A template for you
│   │   ├── resume_data.json
│   │   └── resume_template.qmd.j2
│   └── data_product_manager/ # 🔵 A real-world example (Sample)
├── requirements.txt      # 📦 Python dependencies
└── README.md             # 📖 You are here
```

## 🛠️ Tech Stack & System Setup

This project uses a modern, open-source stack to generate high-quality documents:

1. **Python**: Handles logic, data parsing, and templating using **Jinja2**.
2. **Quarto**: An open-source scientific and technical publishing system that renders markdown to PDF (via TinyTeX/LaTeX).
3. **JSON**: Stores your resume content in a structured, easy-to-read format.

### Prerequisites

* [Python 3.8+](https://www.python.org/downloads/)
* [Quarto CLI](https://quarto.org/docs/get-started/)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/resume-builder.git
    cd resume-builder
    ```

2. **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 How to Use

### 1. Create Your Version

Copy the `example_candidate` folder to a new folder with your name or role (e.g., `my_resume`).

```bash
cp -r cv_versions/example_candidate cv_versions/my_resume
```

### 2. Edit Your Data

Open `cv_versions/my_resume/resume_data.json` and fill in your details. You can define custom skill groups, work history, and education.

### 3. Build Your Resume

Run the builder script. You can build a specific version by passing the folder name.

```bash
# Build specific version
python builder.py my_resume
```

or build **all** versions found in `cv_versions`:

```bash
python builder.py
```

### 4. Find Your PDF

Your generated PDF will be located inside your version folder, named automatically based on your metadata:
`cv_versions/my_resume/resume_[company]_[role]_[date].pdf`

## ✨ Features

### Flexible Skill Groups

Don't get locked into "Hard Skills" vs "Soft Skills". Define your own categories in `resume_data.json`:

```json
"skill_groups": [
    { "name": "Strategic", "keywords": ["Product Strategy", "Roadmapping"] },
    { "name": "Technical", "keywords": ["Python", "SQL", "Tableau"] }
]
```

### Automatic Versioning

The builder automatically appends dates and target roles to filenames, so you never send the wrong resume (e.g., `resume_google_pm_2024-01.pdf`).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🤖 Unlock the AI Agent

This repository comes with a "Resume Consultant" persona designed to work with your LLM (ChatGPT, Claude, etc.).

1. **Open** `resources/agent_persona.md`.
2. **Copy** the System Prompt.
3. **Paste** it into your LLM.
4. **Upload** your `resume_data.json` and any files from `resources/` (like the `sample_consulting_resource.md`).

The Agent will now act as your personal **Career Architect**, helping you tailor your resume JSON for specific job descriptions while ensuring you stay true to your actual skills.

## 👨‍💻 About the Author

**Danial Bahrambeygi** is a Product Manager & Data Scientist who builds tools to solve complex problems—including the job search itself.

> *"I believe in bringing engineering rigor to product management. This project is a reflection of that philosophy: data-driven, version-controlled, and automated."*

I am currently open to **Product Management** roles where I can combine strategic vision with technical execution.

* **Connect on LinkedIn**: [Danial Bahrambeygi](https://bit.ly/DaniPM_LI)
* **View My Resume**: [Latest PDF](cv_versions/data_product_manager/cv_dani_general_resume_2026-01.pdf)

## � Acknowledgements

This project was originally forked from and inspired by the excellent [CV_Quarto](https://github.com/acbass49/CV_Quarto) repository by [acbass49](https://github.com/acbass49).

## �📄 License

This project is licensed under the MIT License.
