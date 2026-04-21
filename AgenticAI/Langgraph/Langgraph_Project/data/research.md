# 🚀 LangGraph + Vertex AI (Gemini) Starter Project

This project demonstrates how to build a modular and extensible **LLM integration layer** using  **LangGraph + LangChain + Google Vertex AI (Gemini)** .

It includes:

* ✅ A reusable `<span>get_llm()</span>` factory module
* ✅ Notebook usage for quick experimentation
* ✅ Integration with Vertex AI (Gemini Flash Lite)
* ✅ Extensible design for multi-provider support

---

# 📦 Project Structure

```
.
├── llm_factory.py        # LLM factory module
├── notebook.ipynb       # Example usage in Jupyter Notebook
├── .env                 # Environment variables (not committed)
└── README.md            # Project documentation
```

---

# 🧠 Features

### 🔹 LLM Factory (`<span>get_llm</span>`)

* Returns a `<span>BaseChatModel</span>` instance
* Supports Google Gemini (Vertex AI)
* Easily extendable for:
  * OpenAI
  * Azure OpenAI
  * Anthropic

---

# ⚙️ Prerequisites

* Python 3.10+
* Google Cloud account
* Billing enabled on your project
* Vertex AI API enabled

---

# 🔐 Authentication Setup

Run this once:

```
gcloud auth application-default login
```

---

# 🌍 Environment Setup

Create a `<span>.env</span>` file:

```
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```

---

# 📥 Installation

```
pip install -r requirements.txt
```

Or manually:

```
pip install langchain langgraph langchain-google-genai google-cloud-aiplatform python-dotenv
```

---

# 🏗️ LLM Factory Implementation

`<span>llm_factory.py</span>` provides a centralized way to initialize LLMs.

### Example:

```
from llm_factory import get_llm

llm = get_llm("gemini-2.5-flash-lite")
```

---

# 📓 Notebook Usage

### Step 1: Import

```
from llm_factory import get_llm, LLMConfig
```

---

### Step 2: Configure

```
config = LLMConfig(
    project="your-project-id",
    location="us-central1",
    temperature=0.3
)
```

---

### Step 3: Initialize LLM

```
llm = get_llm(
    model="gemini-2.5-flash-lite",
    provider="google",
    config=config
)
```

---

### Step 4: Test

```
response = llm.invoke("Explain LangGraph in 2 lines")
print(response.content)
```

---

# 🔗 LangGraph Integration

You can directly use the LLM inside LangGraph nodes:

```
def llm_node(state):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}
```

---

# 🔄 Extending to Other Providers

Example: Add OpenAI support in `<span>llm_factory.py</span>`

```
elif provider == "openai":
    from langchain_openai import ChatOpenAI
    return ChatOpenAI(model=model)
```

---

# ⚠️ Common Issues

### ❌ Billing not enabled

```
403 PERMISSION_DENIED: BILLING_DISABLED
```

✔️ Fix: Enable billing in GCP project

---

### ❌ Module not found

```
ModuleNotFoundError: langchain_google_genai
```

✔️ Fix:

```
pip install langchain-google-genai
```

---

### ❌ Authentication error

✔️ Fix:

```
gcloud auth application-default login
```

---

# 🚀 Future Improvements

* [ ] Add multi-model routing
* [ ] Add fallback models
* [ ] Add streaming support
* [ ] Add memory (LangGraph checkpoints)
* [ ] Deploy on Cloud Run

---

# 🤝 Contributing

Feel free to extend the factory for additional providers or improve the architecture.

---

# 📄 License

This project is for learning and experimentation purposes.
