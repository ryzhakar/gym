# 2026-10-26 — failures

## Plugin update for one login moved every login

What happened: Asked who should update the manifesto plugin, I told the owner the update touched the gym login only and other logins kept 3.6.0; the update moved the shared install, so every login on this Mac went to 4.0.0 at 20:51.

Mechanism: Every login's plugins folder is a symlink to /Users/ryzhakar/.claude-shared/plugins, one installed_plugins.json for all; I read gym's file, saw an install path in the meta login, and did not check the folder link before stating the scope.

Correction: Hazards with the fix sent to the four live sessions whose projects keep the old layout (product-catalog-maintainer, estafette-89, estafette-9a, proudhon), a notice to machine-setup-manager, and the owner told; check a folder's links before stating the scope of a change to it.
