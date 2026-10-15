# Team Collaboration & Contribution Guidelines

Welcome to the **Daneben!** project repository.

To protect the integrity of the project and ensure that our verified work is never accidentally overwritten or broken, **direct pushes to the `main` branch are strictly prohibited**.

The `main` branch is our **untouched, verified golden copy**. All new features, bug fixes, PCB modifications, and docs must go through feature branches and Pull Requests.

---

## 🚀 How Teammates Must Work (Step-by-Step)

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/Kirito077/daneben-project.git
cd daneben-project
```

### 2. Always Start from the Latest `main`
Before starting any new task, make sure your local `main` is up to date:
```bash
git checkout main
git pull origin main
```

### 3. Create a Working Branch (Never edit directly on `main`)
Create a new branch for your work with a descriptive name:
```bash
git checkout -b feature/your-feature-name
```
*Examples:*
* `feature/lid-sensor-calibration`
* `feature/kicad-power-routing`
* `fix/debounce-timer-overflow`
* `docs/presentation-slides`

### 4. Work and Commit Locally
Make your changes and commit with meaningful commit messages:
```bash
git add .
git commit -m "feat: Add calibration offset for ultrasonic sensor"
```

### 5. Push Your Branch to GitHub
Push your working branch up to GitHub:
```bash
git push -u origin feature/your-feature-name
```

### 6. Open a Pull Request (PR)
1. Go to the GitHub repository page.
2. Click **"Compare & pull request"**.
3. Describe what you changed, what you tested, and tag `@Kirito077` for review.
4. **Do not merge it yourself.** Once verified and approved by the project lead, your branch will be merged into `main`.

---

## 🛡️ Golden Rules
* ❌ **Never** run `git push origin main`.
* ❌ **Never** force-push (`git push --force`).
* ✅ **Always** test code and check KiCad schematics/DRC before opening a PR.
* ✅ Keep Pull Requests focused and small for easier review.
