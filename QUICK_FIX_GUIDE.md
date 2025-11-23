# 🚨 Quick Fix: API Key Error on Streamlit Cloud

## The Error You're Seeing

```
Initialization failed: The api_key client option must be set either by passing 
api_key to the client or by setting the OPENAI_API_KEY environment variable
```

## ✅ IMMEDIATE FIX (3 Steps)

### Step 1: Go to Streamlit Cloud
1. Visit https://share.streamlit.io/
2. Click on your **Sage-Lens** app
3. Click **"Settings"** (gear icon ⚙️)

### Step 2: Add Secrets
1. Click **"Secrets"** tab
2. Paste this EXACT format:

```toml
[secrets]
OPENAI_API_KEY = "sk-proj-..."
ANTHROPIC_API_KEY = "sk-ant-api03-..."
TAVILY_API_KEY = "tvly-dev-..."
SERPER_API_KEY = "your-serper-key-here"
```

### Step 3: Save and Wait
1. Click **"Save"** button
2. Wait 10-30 seconds for app to restart
3. Refresh your app page
4. ✅ **It should work now!**

## 🔍 Verify It Worked

After saving secrets:
- ✅ No more "Initialization failed" error
- ✅ App loads without errors
- ✅ You can enter a research topic
- ✅ Generate button works

## ⚠️ Still Not Working?

### Check These:

1. **Secret Names Must Match Exactly** (case-sensitive):
   - ✅ `OPENAI_API_KEY` (not `openai_api_key` or `OpenAI_API_Key`)
   - ✅ `ANTHROPIC_API_KEY` (not `anthropic_api_key`)

2. **No Extra Spaces**:
   - ✅ `OPENAI_API_KEY = "sk-proj-..."`
   - ❌ `OPENAI_API_KEY = " sk-proj-..."` (space before key)
   - ❌ `OPENAI_API_KEY="sk-proj-..."` (no space around =)

3. **Keys Must Be Complete**:
   - Make sure you copied the ENTIRE key (they're very long)
   - Keys should start with `sk-proj-` (OpenAI) or `sk-ant-api03-` (Anthropic)

4. **App Must Restart**:
   - After saving, wait at least 10 seconds
   - Check the app logs for any errors
   - Try refreshing the page

## 📝 Alternative: Check App Logs

1. In Streamlit Cloud, click **"Manage app"**
2. Click **"Logs"** tab
3. Look for any error messages
4. The logs will show if secrets are being loaded

## 🆘 Still Having Issues?

1. **Double-check the secret format** - it must be TOML format
2. **Verify keys are active** in OpenAI/Anthropic dashboards
3. **Try removing and re-adding** the secrets
4. **Check the app is using the latest code** (pull from GitHub)

---

**After following these steps, your app should work! 🎉**

