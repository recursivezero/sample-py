# 🔪 Threadzip API Manual Test Guide

This guide contains all `curl` commands to test your FastAPI endpoints locally at `http://127.0.0.1:5000`.

---

## 1. Health Check

```cmd
curl http://127.0.0.1:5000/health
```

### ⏱️ Loop to exceed rate limit (CMD)

```cmd
for /L %i in (1,1,100) do curl http://127.0.0.1:5000/health
```

---

## 2. Home Page (HTML)

```cmd
curl http://127.0.0.1:5000/
```

---

## 3. Rate Limit Info

```cmd
curl http://127.0.0.1:5000/rate-limit-info
```

---

## 4. Create Table (PUT)

```cmd
curl -X PUT http://127.0.0.1:5000/api/v1/create/table
```

---

## 5. Update Table (PUT)

```cmd
curl -X PUT http://127.0.0.1:5000/api/v1/update/table
```

---

## 6. Search Endpoint

### a. Text-Based Search

```cmd
curl -X POST http://127.0.0.1:5000/api/v1/search -F "search_term=blue pattern" -F "limit=10"
-F "page=1" -F "per_page=10"
```

### b. Image Search

```cmd
curl -X POST http://127.0.0.1:5000/api/v1/search -F "file=@path\to\image.jpg" -F "limit=10"
-F "page=1" -F "per_page=10"
```

> Replace `path\to\image.jpg` with a valid path on your machine.

---

## 7. Analyze Fabric

```cmd
curl -X POST http://127.0.0.1:5000/api/v1/analyze/fabric -F "file=@path\to\fabric.jpg" -F "analysis_type=short"
```

---

## 8. Process Fabric Images

```cmd
curl -X POST http://127.0.0.1:5000/api/v1/process/fabric -F "single_image=@path\to\single.jpg"
-F "group_image=@path\to\group.jpg"
-F "mode=Fabric Mask (Smooth Blend)"
```

---

## 🔁 Loop Test for Rate Limiting

### Text Search Loop (100 Requests)

```cmd
for /L %i in (1,1,100) do curl -X POST http://127.0.0.1:5000/api/v1/search -F "search_term=test %i"
-F "limit=10" -F "page=1"
-F "per_page=10"
```

> Customize `%i` to test dynamic input. Expect 429 (Too Many Requests) after rate limit is hit.

---

## ✅ Tips

- Run these commands in **Windows CMD**
- Do **not use `\` for multi-line** in CMD. Combine all options on one line.
- Use `timeout /t 1 >nul` between requests if you want delays.

---
