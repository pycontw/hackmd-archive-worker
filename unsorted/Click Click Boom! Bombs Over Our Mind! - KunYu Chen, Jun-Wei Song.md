# Click Click Boom! Bombs Over Our Mind! - KunYu Chen, Jun-Wei Song

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

> 從這開始
> 
## Adventure Started

* Develop a virus engine for VirusTotal

## Zip Bomb

* Compression bombs
    * Compression ratio = Uncompressed size / compressed size
    * Ratio > 100 can be considered as a zip bomb

## Create a Package

* zipfile does not handle zip bombs
* [SUNZIP](https://pypi.org/project/sunzip/) (Secure Unzip) on Pypi

## Request a CVE number

* Vulnerability

## Patch

* Steps
    * Address the issue on B.P.O
    * Discuss with core developers
    * Send the patch github

## Discussion on B.P.O

* B.P.O = https://bugs.python.org
* 1st round discussion (rejected)
    * Should not limit compression ratio
        * Hackers can check source code to know the threshold
    * Should make a decision what ZIP files should be rejected
* 2nd round discussion (rejected)
    * It's user's responsibility to verify source
* 3rd round discussion (accepted)
    * https://python-security.readthedocs.io/vuln/zip-bomb.html
    * Document improvement: https://docs.python.org/3.8/library/zipfile.html#decompression-pitfalls

## Prevent mistake
* Send e-mail to security@python.org directly instead of posting it on B.P.O

###### tags: `PyConTW2019`
