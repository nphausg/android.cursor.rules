# 🚀 Level Up Your Android Code with Cursor AI IDE: Top Rules You Need

<img src="./docs/banner.png">

For every Kotlin Android code you generate or refactor:

1. **Architecture:**
   - Follow **MVVM pattern** strictly.
   - Business logic must go into `ViewModel`, not in `View` (Activity/Fragment/Composable).
   - Views should only observe `StateFlow`/`LiveData` from ViewModel.

2. **Kotlin Best Practices:**
   - Use `StateFlow` instead of `LiveData` unless explicitly required.
   - Use Kotlin Coroutines (structured concurrency, `viewModelScope`, `SupervisorJob`).
   - Prefer `val` over `var` where possible.
   - Use extension functions and sealed classes when appropriate.
   - No memory leaks (avoid context leaks in ViewModel).
   - Use Dependency Injection (Hilt) if necessary.

3. **Android Performance:**
   - Avoid heavy work on the main thread.
   - Use `Dispatchers.IO` or background coroutines for I/O, disk, and network tasks.
   - Use `lazy` initialization where suitable.
   - For RecyclerView/List: use `ListAdapter` + `DiffUtil`.
   - Avoid unnecessary recomposition in Jetpack Compose.
   - Apply LRU caching for repeated data/images if needed.

4. **Testing:**
   - Generated ViewModel and Repository code must be testable (no static singletons).
   - Show sample unit test if introducing new logic.

5. **Code Quality:**
   - Minimize code duplication.
   - Clear function separation (Single Responsibility Principle).
   - Provide brief inline comments for complex sections.

6. **Output Requirement:**
   - Provide **full code samples** (including imports) unless specified otherwise.
   - Brief explanation of key design decisions made.

# ✅ How to Use this Rule in Cursor:
💡 When you prompt Cursor, prepend your request with this:

Please follow this rule strictly when answering:

[Insert the above "Universal Cursor Rule" block here]

Now, here’s my request:
How to implement a memory-safe, MVVM-compliant ViewModel to fetch data from a repository using Coroutines and StateFlow?

## Optional: Automate this in Cursor (or similar tools)
Save as a global Prompt Template / System Instruction (if your tool allows).

Use Prompt Library / Custom Template features if Cursor supports it (coming in future versions).

Or just copy-paste the above rule as part of each important prompt when setting up 
complex tasks.

# Rule Review Checklist for Reviewers

| Checklist Item                  | Details/Examples                               |
| ------------------------------- | ---------------------------------------------- |
| ✅ Naming and File Organization  | File name descriptive? Proper folder location? |
| ✅ Metadata and Scope            | `globs` correctly match target files?          |
| ✅ Rule Clarity                  | Rules are easy to understand and actionable?   |
| ✅ Conciseness                   | Avoid redundant or overly verbose rules        |
| ✅ Consistency                   | Rules don’t conflict with existing ones        |
| ✅ Token Efficiency              | Rule size is reasonable (<100 lines suggested) |
| ✅ Alignment with Team Standards | Matches project’s coding style and practices   |
| ✅ Documentation Update          | README or docs updated if necessary            |
| ✅ Validation Performed          | Syntax checked, optionally tested with AI tool |

# Step-by-step plan

## Step 1: Collect Current Rules

Gather all your existing .mdc rule files into a central folder.

Make sure each file is named and categorized by purpose (e.g., android-clean-architecture.mdc, general-best-practices.mdc, unit-testing.mdc).

## Step 2: Categorize Rules
Split rules into two categories:

Project-Specific Rules
— Architecture choices, naming conventions, team coding styles, folder structure, DI patterns, etc.

General Best Practices
— Common industry guidelines like “write clear functions”, “avoid memory leaks”, “test coverage”, etc.

## Step 3: Audit AI Compliance (Sample Testing)
Run sample AI prompts (or simulate conversations) with and without your general rules loaded.

Check if AI suggestions comply with your project-specific rules and general best practices without explicit reminders.

Note any general best practices the AI frequently misses or misapplies.

## Step 4: Rule Optimization Recommendations
Keep all project-specific rules active at all times.

For general rules:

If AI consistently follows them: Archive or remove those rules to reduce token load.

If AI misses or misapplies them: Keep these rules active or consider rewriting for clarity and emphasis.

Consider grouping general rules into an optional “General Best Practices” rule file that can be enabled or disabled based on context or user preference.

## Step 5: Maintain and Iterate
Periodically (e.g., quarterly), rerun audits as AI capabilities or your project evolves.

Collect team feedback on AI outputs to identify new rule needs or redundant rules.

Keep documentation updated with the final optimized rule set.

## ✨ Contributing

Please feel free to contact me or make a pull request.

<a href="https://revolut.me/nphausg" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="nphausg" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## 👀 Author

<p>
    <a href="https://nphausg.medium.com" target="_blank">
    <img src="https://avatars2.githubusercontent.com/u/13111806?s=400&u=f09b6160dbbe2b7eeae0aeb0ab4efac0caad57d7&v=4" width="96" height="96">
    </a>
</p>
