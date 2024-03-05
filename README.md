<p align="center">
  <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLXNwYXJrbGVzIj48cGF0aCBkPSJtMTIgMy0xLjkxMiA1LjgxM2EyIDIgMCAwIDEtMS4yNzUgMS4yNzVMMyAxMmw1LjgxMyAxLjkxMmEyIDIgMCAwIDEgMS4yNzUgMS4yNzVMMTIgMjFsMS45MTItNS44MTNhMiAyIDAgMCAxIDEuMjc1LTEuMjc1TDIxIDEybC01LjgxMy0xLjkxMmEyIDIgMCAwIDEtMS4yNzUtMS4yNzVMMTIgM1oiLz48cGF0aCBkPSJNNSAzdjQiLz48cGF0aCBkPSJNMTkgMTd2NCIvPjxwYXRoIGQ9Ik0zIDVoNCIvPjxwYXRoIGQ9Ik0xNyAxOWg0Ii8+PC9zdmc+" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">AutoBlog: AI Blog Generator</h1>
</p>
<p align="center">
    <em>Automagically create hundreds of blogs for free with the power of local llms.</em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat-square&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat-square&logo=Streamlit&logoColor=white" alt="Streamlit">
</p>

<br><!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary><br>

- [📍 Overview](#-overview)
- [🧩 Features](#-features)
- [🗂️ Repository Structure](#️-repository-structure)
- [📦 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Usage](#-usage)
- [🛠 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
- [🔗 Acknowledgments](#-acknowledgments)
</details>
<hr>

## 📍 Overview

Auto-Blogger is an open-source software project designed to automate blog creation with the power of AI. Users input their desired blog topic, the app. The Blog Manager then orchestrates content generation by interacting with the Blog Writer module, which uses an intelligent language model to create engaging and insightful blog posts. Once generated, the Blog Manager saves the blogs to local storage, allowing users to efficiently generate content.

---

## 🧩 Features

|     | Feature           | Description                                                                                                                          |
| --- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| ⚙️  | **Architecture**  | Microservices-based architecture with modular components and clear separation of concerns: blog management, generation, and writing. |
| 🔩  | **Code Quality**  | Adheres to PEP8 coding style; well-documented functions and modules.                                                                 |
| 📄  | **Documentation** | Detailed README file with project description, setup instructions, and API documentation in Markdown format.                         |
| 🧩  | **Modularity**    | Strongly modular, with each file handling a specific functionality and communicating through interfaces defined by clear APIs.       |
| 📦  | **Dependencies**  | Primarily dependent on Python, Streamlit, Ollama (and related packages) as specified in project dependencies.                        |

---

## 🗂️ Repository Structure

```sh
└── auto_blogger/
    ├── app.py
    ├── auto_blogger.ipynb
    ├── blog_generator.py
    ├── blog_manager.py
    ├── blog_writer.py
    ├── blogs
    │   ├── blog1.md
    │   ├── blog2.md
    └── utils.py
```

---

## 📦 Modules

<details closed><summary>.</summary>

| File                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [blog_manager.py](blog_manager.py)       | Create, retrieve, and track blog files based on topics. Class BlogManager offers functions fetch_existing_blogs (getting existing blogs), save_text_as_markdown (creating new ones), and fetch_stats_for_md_files (retrieving statistics).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [utils.py](utils.py)                     | In the given architecture, `utils.py` serves as a utility module by providing functions to format blog topics and titles for easier handling within the auto_blogger system. Specifically, its `format_func` method generates string representations of these data points in a uniform, topic-title format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [blog_generator.py](blog_generator.py)   | Generate blog posts from given topics with this module. It fetches sections from outlines, writes content for each section, and saves formatted markdown files. Improves over time as it learns from existing blogs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [auto_blogger.ipynb](auto_blogger.ipynb) | In the given codebase residing in the `auto_blogger` repository, the file `blog_manager.py` plays a central role in managing and orchestrating the creation and publication of blogs using different technologies.This critical component interacts with various other modules and systems like blog generator, Kafka messaging system, and writer, ensuring a smooth workflow. The main purpose of `blog_manager.py` is to act as a conductor that ties these functionalities together by receiving instructions and triggering the appropriate actions to generate blogs using specific tech stacks, manage their creation, and ultimately publish them through the specified channels.With its strategic position within this architecture, this file plays an integral part in automating the blogging process and allowing users to generate and share content effectively with different technology combinations. |
| [app.py](app.py)                         | Generate blogs using the AI Blog Generator app. This main file, `app.py`, creates an interface with Streamlit. It handles user inputs for blog topic, count, and format preference. Upon generation, the app displays the created blogs within the UI or saves them in a designated folder for future access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [blog_writer.py](blog_writer.py)         | Engage with an intelligent blog writer module. It leverages an AI language model to generate captivating content. Class BlogWriter processes user-provided text and returns AI-generated completion, enhancing your blogs with rich and thoughtful insights.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

</details>

---

## 🚀 Getting Started

**System Requirements:**

- **Python**: `version 3.11.8`

### ⚙️ Installation

<h4>From <code>source</code></h4>

> 1. Clone the auto_blogger repository:
>
> ```console
> $ git clone https://github.com/ikramhasan/AutoBlog-AI-Blog-Generator.git
> ```
>
> 2. Change to the project directory:
>
> ```console
> $ cd AutoBlog-AI-Blog-Generator
> ```
>
> 3. Install the dependencies:
>
> ```console
> $ pip install -r requirements.txt
> ```
>
> 4. Install Ollama from here: [Ollama](https://ollama.com/download)
>
> 5. Pull your preferred llm model:
>
> ```console
> $ ollama run mistral:7b-instruct
> ```
>
> Note: You can use any model you prefer. The above command is just an example. Make sure to replace `mistral:7b-instruct` with your preferred model in `blog_writer.py`.
>
> 6. Start the ollama server:
>
> ```console
> $ ollama serve
> ```

### 🤖 Usage

<h4>From <code>source</code></h4>

> Run auto_blogger using the command below:
>
> ```console
> $ python app.py
> ```

---

## 🛠 Project Roadmap

- [ ] `► Add support for llama.cpp, lmstudio`
- [ ] `► Improve formatting`
- [ ] `► Add multi-llm support`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/ikramhasan/AutoBlog-AI-Blog-Generator/issues)**: Submit bugs found or log feature requests for the `auto_blogger` project.
- **[Submit Pull Requests](https://github.com/ikramhasan/AutoBlog-AI-Blog-Generator/pulls)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/ikramhasan/AutoBlog-AI-Blog-Generator/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your local account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/ikramhasan/AutoBlog-AI-Blog-Generator.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to local**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com/ikramhasan/AutoBlog-AI-Blog-Generator/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ikramhasan/AutoBlog-AI-Blog-Generator" />
</a>
</p>
</details>

---

## 🎗 License

This project is protected under the [MIT](https://choosealicense.com/licenses/mit/) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/mit/) file.

---

## 🔗 Acknowledgments

- Ollama
- Streamlit
- Jupyter
- LiteLLM

[**Return**](#-overview)

---
