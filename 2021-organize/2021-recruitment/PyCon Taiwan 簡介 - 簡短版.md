---
tags: 2021-organize, organize, 2021-recruitment, recruitment
slideOptions:
  transition: slide
---

<style>
.red {
  color: red;
}
.yellow {
  color: yellow;
}
.green {
  color: green;
}
.blue {
  color: blue;
}
</style>


# PyCon Taiwan 簡介 - 簡短版

<!-- .slide: data-background="https://lineartran.nl/images-provisioning/10th-pycontw-theme-slide-bg.png"  -->

---

🔙 Back to [歷年 PyCon TW Organizing 共筆](/ryPr7SFyP/%2FHM5mHCFKQCu7-W5ea8ITcw%3Fview)
🔙 Back to [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)
🔙 Back to [PyCon TW 2020 Organizing 共筆](/5u84SOprTUeQYBR57TH49w)

---

## Who We Are

<!-- .slide: data-background="https://lineartran.nl/images-provisioning/10th-pycontw-theme-slide-bg.png"  -->

----

<!-- .slide: data-background="https://lineartran.nl/images-provisioning/by-the-community-for-the-community.png"  -->

----

"<span class="yellow">PyCon TW</span>" is a trademark authorized by <span class="yellow">PSF</span>, Python Software Foundation

----

Code of Conduct

----

Everyone Contributes

---

## Who We Are <span class="red">NOT</span>

<!-- .slide: data-background="https://lineartran.nl/images-provisioning/10th-pycontw-theme-slide-bg.png"  -->

----

### We are <span class="red">NOT</span> Python Study Group


----

We do code review and learned from each other by <span class="yellow">code review</span>

----

You may <span class="red">NOT</span> advance your Python skill if you do not contribute your code proactively

----

There is internal study groups, but they are <span class="red">NOT</span> official teams in the organization

----

For people who want to join a study group, you may want to <span class="yellow">Taipei Py, PyLadies,</span> ...... etc. local communities.

----

Tip: try to organize the conference <span class="yellow">by Python</span>. Raise corresponding questions in the organization team.

---

## How We Organize

----

組織架構

<!--
- 組別需求圖
  - 議程最多
  - 有可能對不上
-->

<!--你以為的組織架構-->

<!--
```graphviz
digraph hierarchy {

                nodesep=1.0 // increases the separation between nodes

                node [color=Red,fontname=Courier,shape=box] //All nodes will this shape and colour
                edge [color=Blue, style=dashed] //All the lines look like this

                Chairperson->{議程組 行銷組 場務組 註冊組 設計組 記錄組 招募組 開發組 財務組}
                行銷組->{行銷企劃小隊 贊助執行小隊 公關媒體小隊}
                開發組->{網站整合小隊 資料決策小隊 基礎建設小隊}
                {rank=same;行銷組 開發組}  // Put them on the same level
}
-->
```mermaid
 classDiagram
      Chairperson .. 議程組
      Chairperson .. 行銷組
      Chairperson .. 場務組
      Chairperson .. 註冊組
      Chairperson .. 設計組
      Chairperson .. 記錄組
      Chairperson .. 招募組
      Chairperson .. 開發組
      Chairperson .. 財務組
      行銷組 .. 行銷企劃小隊
      行銷組 .. 贊助執行小隊
      行銷組 .. 社群媒體小隊
      開發組 .. 網站整合小隊
      開發組 .. 資料決策小隊
      開發組 .. 基礎建設小隊
      設計組 .. Graphic 小隊
      設計組 .. UIUX 小隊
``````

----

實際上的架構（是一個相對扁平的組織；每個志工之間運作頗獨立而讓組織呈現網狀的運作方式）

```mermaid
 classDiagram
      Chairperson .. 議程組
      Chairperson .. 行銷組
      Chairperson .. 行銷企劃小隊
      Chairperson .. 贊助執行小隊
      Chairperson .. 公關媒體小隊
      Chairperson .. 網站整合小隊
      Chairperson .. 資料決策小隊
      Chairperson .. 基礎建設小隊
      Chairperson .. 場務組
      Chairperson .. 註冊組
      Chairperson .. 設計組
      Chairperson .. 記錄組
      Chairperson .. 招募組
      Chairperson .. 開發組
      Chairperson .. 財務組
      議程組 .. 行銷企劃小隊
      議程組 .. 贊助執行小隊
      議程組 .. 公關媒體小隊
      行銷組 .. 行銷企劃小隊
      行銷組 .. 贊助執行小隊
      行銷組 .. 公關媒體小隊
      開發組 .. 網站整合小隊
      開發組 .. 資料決策小隊
      開發組 .. 基礎建設小隊
      贊助執行小隊 .. 註冊組
      贊助執行小隊 .. 設計組
      贊助執行小隊 .. 場務組
      網站整合小隊 .. UIUX 小隊
      招募組 .. 議程組
      招募組 .. 行銷組
      招募組 .. 行銷企劃小隊
      招募組 .. 贊助執行小隊
      招募組 .. 公關媒體小隊
      招募組 .. 網站整合小隊
      招募組 .. 資料決策小隊
      招募組 .. 基礎建設小隊
      招募組 .. 場務組
      招募組 .. 註冊組
      招募組 .. 設計組
      招募組 .. 記錄組
      招募組 .. 開發組
      招募組 .. 財務組
      場務組 .. Graphic 小隊
      設計組 .. Graphic 小隊
      設計組 .. UIUX 小隊
```


