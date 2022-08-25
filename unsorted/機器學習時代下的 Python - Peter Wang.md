# 機器學習時代下的 Python - Peter Wang

{%hackmd JgQsr94hSFK427iUDWF9NQ %}
:::warning
Slido連結 : https://app.sli.do/event/qnhcqayv
:::
>
 - what caused the emergency of data science: 
	- More data; cloud; value in data applying DS/ML
	- power of open source
- why python: 
	- Accessible:easy to learn by example; quick learned
	- Performance: well-supported on CPUs, GPUs, TPUs~
	- Compatible: runs on every OS, systems
- Linux+Business Computing => Cloud & SaaS
- Python/R + Predictive Analytics + Clous = ?

- Open: a value regarding contribution, utilization and use freedom
- Source: an outdated term, from when being able just to "read code" could guarantee user sovereignty and freedom


## Q&A

> Reflecting on the society divide, how do you view the current divide between Anaconda Repo & Conda-Forge? Is the structure desirable, or can be improved?
I think we (at Anaconda) and the Conda-Forge community have a very good interaction.  In fact, many current and former Anaconda employees are part of conda-forge.  The "default" or "main" Anaconda repo at repo.anaconda.com serves a somewhat different purpose than the conda-forge channel.
> [color=purple]

The default Anaconda repo aims to be a stable set of packages that interoperate with each other.  This is a non-trivial goal, and oftentimes we have to patch upstream package metadata in order to make them work together.

The goal of conda-forge is to serve as a community package hosting service.  It enables a community of 500+ recipe maintainers to be able to quickly publish their individual builds of their packages. However, very few of them test all of their package against the full smoke/integration test suites of all other related packages.

So, in my view, conda-forge is a great community service that will continue to grow over time, but it serves those who need access to bleeding-edge releases of individual packages.  The main Anaconda repo will always strive to be a stable, tested, commercial-quality set of packages.

> What's the major difference for Anaconda (as a company) and Python community to deal with python packaging problem? Also, what's the relationship between them?
> [color=purple]

I feel that we have a collaborative relationship with them, although we are pursuing different technical directions.  There are technical and historical reasons for why we have created a different packaging system than the core PyPA system.

1) When we started pushing "Python for data science" in 2012, there was no usable solution for packaging and distributing complex binary extensions on Mac, Windows and Linux.  Some may remember those dark times.  Everyone was struggling to build scipy or matplotlib from source; Windows users had to figure out how to install FORTRAN compilers; IPython Notebook was falling back to recommending that Windows users install a Linux VM in order to run the Notebook.... it was a mess. So we (with Guido's blessing) built conda, and within 3 months had put together a distribution of pre-built binaries.  Since that time, the PyPA has evolved its packaging & virtual environment approach, and now the binary Wheels format solves some of the problems that Conda was originally designed to solve.

2) Conda solves a problem that the pip/setuptools/distutils simply was not designed to or trying to solve.  Conda can install different versions of Python itself, into non-root userspace, along with a large number of other tools, frameworks, and libraries.  It supports packaging up libraries of many other languages, include R, Java, Javascript, C, C++, FORTRAN, etc...  It's closer to a cross-platform Homebrew or a "lightweight Docker" than simply a "package manager for Python packages".

3) Python packaging is a complex topic, and it's a big mess partly because of legacy "architecture debt" within the Python community, but also because Python is so successful as a glue language to really gnarly underlying libraries.  By comparison, Javascript packaging ecosystem is its own disaster, and they don't even have to link against FORTRAN code! :)  I think the best, gentle introduction to "Python packaging" is Mahmoud Hashemi's great talk from PyBay a few years back, entitled "The Packaging Gradient": https://www.youtube.com/watch?v=iLVNWfPWAC8&ab_channel=SFPython
While everyone (even XKCD) loves to hate on the dumpster fire that is Python Packaging, it's worth keeping in mind that it's a general, hard problem of "software modularization and integration".  Even the most experienced, well-funded tech companies on the planet struggle with this.  Microsoft struggled with "DLL Hell" for many years. (It even has its own wikipedia entry!)  So some of the problems we face in Python are just a manifestation of this issue.

But if I could point my finger at just one single thing to blame, it's the C linker, and modern operating systems' dynamic loaders.  Of course, I think people are going to all eventually route around this problem by integrating across process boundaries using microservices, REST, and json...

My hope is that as Anaconda becomes more commercially successful, we'll be able to invest more funds into building really great conda+pip/pyenv/poetry/etc. interop.  We have some technical ideas of what could be done, we just don't have the money to do it (yet).  So if any of you are at companies that might be interested in funding some OSS consulting work in this regard, let me know!
###### tags: `PyConTW2020`
