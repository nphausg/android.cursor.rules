# ✅ Universal Cursor Rule for Android Kotlin MVVM + Performance Best Practices

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

Or just copy-paste the above rule as part of each important prompt when setting up complex tasks.