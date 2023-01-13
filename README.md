# CloudLab Profile: Localdev (in ALPHA)

[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

> **_IMPORTANT:_** If you are new to CloudLab, it is highly recommended that you read through [CloudLab manual: Getting Started](http://docs.cloudlab.us/getting-started.html) before proceeding.

This repository contains:
1. A CloudLab experiment profile `slate-localdev` for SLATE local development.
2. An associated Ansible playbook used to further provision an experiment based on this profile.

## Requirements

Install the required Python packages using a preferred method.

For convenience, this repository includes several pre-defined methods:
* **Anaconda (Conda):** `./environment.yml`
* **Pip:** `./requirements.txt`

## Develop the `slate-localdev` CloudLab Profile

The CloudLab profile is defined in `./profile.py` using the `geni-lib` Pip package. Further details on authoring the profile can be found in [CloudLab manual: Describing a profile with python and geni-lib](http://docs.cloudlab.us/geni-lib.html).

## Provision a CloudLab Experiment

1. Create an experiment on CloudLab using this profile (`slate-localdev`).
2. Clone this repository and copy `./ansible/playbook/group_vars/cloudlab.yml.tmpl` to `./ansible/playbook/group_vars/cloudlab.yml`.
3. Replace the placeholder variables with actual values.
4. Append the following to your SSH config file (`~/.ssh/config`) using actual values:
   ```text
   ## CloudLab & SLATE Local Development
   Host cloudlab-slate-localdev
   HostName <cloudlab hostname>
   IdentityFile </path/to/privatekey>
   Port 22
   User <cloudlab user>
   ```
5. Provision the running experiment via Ansible:

   ```shell
   (python env) /path/to/repo/ansible $ ./provision.sh
   Using /path/to/repo/ansible/playbook/ansible.cfg as config file
   
   PLAY [cloudlab] ************************
   PLAY RECAP ************************
   node1   : ok=18   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
   ```

6. Test connecting to the experiment via SSH:

   ```shell
   $ ssh cloudlab-slate-localdev
   Enter passphrase for key '/path/to/privatekey':
   Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-56-generic x86_64)
   
   * Documentation:  https://help.ubuntu.com
   * Management:     https://landscape.canonical.com
   * Support:        https://ubuntu.com/advantage
     Last login: Fri Jan 13 10:18:00 2023 from 38.94.243.206
     cloudlab_user@node1 ~
     $
   ```

### Things to Note

* The Ansible playbook will only check out the `github_branch` branch of `github_repo_url` the first time the experiment is provisioned.
* Running the Ansible playbook over and over again will not overwrite the cloned git repository.
* CloudLab experiments expire roughly 16 hours after creation unless otherwise extended.
* Make sure to commit and push to GitHub before the experiment expires.

## Resources

* [CloudLab homepage](https://www.cloudlab.us/)
* [CloudLab manual](http://docs.cloudlab.us/)
