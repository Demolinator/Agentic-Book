# ✅ Pre-Deployment Checklist

**Date**: 2025-11-29
**Status**: Ready to deploy!

---

## 🎯 Deployment Strategy

**Phase 1** (NOW - 30 minutes):
1. Get API credentials
2. Deploy backend to Railway
3. Deploy frontend to GitHub Pages
4. Test production

**Phase 2** (After testing - 2 hours):
1. Add translation UI to frontend
2. Redeploy frontend
3. Create history records

**Phase 3** (Final - 30 minutes):
1. Record demo video
2. Submit to hackathon

---

## ✅ Pre-Deployment Verification

### Backend Readiness
- [x] **Tests passing**: 12/12 ✅
- [x] **Translation API**: Integrated ✅
- [x] **Railway config**: `backend/railway.toml` ✅
- [x] **Render config**: `backend/render.yaml` ✅
- [x] **Environment variables**: Documented in `.env.example` ✅
- [x] **Dependencies**: `requirements.txt` complete ✅

### Frontend Readiness
- [x] **Tests passing**: 20/20 ✅
- [x] **Build works**: Docusaurus configured ✅
- [x] **GitHub Pages**: Workflow ready ✅
- [x] **Config file**: `src/config.js` exists ✅
- [x] **All 22 chapters**: Content complete ✅

### Infrastructure
- [x] **CI/CD**: `.github/workflows/test.yml` ✅
- [x] **CI/CD**: `.github/workflows/deploy.yml` ✅
- [x] **Documentation**: Deployment guides ✅
- [x] **Skills**: 4 Claude Code skills ✅

---

## 📋 API Credentials Needed

### 1. OpenAI API Key
**Get from**: https://platform.openai.com/api-keys

**Format**: `sk-proj-...`

**Cost**: ~$0.30 for initial ingestion + ~$0.10 for demo

**Your Key**: ___________________________________________

---

### 2. Qdrant Vector Database
**Get from**: https://cloud.qdrant.io

**Sign up**: Free tier (1GB storage, perfect for this project)

**Create**:
- Cluster name: `physical-ai-textbook`
- Region: Choose closest to you
- Free tier

**Your Credentials**:
- Cluster URL: ___________________________________________
- API Key: ___________________________________________

---

### 3. Neon Serverless Postgres
**Get from**: https://neon.tech

**Sign up**: Free tier (3GB storage)

**Create**:
- Project name: `physical-ai-textbook`
- Database name: `textbook`
- Region: Choose closest

**Your Connection String**:
```
postgresql://user:password@host.region.neon.tech/dbname?sslmode=require
```

___________________________________________

---

### 4. Auth Secret
**Generate** (Windows PowerShell):
```powershell
[System.Convert]::ToBase64String([System.Security.Cryptography.RandomNumberGenerator]::GetBytes(32))
```

**OR use**: https://generate-secret.vercel.app/32

**Your Secret** (32+ characters):

___________________________________________

---

## 🚀 Quick Deployment Commands

### Install Railway CLI
```bash
npm i -g @railway/cli
```

### Deploy Backend
```bash
cd backend
railway login
railway init
railway variables set BETTER_AUTH_SECRET="<your-secret>"
railway variables set OPENAI_API_KEY="<your-key>"
railway variables set QDRANT_URL="<your-url>"
railway variables set QDRANT_API_KEY="<your-key>"
railway variables set NEON_DATABASE_URL="<your-connection-string>"
railway up
railway domain  # Get your backend URL
```

### Update Frontend & Deploy
```bash
# Edit frontend/src/config.js with your Railway URL
# Then:
git add frontend/src/config.js
git commit -m "Configure production backend URL"
git push origin gh-pages
```

### Ingest Documentation
```bash
curl -X POST https://your-app.railway.app/ingest
```

---

## 🧪 Production Testing Checklist

