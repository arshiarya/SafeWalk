# SafeWalk Deployment Guide

## 📋 Pre-Deployment Checklist

- [x] Environment variables configured
- [x] No hardcoded localhost URLs
- [x] API endpoint uses environment variables
- [x] CORS properly configured
- [x] Backend has health check endpoint
- [x] Frontend build optimized

---

## 🚀 Deployment Options

### **Option 1: Deploy on Render (Recommended - Free Tier Available)**

#### Backend Deployment (Render.com)

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Deploy Backend**
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Configuration:
     ```
     Build Command: pip install -r requirements.txt
     Start Command: uvicorn main:app --host 0.0.0.0 --port 8000
     Environment: Python 3.11
     Root Directory: backend
     ```
   - Add Environment Variables:
     ```
     FRONTEND_URL=https://your-frontend-domain.com
     ```
   - Deploy

3. **Note Backend URL**
   - Format: `https://safewalk-api.onrender.com`

#### Frontend Deployment (Render Static Site / Netlify / Vercel)

**Option A: Using Vercel (Easiest)**
1. Go to https://vercel.com
2. Import your GitHub project
3. Select `SafeWalk/frontend` as root directory
4. Environment Variables:
   ```
   VITE_API_URL=https://safewalk-api.onrender.com
   ```
5. Deploy

**Option B: Using Netlify**
1. Go to https://netlify.com (or use Vercel - same process)
2. Connect GitHub repository
3. Build settings:
   ```
   Build command: npm run build
   Publish directory: dist
   Root directory: frontend
   ```
4. Environment Variables:
   ```
   VITE_API_URL=https://your-backend-url.com
   ```
5. Deploy

**Option C: Using Render Static**
1. Create `render.yaml` in root directory (see below)
2. Link GitHub and deploy

---

### **Option 2: Deploy on AWS (Production)**

#### Backend (AWS EC2 or Elastic Beanstalk)

1. **Using Elastic Beanstalk:**
   ```bash
   # Install EB CLI
   pip install awsebcli
   
   # Initialize
   cd SafeWalk/backend
   eb init -p python-3.11 safewalk-api
   
   # Create environment
   eb create safewalk-api-env
   
   # Deploy
   eb deploy
   ```

2. **Environment Variables:**
   ```
   FRONTEND_URL=https://your-cloudfront-domain.com
   ```

#### Frontend (AWS S3 + CloudFront)

1. **Build Frontend:**
   ```bash
   cd SafeWalk/frontend
   npm run build
   ```

2. **Upload to S3:**
   ```bash
   aws s3 sync dist/ s3://your-bucket-name --delete
   ```

3. **CloudFront Distribution:**
   - Point to S3 bucket
   - Set `VITE_API_URL` in environment

---

### **Option 3: Docker Deployment (Recommended for Production)**

#### Create Docker Files

1. **Backend Dockerfile** (`SafeWalk/backend/Dockerfile`)
   ```dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY . .
   
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. **Frontend Dockerfile** (`SafeWalk/frontend/Dockerfile`)
   ```dockerfile
   FROM node:20-alpine as builder
   
   WORKDIR /app
   
   COPY package*.json ./
   RUN npm ci
   
   COPY . .
   RUN npm run build
   
   FROM nginx:alpine
   
   COPY --from=builder /app/dist /usr/share/nginx/html
   COPY nginx.conf /etc/nginx/conf.d/default.conf
   
   EXPOSE 80
   ```

3. **Docker Compose** (`SafeWalk/docker-compose.yml`)
   ```yaml
   version: '3.8'
   
   services:
     backend:
       build: ./backend
       ports:
         - "8000:8000"
       environment:
         - FRONTEND_URL=http://frontend
       restart: unless-stopped
   
     frontend:
       build: ./frontend
       ports:
         - "3000:80"
       environment:
         - VITE_API_URL=http://backend:8000
       depends_on:
         - backend
       restart: unless-stopped
   ```

4. **Deploy:**
   ```bash
   docker-compose up -d
   ```

---

## 🔧 Configuration Files Setup

### For Vercel/Netlify Deployment:

1. **Frontend .env.production**
   ```
   VITE_API_URL=https://your-backend-url.com
   ```

2. **Backend .env.production**
   ```
   FRONTEND_URL=https://your-frontend-url.com
   HOST=0.0.0.0
   PORT=8000
   ```

---

## ✅ Pre-Flight Checks

Before deploying, run:

### Backend Tests
```bash
cd SafeWalk/backend
python -m pytest  # if tests exist
python main.py   # Test startup
```

### Frontend Build Test
```bash
cd SafeWalk/frontend
npm run build    # Should complete without errors
npm run preview  # Test production build locally
```

---

## 🚨 Common Deployment Issues & Fixes

| Issue | Solution |
|-------|----------|
| CORS errors | Ensure backend includes frontend URL in CORS origins |
| API 404 | Check `VITE_API_URL` env variable in frontend |
| Map not loading | Verify leaflet CSS is imported |
| Build fails | Run `npm install` in frontend directory |
| Backend crashes | Check requirements.txt is complete - run `pip list` |
| Timeout on map load | First load takes 2-5 min (Delhi map download) - this is normal |

---

## 📝 Health Check URLs

After deployment:
- Backend: `https://your-backend/health` → Should return `{"status": "ok"}`
- Frontend: Load main domain → Should show SafeWalk UI

---

## 🔄 Post-Deployment

1. **Test API Endpoint:**
   ```bash
   curl "https://your-backend/route?start_lat=28.5447&start_lon=77.1642&end_lat=28.6139&end_lon=77.2090"
   ```

2. **Monitor Logs:**
   - Render: Dashboard → Logs
   - Vercel: Dashboard → Function Logs
   - AWS: CloudWatch
   - Docker: `docker logs <container-id>`

3. **Setup Monitoring:**
   - Enable error tracking (Sentry recommended)
   - Setup uptime monitoring (StatusPage.io)

---

## 📞 Support

If you encounter deployment issues:
1. Check application logs
2. Verify environment variables
3. Ensure ports are open (8000 for backend, 3000/80 for frontend)
4. Check CORS origins match your domain

---

**Deployment Date:** ___________
**Backend URL:** ___________
**Frontend URL:** ___________
