# Web Exploitation

- Namespace: picoctf/examples
- Type: custom
- Category: Web Exploitation
- Points: 1
- Templatable: yes

## Description

Do you know how to examine images?

## Details
Check out {{link_as('/', 'here')}}

## Hints

- Try to look for more files.

## Solution Overview

Use Nikto to look for more files.

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

- Steganography
- Hashing
- Looking for directories

## Tags

- example

## Attributes

- author: Joel Jefferson Musiime
- organization: picoCTF
- event: picoCTF Problem Developer Training
