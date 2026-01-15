# Deployment Guide

## Export Requirements

```bash
poetry export -f requirements.txt --without-hashes --output requirements.txt \
  --extras cv --extras ml --extras ocr --extras api
```
