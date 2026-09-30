2026-09-30T15:40 | manager | open | learner=arthur trainer_model=claude-fable-5-1
2026-09-30T15:42 | trainer | present | unit=baseline item=b1-own
2026-09-30T16:07 | trainer | present | unit=baseline item=b1-own
2026-09-30T16:33 | trainer | present | unit=baseline item=b2-life
2026-09-30T16:42 | trainer | present | unit=baseline item=b3-result
2026-09-30T16:55 | trainer | present | unit=baseline item=b4-traits
2026-09-30T17:06 | trainer | present | unit=baseline item=b5-iter
2026-09-30T17:11 | trainer | present | unit=baseline item=b6-enum
2026-09-30T17:19 | trainer | feedback | unit=baseline item=b1-own
2026-09-30T17:19 | trainer | feedback | unit=baseline item=b2-life
2026-09-30T17:19 | trainer | feedback | unit=baseline item=b3-result
2026-09-30T17:19 | trainer | feedback | unit=baseline item=b4-traits
2026-09-30T17:19 | trainer | feedback | unit=baseline item=b5-iter
2026-09-30T17:19 | trainer | feedback | unit=baseline item=b6-enum
2026-09-30T17:19 | trainer | start | unit=u01-own-move-borrow
2026-09-30T17:19 | trainer | present | unit=u01-own-move-borrow item=attempt
2026-09-30T17:19 | trainer | attempt | unit=baseline item=b1-own result=fail minutes=1.23
2026-09-30T17:19 | trainer | attempt | unit=baseline item=b2-life result=fail minutes=0.73
2026-09-30T17:19 | trainer | attempt | unit=baseline item=b3-result result=fail minutes=8.08
2026-09-30T17:19 | trainer | attempt | unit=baseline item=b4-traits result=fail minutes=2.27
2026-09-30T17:19 | trainer | attempt | unit=baseline item=b5-iter result=fail minutes=2.87
2026-09-30T17:19 | trainer | attempt | unit=baseline item=b6-enum result=pass minutes=2.15
2026-09-30T17:35 | trainer | feedback | unit=u01-own-move-borrow item=attempt
2026-09-30T17:35 | trainer | attempt | unit=u01-own-move-borrow item=u01-attempt result=pass minutes=9.62
2026-09-30T17:36 | trainer | instruction | unit=u01-own-move-borrow item=attempt principle=unrecorded-in-csv note="converted; the old schema held no principle"
2026-09-30T17:36 | trainer | present | unit=u01-own-move-borrow item=reuse-1
2026-09-30T17:41 | trainer | request | unit=u01-own-move-borrow item=attempt request=explain
2026-09-30T17:41 | trainer | instruction | unit=u01-own-move-borrow item=attempt principle=unrecorded-in-csv note="converted; the old schema held no principle"
2026-09-30T17:43 | trainer | request | unit=u01-own-move-borrow item=attempt request=explain
2026-09-30T17:43 | trainer | instruction | unit=u01-own-move-borrow item=attempt principle=unrecorded-in-csv note="converted; the old schema held no principle"
2026-09-30T17:46 | trainer | instruction | unit=u01-own-move-borrow item=attempt principle=unrecorded-in-csv note="converted; the old schema held no principle"
2026-09-30T17:48 | trainer | request | unit=u01-own-move-borrow item=attempt request=explain
2026-09-30T17:48 | trainer | instruction | unit=u01-own-move-borrow item=attempt principle=unrecorded-in-csv note="converted; the old schema held no principle"
2026-09-30T18:06 | trainer | feedback | unit=u01-own-move-borrow item=reuse-1
2026-09-30T18:06 | trainer | present | unit=u01-own-move-borrow item=reuse-2
2026-09-30T18:06 | trainer | attempt | unit=u01-own-move-borrow item=u01-reuse-1 result=pass minutes=4.95
2026-09-30T18:11 | trainer | feedback | unit=u01-own-move-borrow item=reuse-2
2026-09-30T18:11 | trainer | attempt | unit=u01-own-move-borrow item=u01-reuse-2 result=pass minutes=2.68
2026-09-30T18:14 | trainer | confidence | unit=u01-own-move-borrow item=u01-own-move-borrow-probe-a-p1-board value=4
2026-09-30T18:14 | trainer | confidence | unit=u01-own-move-borrow item=u01-own-move-borrow-probe-a-p2-summary value=4
2026-09-30T18:14 | trainer | confidence | unit=u01-own-move-borrow item=u01-own-move-borrow-probe-a-p3-shift value=4
2026-09-30T18:23 | tool:probe | probe-item | unit=u01-own-move-borrow which=immediate problem=probe-a-p1-board result=pass minutes=1.50 fraction=1.0000
2026-09-30T18:24 | trainer | feedback | unit=u01-own-move-borrow item=probe-a
2026-09-30T18:24 | tool:probe | probe-item | unit=u01-own-move-borrow which=immediate problem=probe-a-p2-summary result=pass minutes=1.33 fraction=1.0000
2026-09-30T18:24 | tool:probe | probe-item | unit=u01-own-move-borrow which=immediate problem=probe-a-p3-shift result=pass minutes=2.38 fraction=1.0000
2026-09-30T18:24 | manager | queue | unit=u01-own-move-borrow kind=delayed_probe due=2026-10-07
2026-09-30T18:24 | manager | queue | unit=u02-enums-match kind=next_unit due=2026-10-01
2026-09-30T18:25 | manager | close | minutes=168 units=u01-own-move-borrow interruptions=2 assistant_closed=yes probe_minutes=5.45
