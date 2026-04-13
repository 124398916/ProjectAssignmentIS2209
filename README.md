**Group 26 Members:**
Anna Mazurkiewicz: 124704915
Ellen O'Sullivan: 124398916
Lara Amaro: 124341283

render link: https://projectassignmentis2209.onrender.com
Github repo: https://github.com/124398916/ProjectAssignmentIS2209



## 4. Risks and Mitigations

Identify key risks introduced by your toolchain choices and how you addressed (or would address) them.

| Risk | Likelihood | Impact | Mitigation Applied / Proposed |
|---|---|---|---|
| External API downtime | Medium | High | Implemented graceful degradation — if the upstream service is unreachable, the API returns a meaningful error response or serves cached data rather than crashing. Retry logic with exponential back-off prevents thundering-herd on recovery. |
| Secrets accidentally committed to Git | Low | High | `.env.example` documents required variables without values; `.gitignore` excludes `.env`; all runtime secrets (DB URL, API keys) are stored as GitHub Actions encrypted secrets and injected at build/deploy time only. |
| CI pipeline flakiness (false failures) | Medium | Medium | Dependencies pinned in `requirements.txt` to avoid version drift between runs. Docker layer caching in the Actions workflow reduces build time and non-determinism. Test suite uses a dedicated test DB or mocks to avoid external state. |
| Deployment target outages / cold starts | Low | High | `/health` endpoint allows the platform and monitoring tools to detect unavailability quickly. README documents manual re-deploy steps. For platforms with cold-start delays (e.g., Render free tier), the status page surfaces DB connectivity so degraded state is visible. |
| Database connection exhaustion under load | Low | Medium | Flask app uses a connection pool (SQLAlchemy default pool size) rather than opening a new connection per request. Pool size configured via environment variable so it can be tuned per environment without code changes. |
| Docker image containing sensitive build artefacts | Low | High | Multi-stage Dockerfile used to keep the final image minimal — build tools and dev dependencies are excluded from the production layer. `.dockerignore` prevents `.env` and test files from being copied into the image context. |

---

## 5. Alignment with Lean / Agile / DevOps Principles

Briefly map your toolchain choices to the core principles assessed in IS2209.

- **Lean (eliminate waste, fast feedback):** The GitHub Actions CI pipeline runs automatically on every PR, surfacing lint errors and test failures within minutes rather than waiting for a manual review cycle. Pinned dependencies and Docker layer caching keep run times short, reducing idle waiting. The `/health` and `/status` endpoints provide immediate runtime feedback, avoiding time wasted diagnosing silent failures. Structured logging with request IDs means issues are located quickly rather than through trial-and-error.

- **Agile (iterative delivery, collaboration):** Short-lived feature branches and mandatory PR reviews meant the team could work in parallel without blocking each other, merging small increments frequently rather than in one risky batch. Linking every PR to a GitHub Issue and tracking progress on the Kanban board (To Do → In Progress → Review → Done) gave the whole team shared visibility of what was in flight. Requiring at least two substantive PRs per member ensured contribution was distributed rather than siloed.

- **DevOps (automate everything, shared responsibility):** Docker provides environment parity — the same image that passes CI is the one deployed, eliminating "works on my machine" failures. Automated deployment from `main` via GitHub Actions closes the loop between a merged PR and a live change with no manual handoff. Publishing the image to GHCR ties each artefact to the specific commit that produced it, making rollbacks straightforward. Secrets management via GitHub Actions encrypted secrets means no developer needs production credentials locally, reducing the attack surface and reinforcing shared ownership of the pipeline.

---

## 6. Conclusion

The toolchain chosen for DeployHub provided a solid foundation for practising DevOps principles within the constraints of a team assignment. GitHub Actions, Docker, and GHCR together delivered a fully automated path from code commit to deployed container, while GitHub Issues and the Kanban board kept collaboration structured and traceable. The two changes that would have the highest positive impact if the project were repeated are: first, introducing a dedicated staging environment so that automated deploys could be validated before reaching production; and second, adding a lightweight integration test stage to the CI pipeline — one that spins up the Docker Compose stack and exercises the `/health` and consolidated endpoints end-to-end — which would catch container-level failures that unit tests alone cannot surface.

---

*Word count: [~500–700 words recommended for this document]*