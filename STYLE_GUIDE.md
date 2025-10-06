# PoetryCoding Style Guide

PoetryCoding is not about syntax — it’s about **intention**.  
Still, certain practices help embody its spirit.

## 🌿 Principles

1. **Silence over noise**  
   Avoid comments that repeat what the code already says. Let names speak clearly.

2. **Metaphor in naming**  
   Variables, functions, and modules should evoke meaning, not just describe mechanics.  
   → `ghost` instead of `deleted_account_marker`  
   → `tomb` instead of `dead_link_archive`

3. **No deletion without ritual**  
   Never erase. Archive, veil, or transform.  
   Deletion is violence. Remembrance is care.

4. **Minimal output**  
   Programs should speak only when necessary.  
   No verbose logs. No unnecessary prints.  
   Let the user live in quiet.

5. **Offline-first, dependency-light**  
   Poetry doesn’t require the cloud to exist.  
   Your code shouldn’t either.

6. **Leave space**  
   Blank lines are breaths.  
   Indentation is rhythm.  
   Structure is stanza.

## ✨ Example (Python)

```python
def lay_to_rest(url):
    """Place a dead link in the tomb — with name, date, and reason."""
    if not is_alive(url):
        tombstone = carve_tombstone(url, reason="link decay")
        archive_in_tomb(tombstone)
        whisper(f"Remembered: {url}")


Notice:

No redundant docstring
Verbs like lay, carve, whisper carry poetic weight
Action is gentle, not forceful

This guide evolves with the community.
Suggest additions via issue or pull request — but only if they serve care. 