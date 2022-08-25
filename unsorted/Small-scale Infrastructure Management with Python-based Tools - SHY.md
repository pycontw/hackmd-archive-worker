# Small-scale Infrastructure Management with Python-based Tools - SHY

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

> 從這開始

## Speaker & Background

- Engineer in NTU
- 處理教務相關系統
- Small-scale: No datacenter

## Notes

### Install OS

- If it hurts, do it more often.
- Tools
    - [MAAS](https://maas.io)

### MAAS

- Discovery aka enlistment
    - Network Boot / PXE + DHCP + TFTP
- Power control
    - IPMI / iLO / DRAC
- Deployment
    - Courtin (another tool by the same comparny)
    - File download from MASS server
- Post Installation
    - could-init

<!-- -->

- Gottchas
    - **Depend** on MAAS
        - DNS
        - sudo
    - stucked installation: 一直重複下載，如果失敗的話，需要手動排除。
     - complex：太多種，有可能下載錯版本。
- Alternative Toolings to MASS
    - [Openstack](https://www.openstack.org/) (適合更大規模的部屬情境)
    - Installing OS
        - [Clobber](https://cobbler.github.io)
        - [Spacewalk](https://spacewalkproject.github.io/)
        - [Foreman](https://theforeman.org/)
        - [Digital Rebar](https://rebar.digital/)
        - [Razor](https://github.com/puppetlabs/razor-server)
    - IP Address Management
        - [Netbox](https://netbox.readthedocs.io/en/stable/)

## Software management

### Ansible

- **Declarative** (Not procedural)
- Provide SSH feature by `Paramiko` (Ansible Modules)
- Similar tools
    - Chef, Puppet, SaltStack, Capistrano
- Going Forward
    - Container Image (Docker)

## Keyword: Infrastructure as code
## Automate Everything?

- Minimal cost
- Or you can use 

## Q & A

- Q: How to fix CVE? 
- Update ansible Configuration 
    - or Actually: SSH into server and patch
- Q: MASS need any authentication method before discovery machine
    - establish turst on network configuration
###### tags: `PyConTW2019`