### Backend Tests
```bash
# Replace YOUR-RAILWAY-URL with actual URL

# 1. Health check
curl https://YOUR-RAILWAY-URL/ping
# Expected: {"status":"ok"}

# 2. Skills list
curl https://YOUR-RAILWAY-URL/skills
# Expected: {"skills": [...]}

# 3. Translation test
curl -X POST https://YOUR-RAILWAY-URL/translate \
  -H "Content-Type: application/json" \
  -d '{"content": "Hello robot!", "target_language": "ur"}'
# Expected: {"translated": "ہیلو روبوٹ!", ...}
```

### Frontend Tests
- [ ] Homepage loads
- [ ] All 22 chapters accessible
- [ ] Navigation works
- [ ] RAG chatbot responds
- [ ] Source citations appear

---

## 📝 URLs to Save

### Production URLs

**Backend (Railway)**:
```
https://_____________________
```

**Frontend (GitHub Pages)**:
```
https://_____________________
```

**Qdrant Dashboard**:
```
https://cloud.qdrant.io/dashboard
```

**Neon Dashboard**:
```
https://console.neon.tech/app/projects
```

**Railway Dashboard**:
```
https://railway.app/dashboard
```

---

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Get API credentials | 10 min |
| Deploy backend (Railway) | 10 min |
| Update frontend config | 2 min |
| Deploy frontend (GitHub Pages) | 5 min |
| Ingest documentation | 2 min |
| Test production | 10 min |
| **PHASE 1 TOTAL** | **~40 min** |
| | |
| Add translation UI (frontend) | 2 hours |
| Redeploy frontend | 5 min |
| Create history records | 20 min |
| **PHASE 2 TOTAL** | **~2.5 hours** |
| | |
| Record demo video | 30 min |
| Submit to hackathon | 10 min |
| **PHASE 3 TOTAL** | **~40 min** |
| | |
| **GRAND TOTAL** | **~4 hours** |

---

## 💰 Cost Breakdown

### One-Time Costs
- OpenAI ingestion: ~$0.30
- OpenAI demo testing: ~$0.10
- **Total one-time**: **~$0.40**

### Ongoing (Free Tier)
- Railway: Free ($5/month credit)
- Neon: Free (3GB)
- Qdrant: Free (1GB)
- GitHub Pages: Free
- **Total monthly**: **$0**

---

## 🆘 Common Issues & Fixes

### Issue: Railway build fails
**Fix**:
```bash
# Check logs
railway logs

# Verify Python version in requirements
# Should have: python-version==3.11 or compatible
```

### Issue: Frontend shows "Failed to fetch"
**Fix**:
```bash
# Verify backend URL in frontend/src/config.js
# Check CORS settings in backend/src/api/main.py
# Ensure your frontend URL is in allow_origins
```

### Issue: Ingestion fails
**Fix**:
```bash
# Verify OPENAI_API_KEY is set
railway variables | grep OPENAI

# Check Qdrant connection
curl -H "api-key: YOUR_KEY" https://your-qdrant-url:6333/collections
```

### Issue: RAG returns no results
**Fix**:
```bash
# Re-run ingestion
curl -X POST https://your-app.railway.app/ingest

# Check Qdrant has vectors
# Visit: https://cloud.qdrant.io/dashboard
# Check collection: textbook_chapters
```

---

## 📞 Support Resources

- **Railway Docs**: https://docs.railway.app
- **Neon Docs**: https://neon.tech/docs
- **Qdrant Docs**: https://qdrant.tech/documentation
- **Your Deployment Guide**: `DEPLOYMENT_GUIDE.md`
- **Execution Plan**: `DEPLOYMENT_EXECUTION_PLAN.md`

---

## 🎬 Ready to Deploy!

### Start with Step 1:
```bash
npm i -g @railway/cli
railway login
```

### Then follow:
`DEPLOYMENT_EXECUTION_PLAN.md`

---

**Good luck! 🚀**
