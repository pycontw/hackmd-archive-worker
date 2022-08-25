---
tags: 2021-organize, 2021-web, dev team, dev
---

🔙 [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)

<p>歡迎你一起參與並為 PyCon TW 社群貢獻，希望這份紀錄對你在開發上有幫助 :) </p>

<h2>ㄧ. 起手式，試著 Run PyCon 專案</h2>

<p>起手式當然是先把 PyCon TW 的官網試著跑起來看看，今年有整理了一下 <a href="https://github.com/pycontw/pycon.tw" target="_blank" rel="noreferrer noopener nofollow" title="https://github.com/pycontw/pycon.tw">README.md</a>，相信應該非常容易上手！</p>

<p>首先從 <a href="https://github.com/pycontw/pycon.tw">PyCon TW</a> GitHub 中點擊 fork repo 回自己的 GitHub，接下來 <code>git clone</code> 專案到本地後，目前有兩種方式可以讓專案跑起來：</p>

<h3>1. 使用 docker</h3>

<p>基本上都包好 docker-compose 了，只需要下一行指令就完成了，非常簡單！</p>

<pre class="wp-block-code"><code>$ ./enter_dev_env.sh</code></pre>

<p>docker 小補充：</p>

<p>當 docker 跑起來後，如果要進行像是操作，像是增加 admin 帳號的話，可以使用 <code>docker exec</code> 進入環境，如下</p>

<pre class="wp-block-code"><code>1. $ docker ps 找到你的 &lt;docker name>
2. $ docker exec -it &lt;docker_name> bash -> 會進到 docker 裡面
3. 在 docker 裡面 $ cd src &amp;&amp; python3 manage.py createsuperuser 就可以開始建立 admin 帳號了</code></pre>

<p>關於 docker exec 的詳細用法可以參考這篇<a href="https://docs.docker.com/engine/reference/commandline/exec/" target="_blank" rel="noreferrer noopener nofollow" title="https://docs.docker.com/engine/reference/commandline/exec/">官方說明</a></p>

<h3>2. 本地環境</h3>

<p>安裝步驟比較麻煩，主要會分成三步驟：</p>

<ol><li>首先是建立環境，安裝 Python 和 Node.js 套件</li><li>再來需要準備 <code>local.env</code> 檔案</li><li>最後是 migrate &amp; createsuperuser &amp; compilemessages</li></ol>

<p>完整的安裝流程，詳細內容整理在 <a href="https://github.com/pycontw/pycon.tw/blob/master/document/deploy_local_env_dev.md">這篇 deploy_local_env_dev.md</a></p>

<p>不論是使用 Docker 或本地環境跑起來後，進入 <a href="http://0.0.0.0:8000/" target="_blank" rel="noreferrer noopener nofollow">http://0.0.0.0:8000/</a> 就會看到目前最新版本的 PyCon 官網囉！</p>

<h2>二. 開始接任務啦！</h2>

<p>開始前，首先建立新的分支，再開始任務，關於 git branch 指令，可以參考如下：</p>

<pre class="wp-block-code"><code>$ git branch # 查看本地所有分支
$ git checkout &lt;Name> # 切換到指定分支
$ git checkout -b &lt;Name> # 建立且切換到建立的分支
$ git branch -d &lt;name> # 刪除指定分支</code></pre>

<p>接下來可能會遇到當 fork 的專案，落後於 PyCon 的主專案時 (如下紅框框)：</p>

![](https://i.imgur.com/ZnQsaBN.jpg)


<p>可以將使用 merge 讓本地的專案更新，讓兩邊版本保持一致：</p>

<pre class="wp-block-code"><code>$ git remote add upstream git@github.com:pycontw/pycon.tw.git
$ git fetch upstream
$ git checkout master
$ git merge upstream/master # or $ git rebase upstream/master
$ git push origin master</code></pre>

<h2>三. 當任務完成，Push 前要留意的事</h2>

<p>如果有改到 model 的東西，記得要重新 migrate 一次 (關於 migrate 可參考<a href="https://docs.djangoproject.com/en/3.1/topics/migrations/" target="_blank" rel="noreferrer noopener nofollow" title="https://docs.djangoproject.com/en/3.1/topics/migrations/">這篇官方文件</a>)</p>

<pre class="wp-block-code"><code>$ python3 manage.py makemigrations 
$ python3 manage.py migrate</code></pre>

<p>如果有修改到 i18n 的東西，記得需要跑 compilemessages (關於 i18n 可參考<a href="https://docs.djangoproject.com/en/3.1/topics/i18n/translation/" target="_blank" rel="noreferrer noopener nofollow" title="https://docs.djangoproject.com/en/3.1/topics/i18n/translation/">這篇官方文件</a>)</p>

<pre class="wp-block-code"><code>$ python3 manage.py compilemessages</code></pre>

<p>push 之前跑跑測試，看看有沒有遇到什麼問題！</p>

<pre class="wp-block-code"><code>$ cd src
$ pytest -n 2 --cov=.</code></pre>

<p>都正常的話，就可以 push 了</p>

<pre class="wp-block-code"><code>$ git push</code></pre>

<h2>四. 發 Pull Requests</h2>

<p>在自己的專案中，選擇 New pull request</p>

![](https://i.imgur.com/XNOW7fF.jpg)

選擇剛剛的分支後，下方可以看到這次的 commit 和更動的紀錄

![](https://i.imgur.com/cHqsnAd.jpg)

<p>確認都沒問題，就可以點擊 create pull request，接下來就是針對這次的任務進行描述，主要的描述重點可以分成以下六項：</p>

<ol><li>Types of changes</li><li>Description</li><li>Steps to Test This Pull Request</li><li>Expected behavior</li><li>Related Issue</li><li>More Information</li></ol>


![](https://i.imgur.com/v4vIUba.jpg)

<p>最後就完成 PR 囉，接下來等待大家的 review 和建議就可以了～</p>

<p>經過大家的 review 過後，如果有需要修改的部分，只需要重新 push 一次，PR 就會自動更新囉！</p>

<h2>五. 在本地查看 Pull requests</h2>

```
$ git fetch upstream pull/ID/head:BRANCHNAME
$ git checkout BRANCHNAME
```


<h2>六. 其他補充</h2>

<p>專案中的 ccip：

是整合了 OPass 的活動資訊的解決方案，OPass 是為了台灣開源資訊社群研討會所開發的報到 App，關於更多 OPass 可以參考<a href="https://opass.app/" target="_blank" rel="noreferrer noopener nofollow">此篇文件</a>。

</p>