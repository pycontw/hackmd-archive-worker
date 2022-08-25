---
tags: 2021-organize, 2021-web, dev team
---

# PyCon TW Website Feature Doc: CoC Agreement

[TOC]

## Purpose

Make sure all the talk/proposal submitter agree with our latest code-of-conduct

## Precedure


1. Access the proposal dashboard and click the button for adding new talk or tutorial proposal.
![](https://i.imgur.com/2OdxrI3.png)
2. The agreement page show up if (1) the user never sent out the agreement form (2) the agreement is out-dated (explained in next part).
![](https://i.imgur.com/sYBqGEz.png)
...
![](https://i.imgur.com/RtfObpJ.png)
3. Users can only enter the proposal editing page after submitting the agreement.

## Admin Settings

- All CoC records are stored in DB and listed on admin portal (`<host>/admin/users/cocrecord/`).
- If CoC content is updated, program team may need to inform developers to increment the `COC_VERSION` in Django setting (e,g, change it from `2021.0` to `2021.1`).

## Known Issues

- After changing the language setting on agreement page, the website return 5XX after sending out the form. (but the record is saved)
- We plan to migrate the attendee facing pages to a new project. However, the agreement page capture the coc content from the old template (`templates/contents/<lang>/about/code-of-conduct.html`), which prevents us from deprecating the template of CoC.

## Reference

- Issue: [#653](https://github.com/pycontw/pycon.tw/issues/635)
- PR: [#659](https://github.com/pycontw/pycon.tw/pull/659)
- Checkout how we specify if an user agreed with the latest CoC [here](https://github.com/pycontw/pycon.tw/pull/659/files#diff-427b34724e833389b229ff0ff0f0aee9819dc1b3f24eb4f2b1a27f05ac73b80dR299-R301)
