# ⚠️ API KEYS NEEDED BEFORE PHASE 3

## Quick Reference

### ✅ REQUIRED: Choose ONE

| Provider | Key Name | Get It | Cost |
|----------|----------|--------|------|
| **OpenAI** ⭐ | `OPENAI_API_KEY` | [platform.openai.com](https://platform.openai.com/api-keys) | $1-5 for Phase 3 |
| Anthropic | `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com/) | Similar |
| Google | `GOOGLE_API_KEY` | [ai.google.dev](https://ai.google.dev/) | Free tier |

### ⬜ OPTIONAL

| Provider | Key Name | Purpose |
|----------|----------|---------|
| Tavily | `TAVILY_API_KEY` | Web search for agents |

---

## 🚀 Quick Setup

1. **Create `.env` file:**
   ```powershell
   # In project root
   New-Item -Path .env -ItemType File
   ```

2. **Add your key:**
   ```env
   OPENAI_API_KEY=sk-your-actual-key-here
   OPENAI_MODEL_NAME=gpt-4-turbo
   ```

3. **Test it:**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   python -c "from src.utils.config import Config; Config.validate(); print('✓ Ready!')"
   ```

---

## 📚 Full Documentation

See [`docs/api_keys_guide.md`](docs/api_keys_guide.md) for:
- Detailed setup instructions
- Cost estimates
- Security best practices
- Troubleshooting
- All provider options

---

**Status:** ⏸️ Waiting for API keys before Phase 3
