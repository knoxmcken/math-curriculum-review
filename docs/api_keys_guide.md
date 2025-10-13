# API Keys Guide - Phase 3 Requirements

**Last Updated:** October 13, 2025

---

## 🔑 Required API Keys

Before proceeding to Phase 3 (building agents), you need **at least ONE** of the following LLM provider API keys:

### **Option 1: OpenAI (Recommended)** ⭐
- **Key Name:** `OPENAI_API_KEY`
- **Used For:** CrewAI agents (primary LLM)
- **Model:** GPT-4 Turbo (or GPT-3.5 Turbo)
- **Status:** **REQUIRED** (unless using alternative)
- **Cost:** Pay-per-use (token-based pricing)

**Where to Get:**
1. Go to: https://platform.openai.com/api-keys
2. Sign up or log in to your OpenAI account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. Add to `.env` file

**Pricing:** ~$0.01 per 1K tokens (GPT-4 Turbo)

---

### **Option 2: Anthropic Claude** 
- **Key Name:** `ANTHROPIC_API_KEY`
- **Used For:** Alternative LLM provider
- **Model:** Claude 3 (Opus, Sonnet, or Haiku)
- **Status:** **OPTIONAL** (alternative to OpenAI)
- **Cost:** Pay-per-use (token-based pricing)

**Where to Get:**
1. Go to: https://console.anthropic.com/
2. Sign up for an account
3. Navigate to API Keys section
4. Generate a new API key
5. Add to `.env` file

**Pricing:** ~$0.015 per 1K tokens (Claude 3)

---

### **Option 3: Google Gemini**
- **Key Name:** `GOOGLE_API_KEY`
- **Used For:** Alternative LLM provider
- **Model:** Gemini Pro or Ultra
- **Status:** **OPTIONAL** (alternative to OpenAI)
- **Cost:** Free tier available, then pay-per-use

**Where to Get:**
1. Go to: https://ai.google.dev/
2. Sign in with Google account
3. Create a new API key in Google AI Studio
4. Copy the key
5. Add to `.env` file

**Pricing:** Free tier: 60 requests/minute

---

## 🔍 Optional API Keys

### **Tavily Search API** (Optional)
- **Key Name:** `TAVILY_API_KEY`
- **Used For:** Web search capabilities (if agents need external research)
- **Status:** **OPTIONAL**
- **Cost:** Free tier: 1,000 searches/month

**Where to Get:**
1. Go to: https://tavily.com/
2. Sign up for an account
3. Get your API key from the dashboard
4. Add to `.env` file

**Note:** Only needed if you want agents to search the web for additional information.

---

## 📝 How to Set Up Your API Keys

### Step 1: Create `.env` File

In your project root directory (`math-curriculum-review/`), create a file named `.env`:

```powershell
# From project root
New-Item -Path .env -ItemType File
```

### Step 2: Add Your API Keys

Open `.env` in a text editor and add your keys:

```env
# Required: Choose ONE of these LLM providers
OPENAI_API_KEY=sk-your-actual-openai-key-here
OPENAI_MODEL_NAME=gpt-4-turbo

# OR use Anthropic
# ANTHROPIC_API_KEY=your-actual-anthropic-key-here

# OR use Google
# GOOGLE_API_KEY=your-actual-google-key-here

# Optional: Web search
# TAVILY_API_KEY=your-actual-tavily-key-here

# Application Settings
LOG_LEVEL=INFO
DEBUG_MODE=False
```

### Step 3: Verify Setup

Run this command to verify your configuration:

```powershell
.\.venv\Scripts\Activate.ps1
python -c "from src.utils.config import Config; Config.validate(); print('✓ Configuration valid!')"
```

---

## ✅ Minimum Requirements for Phase 3

**You MUST have:**
- ✅ **At least ONE LLM API key** (OpenAI OR Anthropic OR Google)

**Recommended setup:**
- ✅ OpenAI API key (most tested with CrewAI)
- ✅ Model: `gpt-4-turbo` or `gpt-3.5-turbo`

**Optional:**
- ⬜ Tavily API key (for web search)
- ⬜ Alternative LLM as backup

---

## 💰 Estimated Costs for Phase 3

### Development & Testing Phase
**For building and testing 5 agents:**

**With GPT-4 Turbo:**
- Estimated tokens: ~100K - 500K tokens
- Cost: $1 - $5 for development
- Cost per review: ~$0.10 - $0.50

