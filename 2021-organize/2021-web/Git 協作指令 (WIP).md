---
tags: 2021-organize, 2021-web, dev team
---

🔙 Back to [PyCon TW Organizing 共筆](https://hackmd.io/@pycontw/SyG5_GrED/https%3A%2F%2Fhackmd.io%2F%40pycontw%2FByi2hyM9w)

# Git 協作指令 (WIP)

Git 是一種分散式版本的版本控制系統(Version Control System)，和許多多人協作 project 一樣，我們希望開發者在開始貢獻之前對於 Git 都要有一定的認識。
關於 Git 的教學文章已經太多，如果對 Git 完全不認識的話請先花點時間自行學習。
此篇文章只會列出大家普遍認為寫的不錯的學習資源和一些協作時常用到的指令。

## Git 的基本介紹

如果你剛認識 Git：

- [寫給 Git 初學者的入門 4 步驟 by Max](https://www.maxlist.xyz/2018/11/02/git_tutorial/)
- [連猴子都能懂的Git入門篇](https://backlog.com/git-tutorial/tw/intro/intro1_1.html)

如果你已經會 git {clone,add,commit,push} 等基本指令：

- [為你自己學 Git](https://gitbook.tw/)
- [連猴子都能懂的Git進階篇](https://backlog.com/git-tutorial/tw/stepup/stepup1_1.html)

## 進階協作指令

### Make your own forked repo up-to-date
 
```
git remote add upstream git@github.com:pycontw/<repo name>.git
git fetch upstream

git checkout master
git merge upstream/master  # or git rebase upstream/master
git push origin master
```

### Pull the code from a forked repo

當 review 其他人的 PR 時，若想把在某個 forked repo 裡的某個 branch 拉下來試跑，可以輸入以下指令

```
git remote add <whatever tag> git@github.com:<user name>/<repo name>.git
git checkout <whatever tag>/<branch>
```

### Rebase
在 push code 前，可以先整理自己的 commit，令其更具易讀性。輸入以下的指令，並按下 enter 後會進入文字互動模式，可以修改 commit 的內容、合併相似的 commit、變更順序等
```
git rebase -i <after this commit>
```