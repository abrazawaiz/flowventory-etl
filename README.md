# Flowventory — End-to-End ETL Data Pipeline

!Limage alt](https://github.com/abrazawaiz/flowventory-etl/blob/bdd57254d78ba078c0691d2d5b764171482ec565/flowventory_etl_architecture.jpeg)

## Overview
**Flowventory** is an end-to-end **ETL (Extract, Transform, Load)** project that simulates a production-grade data pipeline using a dataset from **Kaggle**.  
The data is extracted in CSV format, cleaned and transformed using **Python**, and then loaded into **PostgreSQL**.  
The workflow is orchestrated with **Apache Airflow** and containerized with **Docker**, ensuring consistency, scalability, and ease of deployment.

---

## 🎯 Objectives
This project mirrors the workflow of a modern **Data Engineer**, focusing on building a pipeline that is scalable, modular, and maintainable.

- Automate data extraction, transformation, and loading through modular tasks.  
- Seamlessly integrate **Python**, **Airflow**, **PostgreSQL**, and **Docker**.  
- Apply production-grade practices: structured architecture, logging, and dependency orchestration.  
- Establish a foundation for analytics and visualization in the next phase.

---

## ⚠️ Challenges
Several technical challenges were encountered during development:

- Structuring the project so **Airflow** can properly detect and execute **DAGs**.  
- Managing communication and networking between **Airflow** and **PostgreSQL** containers.  

**Next Step:** Develop an _interactive BI dashboard_ to visualize ETL outcomes.

---

## 🏆 Outcome
The first phase of **Flowventory** successfully established a fully containerized, end-to-end ETL system.  
It demonstrates how modern tools — **Python**, **Airflow**, **PostgreSQL**, and **Docker** — can be combined to build a strong foundation for analytics and data-driven insights.

**Repository:** [github.com/abrazawaiz/flowventory](https://github.com/abrazawaiz/flowventory)  
**Status:** In Development
