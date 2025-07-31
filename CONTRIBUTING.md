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

Thank you for your contribution! 🎉