# Advanced container topics

## Setting up Vagrant box

We need to run two provision scripts:

First script installs `ansible` and reboots the machine

```
vagrant up
```

`ansible` RPMs are overlayed so we can build all demo images:

```
vagrant reload --provision-with populate
```
