# 🤖 TreasuryAICore

[![CI/CD](https://github.com/DevSpecOps/TreasuryAICore/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/DevSpecOps/TreasuryAICore/actions)
[![GitHub release](https://img.shields.io/github/release/DevSpecOps/TreasuryAICore.svg)](https://github.com/DevSpecOps/TreasuryAICore/releases)
![Java](https://img.shields.io/badge/Java-21-blue.svg)
![.NET](https://img.shields.io/badge/.NET-8-purple.svg)
![Node.js](https://img.shields.io/badge/Node.js-20-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Docker](https://img.shields.io/badge/docker-compose-blue.svg)

**Enterprise‑grade banking transaction platform** with microservices (Java, C#, Node.js), PostgreSQL, Redis, RabbitMQ, Kafka, and a full DevOps pipeline.

---

## 🗂️ What It Does

- **Microservices architecture** — Auth (Java), Payment (C#), Notification (Node.js)
- **Event‑driven communication** via RabbitMQ and Kafka
- **Data persistence** with PostgreSQL (relational) and Redis (caching)
- **RESTful APIs** with health checks and readiness probes
- **Containerization** with Docker Compose (local development)
- **CI/CD pipeline** using GitHub Actions (build, test, push)
- **Monitoring** (planned for v2.0.0) — Prometheus + Grafana
- **Realistic banking data model** — transactions, users, notifications

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend (Auth) | Java 21 + Spring Boot + Maven |
| Backend (Payment) | C# + .NET 8 |
| Backend (Notification) | Node.js 20 + Express |
| Databases | PostgreSQL 15, Redis 7 |
| Message Brokers | RabbitMQ 3, Kafka (Confluent) |
| Containerization | Docker + Docker Compose |
| CI/CD | GitHub Actions |
| Monitoring (future) | Prometheus + Grafana |

---

## ⚡ Quick Start

### Docker Compose (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DevSpecOps/TreasuryAICore.git
   cd TreasuryAICore
   ```

2. **Build and run all services**:
   ```bash
   docker-compose up -d --build
   ```

3. **Verify services**:

   | Service | URL | Credentials |
   |---------|-----|-------------|
   | Auth API | http://localhost:8080/api/v1/auth/health | — |
   | Payment API | http://localhost:8081/api/v1/payment/health | — |
   | Notification API | http://localhost:8082/api/v1/notification/health | — |
   | PostgreSQL | localhost:5432 | treasury / treasury123 |
   | Redis | localhost:6379 | — |
   | RabbitMQ Management | http://localhost:15672 | treasury / treasury123 |
   | Kafka | localhost:9092 | — |

4. **Check data flow**:
   - The `init-db.sh` script automatically creates the `transactions` table on PostgreSQL startup.
   - Run the seed script to populate test data:
     ```bash
     python3 scripts/seed-data.py
     ```

---

## ⚙️ Development

### Run Locally (without Docker)

You can run each service separately, but you'll need to start PostgreSQL, Redis, RabbitMQ, and Kafka manually.

```bash
# Auth Service (Java)
cd services/auth-service
mvn spring-boot:run

# Payment Service (C#)
cd services/payment-service
dotnet run

# Notification Service (Node.js)
cd services/notification-service
npm install
npm start
```

### Environment Variables

Each service uses environment variables for configuration — see `docker-compose.yml` for examples.

---

## 🧪 Run Tests

Each service has its own unit tests:

```bash
# Auth Service
cd services/auth-service
mvn test

# Payment Service
cd services/payment-service
dotnet test

# Notification Service
cd services/notification-service
npm test
```

---

## 📦 Dependencies

| File | Purpose |
|------|---------|
| `services/auth-service/pom.xml` | Java (Maven) dependencies |
| `services/payment-service/*.csproj` | .NET NuGet packages |
| `services/notification-service/package.json` | Node.js npm packages |

---

## 🚦 CI/CD

GitHub Actions (or GitLab CI) is configured to:

- Run unit tests on every `push` and `pull_request`
- Build Docker images for each microservice
- (Optional) Push images to a container registry

See `.github/workflows/ci.yml` (or `.gitlab-ci.yml`).

---

## 🏗️ Project Structure

```
TreasuryAICore/
├── .github/workflows/        # CI/CD pipelines
├── services/
│   ├── auth-service/         # Java + Spring Boot
│   │   ├── Dockerfile
│   │   ├── pom.xml
│   │   └── src/
│   ├── payment-service/      # C# + .NET 8
│   │   ├── Dockerfile
│   │   ├── TreasuryAICore.Payment.csproj
│   │   └── Program.cs
│   └── notification-service/ # Node.js + Express
│       ├── Dockerfile
│       ├── package.json
│       └── app.js
├── scripts/
│   ├── init-db.sh            # DB initialisation
│   └── seed-data.py          # Test data generator
├── docker-compose.yml        # Full stack orchestration
└── README.md
```

---

## 🧭 Roadmap

### Version 1.0.0 (Current)
- ✅ Docker Compose with all services
- ✅ PostgreSQL, Redis, RabbitMQ, Kafka
- ✅ Health check endpoints
- ✅ Basic CI/CD pipeline

### Version 2.0.0 (Planned)
- **Kubernetes** (k3s) with Helm charts
- **Prometheus** + **Grafana** monitoring
- **Full CI/CD** with GitLab CI (build, deploy, rollback)
- **SLA** dashboards and alerting

### Version 3.0.0 (Future)
- **Service Mesh** (Istio)
- **GitOps** (ArgoCD)
- **Centralised logging** (Loki)
- **Load testing** (k6) in CI

---

## 🏷️ Releases

Check the [Releases](https://github.com/DevSpecOps/TreasuryAICore/releases) page for versioned artifacts, changelogs, and stable builds.

- **Latest stable version**: [v1.0.0](https://github.com/DevSpecOps/TreasuryAICore/releases/tag/v1.0.0)

---

## ⚖️ License

**MIT** — free for personal and commercial use.

---

## 🙌 Contributing

PRs and issues are welcome! Feel free to improve the project.

---

## 📧 Contact

- **Author**: DevSpecOps
- **Email**: devspecops@gmail.com
- **GitHub**: [@DevSpecOps](https://github.com/DevSpecOps)
- **Telegram**: @DevSpecOps