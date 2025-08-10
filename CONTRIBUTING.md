 foundational-infrastructure
﻿# Contributing to Shakti App 🤝

Thank you for your interest in contributing to **Shakti**! This project aims to provide a safe, anonymous platform for sharing stories, and we welcome contributions that help us achieve this mission.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Issue Guidelines](#issue-guidelines)
- [Community](#community)

## 🤝 Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

### Our Pledge

- **Respectful**: Treat everyone with respect and kindness
- **Inclusive**: Welcome contributors from all backgrounds
- **Collaborative**: Work together constructively
- **Supportive**: Help each other learn and grow

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- FFmpeg (for audio processing)
- A GitHub account

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   `ash
   git clone https://github.com/YOUR_USERNAME/Shakti-app.git
   cd Shakti-app
   `

3. **Add the upstream remote**:
   `ash
   git remote add upstream https://github.com/thedgarg31/Shakti-app.git
   `

## 🛠️ Development Setup

### 1. Create Virtual Environment

`ash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
`

### 2. Install Dependencies

`ash
# Install main dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
`

### 3. Install Pre-commit Hooks

`ash
pre-commit install
`

### 4. Verify Setup

`ash
# Run tests
pytest

# Run linting
flake8 .

# Format code
black .

# Start the app
streamlit run streamlit_app.py
`

## 🎯 How to Contribute

### Types of Contributions

We welcome various types of contributions:

- 🐛 **Bug fixes**
- ✨ **New features**
- 📚 **Documentation improvements**
- 🧪 **Tests**
- 🌍 **Translations**
- 🎨 **UI/UX improvements**
- ⚡ **Performance optimizations**

### Before You Start

1. **Check existing issues** to see if your idea is already being worked on
2. **Create an issue** to discuss your proposed changes
3. **Wait for feedback** from maintainers before starting work
4. **Assign yourself** to the issue once approved

## 🔄 Pull Request Process

### 1. Create a Feature Branch

`ash
git checkout -b feature/your-feature-name
`

### 2. Make Your Changes

- Write clean, readable code
- Follow our coding standards
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

`ash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run linting
flake8 .
black --check .
isort --check-only .
`

### 4. Commit Your Changes

`ash
git add .
git commit -m "feat: add new feature description"
`

#### Commit Message Format

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- eat: new feature
- ix: bug fix
- docs: documentation changes
- style: formatting changes
- 
efactor: code refactoring
- 	est: adding tests
- chore: maintenance tasks

### 5. Push and Create PR

`ash
git push origin feature/your-feature-name
`

Then create a Pull Request on GitHub with:

- **Clear title** describing the change
- **Detailed description** of what was changed and why
- **Link to related issues**
- **Screenshots** (if applicable)
- **Testing instructions**

### 6. PR Review Process

- Maintainers will review your PR
- Address any feedback or requested changes
- Once approved, your PR will be merged

## 📏 Coding Standards

### Python Style Guide

We follow [PEP 8](https://pep8.org/) with some modifications:

- **Line length**: 88 characters (Black default)
- **Imports**: Use isort for import sorting
- **Formatting**: Use lack for code formatting
- **Linting**: Use lake8 for linting

### Code Quality Tools

- **Black**: Code formatting
- **isort**: Import sorting
- **Flake8**: Linting
- **MyPy**: Type checking (optional but recommended)

### Best Practices

- **Functions**: Keep functions small and focused
- **Variables**: Use descriptive variable names
- **Comments**: Write clear, helpful comments
- **Docstrings**: Use docstrings for functions and classes
- **Error Handling**: Handle errors gracefully
- **Security**: Never commit sensitive data

## 🧪 Testing Guidelines

### Test Structure

`
tests/
├── __init__.py
├── test_app.py          # Main application tests
├── test_utils.py        # Utility function tests
└── conftest.py          # Test configuration (if needed)
`

### Writing Tests

- **Unit Tests**: Test individual functions
- **Integration Tests**: Test component interactions
- **Smoke Tests**: Basic functionality verification

### Test Categories

Use pytest markers to categorize tests:

`python
@pytest.mark.unit
def test_story_validation():
    pass

@pytest.mark.integration
def test_audio_processing_flow():
    pass

@pytest.mark.slow
def test_large_file_processing():
    pass
`

### Running Tests

`ash
# All tests
pytest

# Specific category
pytest -m unit
pytest -m integration

# With coverage
pytest --cov=. --cov-report=html

# Verbose output
pytest -v
`

## 📝 Issue Guidelines

### Creating Issues

When creating an issue, please:

1. **Use a clear, descriptive title**
2. **Provide detailed description**
3. **Include steps to reproduce** (for bugs)
4. **Add relevant labels**
5. **Include environment information**

### Issue Templates

We provide templates for:

- 🐛 Bug reports
- ✨ Feature requests
- 📚 Documentation improvements
- ❓ Questions

### Issue Labels

- ug: Something isn't working
- enhancement: New feature or request
- documentation: Improvements to documentation
- good first issue: Good for newcomers
- help wanted: Extra attention is needed
- priority-high: High priority issue
- priority-low: Low priority issue

## 🌍 Internationalization

### Adding New Languages

To add support for a new language:

1. **Add translation dictionary** in streamlit_app.py
2. **Update language selection** dropdown
3. **Test transcription** with new language code
4. **Update documentation**

### Translation Guidelines

- **Accuracy**: Ensure translations are accurate
- **Context**: Consider cultural context
- **Consistency**: Use consistent terminology
- **Testing**: Test UI with new translations

## 🚀 Release Process

### Versioning

We use [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] CHANGELOG updated
- [ ] Version bumped
- [ ] Tagged release
- [ ] Deployment verified

## 🏆 Recognition

Contributors are recognized in:

- **README.md**: Contributors section
- **CHANGELOG.md**: Release notes
- **GitHub**: Contributor graphs
- **Special mentions**: For significant contributions

## 📞 Getting Help

### Communication Channels

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Email**: For sensitive matters

### Mentorship

New contributors can get help from:

- **Good first issues**: Labeled for beginners
- **Maintainer guidance**: Available for complex issues
- **Community support**: From other contributors

## 🎉 Thank You!

Every contribution, no matter how small, makes a difference. Thank you for helping make **Shakti** a better platform for sharing stories and supporting those who need to be heard.

---

**Remember**: Every story matters. Every contribution counts. 💙

## 📚 Additional Resources

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Streamlit Documentation](https://docs.streamlit.io/)
=======
# Contributing to Shakti-app

First off, thank you for considering contributing to Shakti-app! It's people like you that make the open-source community such a great place. ❤️

We welcome any type of contribution, not just code. You can help with:
* **Reporting a bug**
* **Discussing the current state of the code**
* **Submitting a fix**
* **Proposing new features**
* **Becoming a maintainer**

## We Have a Code of Conduct
Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

---

## How to Contribute
Here’s how you can contribute to this project:

### Reporting Bugs 🐛
If you find a bug, please make sure it hasn't been reported yet by searching on GitHub under [Issues](https://github.com/my-projects-it/Shakti-app/issues).

If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/my-projects-it/Shakti-app/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

### Suggesting Enhancements 🚀
If you have an idea for a new feature or an enhancement to an existing one, please open an issue to discuss it. This allows us to coordinate our efforts and prevent duplication of work.

Before creating a new enhancement suggestion, please check if a similar one already exists in the [Issues](https://github.com/my-projects-it/Shakti-app/issues) list. If it does, please add your comments to the existing issue.

### Your First Code Contribution
Unsure where to begin contributing to Shakti-app? You can start by looking through these `good first issue` and `help wanted` issues:

* **Good first issues** - issues which should only require a few lines of code, and a test or two.
* **Help wanted issues** - issues which should be a bit more involved than `good first issue` issues.

Both issue lists are sorted by total number of comments. While not perfect, number of comments is a reasonable proxy for impact a given change will have.

### Pull Requests
When you're ready to contribute code, please follow these steps:

1.  **Fork the repository** and create your branch from `main`.
2.  **Set up your development environment.** You will need Android Studio and the Android SDK.
3.  **Make your changes.** Please follow the coding style of the project.
4.  **Add tests.** Your patch won't be accepted if it doesn't have tests.
5.  **Ensure the test suite passes.**
6.  **Make sure your code lints.**
7.  **Issue that pull request!**

---

## Development Setup

This project is a standard Android application. You will need the following to get started:
* [Android Studio](https://developer.android.com/studio) (latest stable version recommended)
* The Android SDK
* A physical device or emulator running Android API level 21 or higher.

To get the project running:
1.  Clone your fork: `git clone https://github.com/YOUR-USERNAME/Shakti-app.git`
2.  Open the project in Android Studio.
3.  Let Gradle sync and download the required dependencies.
4.  Build and run the app on your emulator or physical device.

---

## Styleguides

### Java & Kotlin Styleguide
We follow Google's Java and Kotlin style guides. Android Studio should be configured to do this by default, but please ensure your code adheres to these guidelines.

* [Google's Java Style Guide](https://google.github.io/styleguide/javaguide.html)
* [Android's Kotlin Style Guide](https://developer.android.com/kotlin/style-guide)

### XML Layouts Styleguide
* Use `snake_case` for file names (e.g., `activity_main.xml`).
* Use `camelCase` for view IDs (e.g., `id="@+id/userNameInput"`).
* Keep layouts readable and organized. Use `<include>` and `<merge>` tags where appropriate.

### Git Commit Messages
* Use the present tense ("Add feature" not "Added feature").
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
* Limit the first line to 72 characters or less.
* Reference issues and pull requests liberally after the first line. For example: `Closes #123`.

---

## Any questions?
If you have any questions, feel free to reach out by opening an issue on the repository.

Thank you for your contribution!
main
