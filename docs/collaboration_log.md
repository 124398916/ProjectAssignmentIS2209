# Team Collaboration Log
## IS2209 DeployHub — Integration & CI/CD Group Project

**Group name:** Group 26  
**Members:** Lara Amaro · Anna Mazurkiewicz · Ellen O'Sullivan  
**Repository:** https://github.com/124398916/ProjectAssignmentIS2209
**Submission date:** 14/04/2026

---

## 1. Team Roles

| Member  | Primary Role    | Responsibilities                                                                                                       |
|---------|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Ellen O'Sullivan | Team Leader     | create git repo, protected main branc, approve team members pull reqs, submitted final project                         |
| Lara Amaro | documentation   | kept up to date on documenting what we had to do, what was in progress, what needed to be reviewed, and what was done. |
| Anna Mazurkiewicz        | DevOps Engineer | docker, CI/CD, github actions                                                                                          |

> Roles were agreed in our first planning session and adjusted as needed throughout the project.

---

## 2. Ceremonies & Meetings

| Date         | Type | Attendees | Summary                                                                  |
|--------------|---|---|--------------------------------------------------------------------------|
| [17/02/2026] | Kickoff meeting | All | Assigned roles, agreed branching strategy, set up repo and project board |
| [03/03/2026] | Sprint planning | All | Broke work into issues, set priorities on Kanban board                   |
| [24/03/2026] | Check-in | All | Reviewed progress, resolved blockers, reassigned tasks                   |
| [31/03/2026] | Final review | All | Reviewed documentation, prepared submission                              |

---

## 3. Branching Strategy

We adopted a **trunk-based development** approach with short-lived feature branches:

- `main` — protected branch; only accepts merges via approved PRs with passing CI checks
- `feature/<issue-number>-<short-description>` — one branch per issue/task
- No direct commits to `main`

All branches were linked to a GitHub Issue and closed via Pull Request.

---

## 4. Kanban Board

**Board link:** https://miro.com/app/board/uXjVGsE5T9Q=/?share_link_id=292144440814

We maintained a four-column Kanban board throughout the project:

| Column | Purpose |
|---|---|
| To Do | All planned issues not yet started |
| In Progress | Actively being worked on |
| Review | PR open, awaiting peer review |
| Done | Merged and closed |

At peak we had 9 issues open simultaneously across the board.

---

## 5. Issues & Pull Requests

**Issues link:** https://github.com/124398916/ProjectAssignmentIS2209/issues  
**Pull requests link:** https://github.com/124398916/ProjectAssignmentIS2209/pulls

#### Key Pull Requests

| PR | Title                                 | Author | Reviewer         | Description                                                    |
|---|---------------------------------------|--|------------------|----------------------------------------------------------------|
| #12 | Added code and css and html and image | Ellen O'Sullivan | Ellen O'Sullivan | Added frontend assets                                          |
| #11 | Feature/requirements                  | Ellen O'Sullivan | Ellen O'Sullivan | changed design of cat facts homepage                           |
| #10 | Feature/dockerfile                    | Anna Mazurkiewicz | Ellen O'Sullivan | Dockerfile feature work                                        |
| #9 | Feature/requirements                  | Ellen O'Sullivan | Ellen O'Sullivan | added code for cats facts home page                            |
| #8 | Feature/requirements                  | Ellen O'Sullivan | Ellen O'Sullivan | added api url                                                  |
| #7 | changed code in app.py                | Ellen O'Sullivan | Ellen O'Sullivan | changed code from example from tutors to code to match our api |
| #6 | Added index.html file                 | Ellen O'Sullivan | Ellen O'Sullivan | Added main HTML page                                           |
| #5 | Feature/dockerfile                    | Anna Mazurkiewicz | Ellen O'Sullivan | Dockerfile feature work                                        |
| #4 | Feature/dockerfile                    | Anna Mazurkiewicz | Ellen O'Sullivan | Dockerfile feature work                                        |
| #3 | Add Dockerfile                        | Anna Mazurkiewicz | Ellen O'Sullivan | Initial Dockerfile setup                                       |
| #2 | added requirements.txt                | Ellen O'Sullivan | Ellen O'Sullivan | created requirements.txt file                                  |
| #1 | Change to there                       | Lara Amaro | Ellen O'Sullivan | Initial change                                                 |

> Every feature landed via PR with at least one peer review. CI checks were required to pass before merge.

### Contribution Summary

| Member      | PRs Authored | PRs Reviewed |
|-------------|--------------|--------------|
| Ellen O'Sullivan | 7            | 0            |
| Lara Amaro  | 1            | 0            |
| Anna Anna Mazurkiewicz       | 4            | 0            |

---

## 6. Communication

- **Primary channel:** Snapchat Groupchat, and IS2209 Tutorials
- **Code collaboration:** GitHub Issues, PR comments, and inline code review
- **Meeting format:** In person

---

## 7. Challenges & How We Resolved Them

| Challenge                                            | How We Resolved It                                                          |
|------------------------------------------------------|-----------------------------------------------------------------------------|
| Docker not working during class                      | met up again, and worked through it at our own pace                         |
| getting out env to work                              | had to double check posted document                                         |
| making sure all changes made were commited to github | we only worked on the project together, so we could communicate any changes |