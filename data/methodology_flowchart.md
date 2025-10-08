# 🧭 Project Methodology Flowchart

```mermaid
flowchart LR
    A[📂 Raw Data Collection] --> B[🧹 Data Cleaning & Preprocessing]
    B --> C[⚙️ Feature Extraction (Email & URL)]
    C --> D[🤖 Model Training & Evaluation]
    D --> E[💻 Frontend App Integration]

    subgraph Full_Workflow [Complete Phishing Detection Pipeline]
    A
    B
    C
    D
    E
    end

    style A fill:#b6e3b6,stroke:#2d862d,stroke-width:2px
    style B fill:#a3d5ff,stroke:#004080,stroke-width:2px
    style C fill:#ffd699,stroke:#b37400,stroke-width:2px
    style D fill:#f8b3b3,stroke:#b30000,stroke-width:2px
    style E fill:#d9b3ff,stroke:#6600cc,stroke-width:2px
