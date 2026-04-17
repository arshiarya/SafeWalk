# 🚀 Quick Deployment Guide (5 Minutes)

## Choose Your Platform

### **Easiest: Vercel + Render (Recommended)**

#### Step 1: Deploy Backend (Render.com) - 2 minutes

1. Sign up at https://render.com
2. Create new Web Service
3. Connect GitHub and select `SafeWalk` repo
4. Fill in:
   - **Root Directory:** `backend` (NOT SafeWalk/backend)
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 8000`
5. Add Environment Variable: `FRONTEND_URL` = (leave blank for now)
6. Click **Deploy**
7. Copy the deployed URL (e.g., `https://safewalk-api.onrender.com`)

#### Step 2: Deploy Frontend (Vercel) - 2 minutes

1. Sign up at https://vercel.com
2. Import GitHub repo
3. Select **Framework:** React
4. Select **Root directory:** `frontend` (NOT SafeWalk/frontend)
5. Add Environment Variable: `VITE_API_URL` = (paste backend URL from Step 1)
6. Click **Deploy**
7. Copy frontend URL

#### Step 3: Update Backend CORS - 1 minute

1. Go back to Render dashboard
2. Go to Backend service settings
3. Update environment variable: `FRONTEND_URL` = (paste frontend URL from Step 2)
4. Service will redeploy automatically

✅ **Done!** Your app is live.

---

## Troubleshooting Quick Fixes

### API not responding?
- Check if backend has finished loading Django map (2-5 min first time)
- Verify `VITE_API_URL` in Vercel environment matches deployed backend

### Map not showing?
- Make sure leaflet CSS is loaded (should be automatic)
- Check browser console for errors

### Routes not loading?
- Wait 5+ minutes for first-time map data download
- Check network tab - API call should return 200 status

---

## Alternative One-Click Deployments

**Railway.app:**
```
git push  
- Connects automatically
- Paste URL in frontend env
Done!
```

**Replit:**
```
Fork project → Run → Share URL
```

---

## Performance Tips

- Frontend build: ~1 MB (after gzip)
- Backend: ~500 MB RAM needed (for Delhi map)
- First API call: 2-5 minutes (map download)
- Subsequent calls: < 2 seconds

**Recommended Render Plan:** Starter Plan ($7/month) is sufficient

