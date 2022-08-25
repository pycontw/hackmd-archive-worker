---
tags: 2021-organize, 2021-web, dev team
---

🔙 [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)

# 2021 Web Squad Feature Doc: Codebase Restruction

[TOC]

### Decisions

1. Spin off 2021 attendee-facing website frontend to a separate repo
2. Use Vue.js to develop the 2021 website
3. Remain the proposal related services as it is while extending the API server section (DRF) for frontend's calls

#### 2021 Website Frontend MVP Scope

:::warning
Deadline: Dec. 20th
:::

- Get the repo ready with:
    - a proper `build` script for faster deployment
    - the unit testing mechanism
    - the data server without depending on backend service updates
    - i18n
- Layout the Information Archirecture (IA)
    - based on the 2020's as the reference while standing by for any new page contents
    - without a specific themed design until the design team has made the call
- Deploy to [TBD]