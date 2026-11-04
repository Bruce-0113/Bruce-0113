<!-- Terminal-style GitHub Profile README -->

<div align="center">
  <img src="assets/terminal.svg" alt="bruce@github:~$ whoami → Bruce Huang · AI Engineer · Medical AI" width="494">
</div>

---

<div align="center">

# Bruce Huang

**AI Engineer · Computer Vision · LLM Systems · Medical AI**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/po-hsun-huang-99a39b208/)
[![Website](https://img.shields.io/badge/Bruce's_Notes-FF5D01?style=flat-square&logo=astro&logoColor=white)](https://bruce-notes.s24578111.workers.dev/)
[![Email](https://img.shields.io/badge/Email-333333?style=flat-square&logo=gmail&logoColor=white)](mailto:s24578111@gmail.com)

</div>

---
 
## `$ whoami`
 
```json
{
  "role"     : "AI Engineer @ 睿傳數據股份有限公司",
  "focus"    : ["Medical AI", "Medical Imaging", "LLM for Medical Reports",
                "LLM Evaluation", "On-premise LLM Serving", "RAG & AI Agents"],
  "stack"    : {
    "lang"  : ["Python", "SQL"],
    "ml"    : ["PyTorch", "TensorFlow / Keras", "HuggingFace", "BERT"],
    "llm"   : ["vLLM", "SGLang", "Speculative Decoding", "Pydantic / instructor",
               "LangChain", "LlamaIndex", "LoRA"],
    "cv"    : ["YOLOv5 / YOLOv7", "OpenCV", "pydicom", "DICOM QC"],
    "mlops" : ["Docker", "Kubernetes", "GCP", "FastAPI"],
    "data"  : ["Spark SQL", "Oracle", "AWS S3"],
    "stats" : ["Statistical Modeling", "Sampling & Estimation", "Regression / ANOVA"]
  },
  "approach" : ["Frame the decision first: what it supports, what errors cost",
                "Evaluate like a statistician: is the gain real?",
                "Ship with guardrails: QC gates, regression tests, refuse when unsure"],
  "edu"      : "B.S. & M.S. Statistics, National Taipei University",
  "exp"      : "4+ years in AI model development & deployment",
  "site"     : "bruce-notes.s24578111.workers.dev",
  "location" : "Taiwan 🇹🇼"
}
```
 
---
 
## `$ cat ./experience.log`
 
```
[2022.08-present]  AI Engineer · 睿傳數據股份有限公司
                   > Medical imaging CV pipelines, DICOM end-to-end (YOLOv7 detection, CNN regression)
                   > LLM systems for medical reports: on-prem serving (vLLM / SGLang), structured extraction, evaluation
                   > Health-report severity grading: 100K+ reports processed, ≥95% agreement with manual review
                   > Full lifecycle ownership: research → training → serving → monitoring (Docker / K8s / GCP)

[2017.01-2021.06]  Research Assistant · 國立臺北大學 大數據與智慧城市研究中心
                   > Nationwide telecom-signaling population database for the Ministry of the Interior
                   > Integrated billions of signaling records from three carriers with Spark SQL
```
 
---

## `$ ls ./projects`

<pre>
<b>work/</b>  ·  case studies on <a href="https://bruce-notes.s24578111.workers.dev/projects/">bruce-notes/projects</a>
  <a href="https://bruce-notes.s24578111.workers.dev/projects/report-qc/">report-qc</a>                     LLM QC for CT/MRI radiology reports · on-prem Gemma-4-31B
  <a href="https://bruce-notes.s24578111.workers.dev/projects/health-report-classification/">health-report-classification</a>  BERT + LLM + rules · 100K+ reports · ≥95% agreement
  <a href="https://bruce-notes.s24578111.workers.dev/projects/dental-xray-detection/">dental-xray-detection</a>         Two-stage YOLOv7 wisdom-tooth detection, panoramic X-ray
  <a href="https://bruce-notes.s24578111.workers.dev/projects/ct-body-part-regression/">ct-body-part-regression</a>       CNN regression of body-part index per CT slice
  <a href="https://bruce-notes.s24578111.workers.dev/projects/telecom-signaling-population/">telecom-signaling-population</a>  First nationwide telecom-signaling population stats

<b>side/</b>
  <a href="https://github.com/Bruce-0113/financial_report_RAG">financial_report_RAG</a>          Offline RAG on TSMC annual report · LlamaIndex + Ollama
  <a href="https://github.com/Bruce-0113/bruce-badminton">bruce-badminton</a>               Local coach LLM: 9B → 4B distillation, LoRA, MLX 4-bit
  <a href="https://github.com/Bruce-0113/ai-paper-tracker">ai-paper-tracker</a>              Daily arXiv digest (cs.AI/LG/CV/CL) via GitHub Actions
  <a href="https://github.com/Bruce-0113/ai-from-scratch">ai-from-scratch</a>               CV and NLP fundamentals, reimplemented from scratch
  <a href="https://github.com/Bruce-0113/slot-reel-designer">slot-reel-designer</a>            Exact-target-RTP reel strips · enumeration + Monte Carlo
  <a href="https://github.com/Bruce-0113/useful-prompts-library">useful-prompts-library</a>        Reusable, battle-tested LLM prompts in Markdown
</pre>

---

## `$ ls -t ./posts | head -5`

<!-- latest_posts starts -->
<pre>
  2026-10-27  <a href="https://bruce-notes.s24578111.workers.dev/posts/rag-overview/">RAG 全貌：從固定 pipeline 到 agent 手上的檢索工具</a>
  2026-10-15  <a href="https://bruce-notes.s24578111.workers.dev/posts/llm-inference-optimization/">LLM 推論效能優化：vLLM、SGLang 與 TensorRT-LLM 的調校方法</a>
  2026-10-15  <a href="https://bruce-notes.s24578111.workers.dev/posts/hf-model-deployment/">從 Hugging Face 到上線：開源 LLM 的下載與部署實戰</a>
  2026-10-13  <a href="https://bruce-notes.s24578111.workers.dev/posts/agent-control-flow/">Agent 的控制流：從 ReAct 到 Dynamic Workflows</a>
  2026-10-02  <a href="https://bruce-notes.s24578111.workers.dev/posts/model-compression-overview/">模型壓縮全貌：量化、剪枝、蒸餾怎麼選、怎麼組合</a>

  → <a href="https://bruce-notes.s24578111.workers.dev/">all posts, notes &amp; readings (zh-TW)</a>
</pre>
<!-- latest_posts ends -->

---

## `$ ls ./recent-activity`
 
<!-- recent_activity starts -->
<pre>
  2026-11-03  <a href="https://github.com/Bruce-0113/slot-reel-designer">slot-reel-designer</a>      Python
  2026-10-14  <a href="https://github.com/Bruce-0113/bruce-badminton">bruce-badminton</a>         Python
  2026-09-16  <a href="https://github.com/Bruce-0113/ai-from-scratch">ai-from-scratch</a>         Python
  2026-08-18  <a href="https://github.com/Bruce-0113/useful-prompts-library">useful-prompts-library</a>  —
  2026-08-03  <a href="https://github.com/Bruce-0113/financial_report_RAG">financial_report_RAG</a>    Python
</pre>
<!-- recent_activity ends -->
 
---

```
bruce@github:~$ █
```
 
<div align="center">
<sub>Open to freelance opportunities in Computer Vision & Medical AI</sub>
</div>
