# Automated Visual Inspection — Color Detection

This repository contains a small color-detection utility and example assets. It has been aligned to reflect a professional engineering profile: Senior Software Engineer with expertise in cloud (AWS/Azure), Kubernetes, containerization, and event-driven architectures.

**Summary:**
- Lightweight OpenCV-based color picker demo written in Python.
- Demonstrates image processing fundamentals; minimal production readiness by design.

**Professional alignment:**
- **Cloud:** Suitable for packaging as a container and deploying to AWS (ECS/EKS) or Azure (AKS) with proper CI/CD.
- **Kubernetes:** Add a `Dockerfile` and a small `Deployment` manifest to run the utility as a sidecar or batch job for image annotation workloads.
- **Event-driven:** In production this tool can be extended to process images from event sources (S3/Azure Blob events, Kafka, or Azure Event Grid) and emit results to message buses.

## Files
- `color_detection.py` — small CLI tool to pick colors from an image.
- `colors.csv` — color name/RGB dataset used by the tool.
- `SECURITY.md` — reporting and disclosure guidance (added).

## Running locally
Install dependencies (recommended in a venv):

```powershell
python -m pip install -r requirements.txt
```

Run the color picker (opens a window):

```powershell
python color_detection.py -i path\to\image.jpg
```

For containerization and deployment notes, see the repository owner or add a `Dockerfile` and Kubernetes manifests.

## Security
- Removed interactive notebook outputs from the repo. See `SECURITY.md` for disclosure guidance.

## Contact
If you want this repo tailored further for cloud-native demos (Dockerfile, Helm chart, or event-driven wiring), tell me which provider and I'll scaffold it.