# hackmd-archive-worker

A worker that helps us archive discussion is recorded in [HackMD](https://hackmd.io/team/pycontw?nav=overview) periodically.
The detailed working flow is as follows:

0. (Prerequisite) Define the storing directories mapping in `directory_hierarchy.yaml` for the documents according to the tags.

1. Download all the documents from HackMD through HackMD API.
2. For each downloaded document, parse its tags and move it to the current directory following the definition in `directory_hierarchy.yaml`.
3. After arranging the documents, push the documents to the new branch for archiving.
4. Another script will handle create/update the index of these documents and made them searchable leveraged by [MeiliSearch](https://www.meilisearch.com/) engine.
