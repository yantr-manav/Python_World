# MCP Scraper with LangGraph, LangChain-Ollama, and MCP Tools

This project is an intelligent agent-powered scraper/chatbot built using [LangGraph](https://docs.langchain.com/langgraph/), [LangChain-Ollama](https://js.langchain.com/docs/integrations/chat/ollama), and [BrightData MCP](https://brightdata.com/). The AI assistant can search, scrape, and provide useful data in real time using browser-based tools.

---

## 🧠 What This Script Does

This script sets up a conversational AI assistant using:

- ✅ `Ollama` local model (`mistral`) via `langchain_ollama`
- ✅ `LangGraph` for managing multi-step agent workflows
- ✅ `BrightData MCP` scraping and search tools via `@brightdata/mcp`
- ✅ `MCP tools` like `search_engine` and `scrape_as_markdown`
- ✅ A `ReAct`-style agent that dynamically decides when and how to use the tools

---

## 🧩 Core Features

- 🚀 Asks real-time factual queries (e.g., “Find the best YouTube tutorial for LangGraph”)
- 🧰 Automatically chooses between tools like search and web scraping
- 🧼 Cleans and returns scraped data as markdown
- 🔁 Maintains conversational context
- 🌐 Works with BrightData's web unlocking tools for hard-to-reach content

---

## 📁 File Structure

MCP_Scraper/
│
├── .env # Stores API tokens and other secrets
├── run_ollama.py # Main Python script (formerly ollama.py)
├── README.md # You're reading this!
└── ...

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/MCP_Scraper.git
cd MCP_Scraper
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv .venv
Activate it:

Windows:

bash
Copy
Edit
.venv\Scripts\activate
macOS/Linux:

bash
Copy
Edit
source .venv/bin/activate
3. Install Dependencies (using uv or pip)
If using uv:

bash
Copy
Edit
uv pip install -r requirements.txt
Or with pip:

bash
Copy
Edit
pip install -r requirements.txt
Make sure you have:

txt
Copy
Edit
langchain
langgraph
langchain-ollama
langchain-mcp-adapters
python-dotenv
4. Install BrightData MCP CLI
You must have Node.js installed.

bash
Copy
Edit
npm install -g @brightdata/mcp
5. Set Environment Variables
Create a .env file:

env
Copy
Edit
API_TOKEN=your_brightdata_api_token
BROWSER_AUTH=your_browser_profile_or_auth
WEB_UNLOCKER_ZONE=your_web_unlocker_zone_name
6. Rename the Script (if needed)
Make sure your script is not named ollama.py, since that conflicts with the ollama Python package. Rename it to something like run_ollama.py.

7. Run the Script
bash
Copy
Edit
uv run run_ollama.py
Or:

bash
Copy
Edit
python run_ollama.py
💬 How to Use the Agent
Once the agent is running, interact with it via the terminal:

bash
Copy
Edit
You: Find a tutorial on LangGraph
Agent: [AI fetches search results or scrapes data]
To exit:

bash
Copy
Edit
You: exit
📌 How It Works
The ChatOllama object loads the local mistral model.

MCP tools (like scraping and searching) are dynamically loaded.

A ReAct agent is built using LangGraph to plan and execute reasoning steps.

Input is processed in a loop and routed through the agent for dynamic responses.

Results are printed back to the terminal.

🛠️ Troubleshooting
❗ ImportError for ChatOllama: Make sure your file is not named ollama.py.

❗ .env not loaded: Ensure you run from the directory where .env exists or set full paths.

❗ Ollama not installed: Download Ollama from https://ollama.com/ and install models like mistral.

✅ Requirements
Python 3.8+

Ollama (local LLMs)

BrightData MCP CLI

Node.js (for MCP tools)

Internet connection (for scraping/searching)

🧠 Credits
Built using:

LangChain

LangGraph

Ollama

BrightData MCP

yaml
Copy
Edit

---

This file provides a comprehensive breakdown of the project, its structure, installation, and usage in one place.







