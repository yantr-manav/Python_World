# MCP Scraper with LangGraph, LangChain-Ollama, and MCP Tools

An intelligent, AI-powered web scraper and chatbot that combines the power of [LangGraph](https://docs.langchain.com/langgraph/), [LangChain-Ollama](https://js.langchain.com/docs/integrations/chat/ollama), and [BrightData MCP](https://brightdata.com/). This assistant can search, scrape, and provide data in real-time using browser-based tools.

---

## 🧠 What This Script Does

This project sets up a conversational AI assistant capable of:

- ✅ Utilizing the `Ollama` local model (`mistral`) via `langchain_ollama`
- ✅ Managing multi-step agent workflows with `LangGraph`
- ✅ Scraping and searching with `BrightData MCP` tools
- ✅ Using tools like `search_engine` and `scrape_as_markdown`
- ✅ Employing a `ReAct`-style agent to dynamically decide tool usage

---

## 🧩 Core Features

- 🚀 Real-time factual queries (e.g., “Find the best YouTube tutorial for LangGraph”)
- 🧰 Automatic selection of tools like search and web scraping
- 🧼 Clean markdown output for scraped data
- 🔁 Maintains conversational context
- 🌐 Unlocks hard-to-reach web content with BrightData tools

---

## 📁 File Structure

```plaintext
MCP_Scraper/
│
├── .env               # Stores API tokens and other secrets
├── run_ollama.py      # Main Python script (formerly ollama.py)
├── README.md          # You're reading this!
└── ...
```
---
## ⚙️ Setup Instructions
### 1. Clone the Repository
``` bash
git clone https://github.com/your-username/MCP_Scraper.git
cd MCP_Scraper
```
---
### 2. Create a Virtual Environment
   ```bash
   python -m venv .venv
   ```
   Activate it:
   ### Windows:
   ```bash
   .venv\Scripts\activate
   ```
   ### macOS/Linux:
   ```bash
   source .venv\bin\activate
   ```
### 3.Install Dependencies
   If using `uv` :
   ```bash
   uv pip install -r requirements.txt
   ```
   Or with `pip`:
   ``` bash
   pip install -r requirements.txt
   ```
   Make sure you have the following packages installed :
   - `langchain`
   - `langgraph`
   - `langchain-ollama`
   - `langchain-mcp-adapters`
   - `python-dotenv`

### 4. Install BrightData MCP CLI
   You must have Node.js installed:
   ```bash
   npm install -g @brightdata/mcp
   ```
### 5. Set Environment Variables
    Create a `.env` file with the following :
   ```env
   API_TOKEN=your_brightdata_api_token
   BROWSER_AUTH=your_browser_profile_or_auth
   WEB_UNLOCKER_ZONE=your_web_unlocker_zone_name
   ```
### 6. Run the Script
   Using `uv`:
   ```bash
   uv run main.py
   ```
   Or with `python`:
   ```bash
   python main.py
   ```
   ---

   ##💬 How to Use the Agent
   ---
   Once the agent is running, interact with it via terminal:
   ```bash
   You: Find a tutorial on LangGraph
   Agent: [AI fetches search results or scrapes data]
   ```
   To exit, type:
   ```bash
   You: exit
   ```
   ---
   ## 📌 How It Works
1. The `ChatOllama` object loads the local `mistral` model.

2. MCP tools (e.g., `search_engine`, `scrape_as_markdown`) are dynamically loaded.

3. A `ReAct` agent is created using `LangGraph` to plan and execute reasoning steps.

4. Input is processed in a loop and routed through the agent for dynamic responses.
   
5. Results are displayed in the terminal.



---
## ✅ Requirements
- Python 3.8+
- Ollama (local LLMs)
- BrightData MCP CLI
- Node.js (for MCP tools)
