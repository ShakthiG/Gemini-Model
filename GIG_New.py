{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyML4vjoKW87ynQC/YRY1MAp",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ShakthiG/Gemini-Model/blob/Gem1/GIG_New.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install -q -U google-generativeai"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "grw5EAUcKQlt",
        "outputId": "4f53138b-7b55-4e06-c1bb-1b5e51e45497"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[?25l     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/137.4 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K     \u001b[91m━━━━━━━━\u001b[0m\u001b[91m╸\u001b[0m\u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m30.7/137.4 kB\u001b[0m \u001b[31m945.7 kB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\r\u001b[2K     \u001b[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[91m╸\u001b[0m\u001b[90m━━━━━━━\u001b[0m \u001b[32m112.6/137.4 kB\u001b[0m \u001b[31m1.5 MB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\r\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m137.4/137.4 kB\u001b[0m \u001b[31m1.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X7TBfB0SH6zk",
        "outputId": "284d1dea-1174-4dc5-dda2-b670daa24c9f"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.32.2-py2.py3-none-any.whl (8.1 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.1/8.1 MB\u001b[0m \u001b[31m22.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.3.3)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<2,>=1.19.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.25.2)\n",
            "Collecting packaging<24,>=16.8 (from streamlit)\n",
            "  Downloading packaging-23.2-py3-none-any.whl (53 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m53.0/53.0 kB\u001b[0m \u001b[31m6.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.5.3)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.4.0)\n",
            "Requirement already satisfied: protobuf<5,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.31.0)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.7.1)\n",
            "Requirement already satisfied: tenacity<9,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.2.3)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.10.0)\n",
            "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
            "  Downloading GitPython-3.1.42-py3-none-any.whl (195 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m195.4/195.4 kB\u001b[0m \u001b[31m21.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m41.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Collecting watchdog>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-4.0.0-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m83.0/83.0 kB\u001b[0m \u001b[31m10.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2023.4)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.6)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.34.0)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.1->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
            "Installing collected packages: watchdog, smmap, packaging, pydeck, gitdb, gitpython, streamlit\n",
            "  Attempting uninstall: packaging\n",
            "    Found existing installation: packaging 24.0\n",
            "    Uninstalling packaging-24.0:\n",
            "      Successfully uninstalled packaging-24.0\n",
            "Successfully installed gitdb-4.0.11 gitpython-3.1.42 packaging-23.2 pydeck-0.8.1b0 smmap-5.0.1 streamlit-1.32.2 watchdog-4.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st"
      ],
      "metadata": {
        "id": "g7teLCYaGE0W"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.title (\"Welcome to AI Assistant\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TR3zli2cGeml",
        "outputId": "6174ace6-b295-4848-f2f1-5fbaa7d3d4ad"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -q streamlit"
      ],
      "metadata": {
        "id": "foFBDNRzGe6m"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "\n",
        "x = st.slider('Select a value')\n",
        "st.write(x, 'squared is', x * x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3mFMRnQoOQcY",
        "outputId": "1e58b20d-b1e8-4168-906e-b184a47d1742"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!npm install localtunnel"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tMEHWkHmOQpR",
        "outputId": "72b32a7f-20d7-41dd-fe1d-a3063f6bc907"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[K\u001b[?25h\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m \u001b[0m\u001b[35msaveError\u001b[0m ENOENT: no such file or directory, open '/content/package.json'\n",
            "\u001b[K\u001b[?25h\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[34;40mnotice\u001b[0m\u001b[35m\u001b[0m created a lockfile as package-lock.json. You should commit this file.\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m \u001b[0m\u001b[35menoent\u001b[0m ENOENT: no such file or directory, open '/content/package.json'\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No description\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No repository field.\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No README data\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No license field.\n",
            "\u001b[0m\n",
            "+ localtunnel@2.0.2\n",
            "added 22 packages from 22 contributors and audited 22 packages in 2.273s\n",
            "\n",
            "3 packages are looking for funding\n",
            "  run `npm fund` for details\n",
            "\n",
            "found 1 \u001b[93mmoderate\u001b[0m severity vulnerability\n",
            "  run `npm audit fix` to fix them, or `npm audit` for details\n",
            "\u001b[K\u001b[?25h"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run /content/app.py &>/content/logs.txt &"
      ],
      "metadata": {
        "id": "uysS4W5tGfOH"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ZfcIWsjdOyVZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pathlib\n",
        "import textwrap\n",
        "\n",
        "import google.generativeai as genai\n",
        "\n",
        "from IPython.display import display\n",
        "from IPython.display import Markdown\n",
        "\n",
        "\n",
        "def to_markdown(text):\n",
        "  text = text.replace('•', '  *')\n",
        "  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))"
      ],
      "metadata": {
        "id": "9J4WwexuKcAi"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Used to securely store your API key\n",
        "from google.colab import userdata"
      ],
      "metadata": {
        "id": "Xs2Zwt1eKlyq"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.\n",
        "Google_API_KEY=userdata.get('Google_API_KEY')\n",
        "\n",
        "genai.configure(api_key=Google_API_KEY)"
      ],
      "metadata": {
        "id": "-n7XSBRpL0cE"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for m in genai.list_models():\n",
        "  if 'generateContent' in m.supported_generation_methods:\n",
        "    print(m.name)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 121
        },
        "id": "G7AnaIbuL0nM",
        "outputId": "0618daeb-f3cf-4979-822c-d85c054ff8ec"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "models/gemini-1.0-pro\n",
            "models/gemini-1.0-pro-001\n",
            "models/gemini-1.0-pro-latest\n",
            "models/gemini-1.0-pro-vision-latest\n",
            "models/gemini-pro\n",
            "models/gemini-pro-vision\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model = genai.GenerativeModel('gemini-pro')\n"
      ],
      "metadata": {
        "id": "6z70jLQvL0yp"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%%time\n",
        "response = model.generate_content(\"What do you think of Indian Weavers ?\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "id": "1iP7D80-M0jD",
        "outputId": "8540a661-e68f-4636-e4be-73fe4cec9b3d"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 143 ms, sys: 27.8 ms, total: 171 ms\n",
            "Wall time: 9.41 s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "to_markdown(response.text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 428
        },
        "id": "vtT5lmtnM0vB",
        "outputId": "395d9624-1937-4716-f76e-0b3361221566"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ],
            "text/markdown": "> Indian weavers are highly skilled artisans who create beautiful and intricate textiles. Their work is an important part of Indian culture and heritage.\n> \n> Indian weavers use a variety of techniques to create their textiles, including handloom weaving, power loom weaving, and embroidery. Handloom weaving is the most traditional method, and it involves using a hand-operated loom to create the fabric. Power loom weaving is a more modern method, and it uses a machine to create the fabric. Embroidery is a decorative technique that involves using a needle and thread to create designs on fabric.\n> \n> Indian textiles are known for their beauty and durability. They are often made from natural fibers, such as cotton, silk, and wool. Indian weavers use a variety of dyes to create their textiles, including natural dyes and synthetic dyes.\n> \n> Indian textiles are used for a variety of purposes, including clothing, home furnishings, and religious ceremonies. They are also popular with tourists, and they can be found in many shops and markets throughout India.\n> \n> Here are some of the benefits of using Indian textiles:\n> \n> * **Beauty:** Indian textiles are known for their beauty and intricate designs. They are available in a wide variety of colors and patterns, so you can find the perfect fabric for your needs.\n> * **Durability:** Indian textiles are made from high-quality materials, so they are durable and long-lasting. They can withstand wear and tear, and they will last for many years to come.\n> * **Versatility:** Indian textiles can be used for a variety of purposes, including clothing, home furnishings, and religious ceremonies. They are also popular with tourists, and they can be found in many shops and markets throughout India.\n> * **Sustainability:** Indian textiles are often made from natural fibers, so they are sustainable and environmentally friendly. They are also produced by skilled artisans, so you can be sure that you are supporting a fair trade industry.\n> \n> If you are looking for beautiful, durable, and versatile textiles, then you should consider using Indian textiles. They are a great way to add a touch of Indian culture to your home or wardrobe."
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "response = model.generate_content(\"What do you think of India ?\")\n",
        "to_markdown(response.text)"
      ],
      "metadata": {
        "id": "LXjTRiSXOz6k",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 428
        },
        "outputId": "2bc37ab7-6222-406f-f3a3-e7d92b4ba555"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ],
            "text/markdown": "> India is a fascinating and diverse country with a rich history and culture. It is the second-most populous country in the world, with over 1.3 billion people. India is also a land of contrasts, with some of the world's poorest and richest people living side by side.\n> \n> There are many things to love about India. The country is home to some of the world's most iconic landmarks, such as the Taj Mahal and the Red Fort. India is also a land of vibrant festivals, delicious food, and warm and welcoming people.\n> \n> However, there are also some challenges facing India. The country has a high rate of poverty and inequality, and there are significant issues with corruption and pollution. India also faces security challenges, both from within and from its neighbors.\n> \n> Despite these challenges, India is a country with enormous potential. The country has a strong economy and a growing middle class. India is also a major player in the global arena, and it is likely to play an increasingly important role in the years to come.\n> \n> Here are some of the things that I think make India a special place:\n> \n> * **The people:** Indians are some of the most welcoming and hospitable people in the world. They are always willing to help out a stranger, and they are always happy to share their culture and traditions.\n> * **The culture:** India is a land of vibrant and diverse cultures. There are over 22 official languages spoken in India, and each region has its own unique customs and traditions.\n> * **The food:** Indian food is some of the most delicious in the world. There is a wide variety of dishes to choose from, and each one is bursting with flavor.\n> * **The history:** India has a rich and fascinating history. The country has been home to some of the world's oldest civilizations, and it has been ruled by a variety of empires over the centuries.\n> * **The potential:** India is a country with enormous potential. The country has a strong economy and a growing middle class. India is also a major player in the global arena, and it is likely to play an increasingly important role in the years to come.\n> \n> Overall, I think India is a wonderful country with a lot to offer. It is a land of contrasts, but it is also a land of beauty, culture, and opportunity."
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    }
  ]
}