**With GPT-3.5 Turbo (cheaper):**
- Estimated tokens: ~100K - 500K tokens
- Cost: $0.10 - $0.50 for development
- Cost per review: ~$0.01 - $0.05

**Recommendation:** Start with GPT-3.5 Turbo for development, then use GPT-4 Turbo for production.

---

## 🔒 Security Best Practices

### DO ✅
- Store keys in `.env` file (already in `.gitignore`)
- Never commit `.env` to git
- Keep keys private and secure
- Use environment variables
- Rotate keys periodically

### DON'T ❌
- Hardcode keys in source code
- Share keys in chat/email
- Commit keys to GitHub
- Use production keys for testing
- Share `.env` file

---

## 🧪 Testing Your API Keys

Before Phase 3, verify your API key works:

### Test OpenAI Key:
```python
.\.venv\Scripts\Activate.ps1
python -c "
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'user', 'content': 'Say hello'}],
    max_tokens=10
)
print('✓ OpenAI API key is valid!')
print('Response:', response.choices[0].message.content)
"
```

### Test Configuration:
```python
.\.venv\Scripts\Activate.ps1
python -c "
from src.utils.config import Config
print('OpenAI Key set:', bool(Config.OPENAI_API_KEY))
print('Model:', Config.get_model_name())
Config.validate()
print('✓ All configuration valid!')
"
```

---

## 📊 API Key Status Checklist

Before proceeding to Phase 3, ensure:

- [ ] I have created a `.env` file in the project root
- [ ] I have added at least ONE LLM API key
- [ ] My `.env` file is NOT tracked by git (check `.gitignore`)
- [ ] I have tested my API key and it works
- [ ] I understand the estimated costs
- [ ] I have set my preferred model name

---

## 🆘 Troubleshooting

### Problem: "No API key configured"
**Solution:** Make sure your `.env` file is in the project root and contains a valid API key.

### Problem: "Invalid API key"
**Solution:** 
1. Verify you copied the entire key
2. Check for extra spaces
3. Ensure key is active (not revoked)
4. Try generating a new key

### Problem: "Rate limit exceeded"
**Solution:**
1. Wait a few minutes
2. Use a different API key
3. Upgrade your API plan

### Problem: "Import error with Config"
**Solution:**
```powershell
.\.venv\Scripts\Activate.ps1
python -c "from src.utils.config import Config; print('OK')"
```

---

## 📞 Support Resources

### OpenAI
- Documentation: https://platform.openai.com/docs
- API Keys: https://platform.openai.com/api-keys
- Pricing: https://openai.com/pricing

### Anthropic
- Documentation: https://docs.anthropic.com/
- Console: https://console.anthropic.com/

### Google AI
- Documentation: https://ai.google.dev/docs
- AI Studio: https://makersuite.google.com/

### CrewAI
- Documentation: https://docs.crewai.com/
- GitHub: https://github.com/joaomdmoura/crewAI

---

## ✨ Quick Start Checklist

Ready for Phase 3? Check these items:

**Environment:**
- [x] Virtual environment activated
- [x] All dependencies installed
- [x] Phase 1 & 2 complete

**API Keys:**
- [ ] `.env` file created
- [ ] LLM API key added (OpenAI/Anthropic/Google)
- [ ] API key tested and validated
- [ ] Model name configured

**Optional:**
- [ ] Tavily API key (if using web search)
- [ ] Backup LLM API key

**Once all checked, you're ready to build agents!** 🚀

---

## 📋 Template `.env` File

Copy this template and fill in your keys:

```env
# ===========================================
# Math Curriculum Review - API Configuration
# ===========================================

# LLM Provider (Choose ONE)
# --------------------------
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL_NAME=gpt-4-turbo

# Alternative LLM Providers (Optional)
# ANTHROPIC_API_KEY=your-key-here
# GOOGLE_API_KEY=your-key-here

# Optional Services
# -----------------
# TAVILY_API_KEY=your-key-here

# Application Settings
# --------------------
LOG_LEVEL=INFO
DEBUG_MODE=False

# ===========================================
# DO NOT COMMIT THIS FILE TO GIT!
# ===========================================
```

---

**Ready to get your API keys?** Follow the instructions above for your chosen provider, then we can proceed to Phase 3! 🎯
