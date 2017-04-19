# Advanced container deep-dive

## Setup via USB

If you received USB key from me, this is how you should set the vagrant box up:

```
$ vagrant box add ./devconf-container-roadshow-2017.box --name devconf-container-roadshow-2017
```

Now the box is inside your system, so you can init a new vagrant project:

```
$ vagrant init devconf-container-roadshow-2017
```

Don't run the command above inside this git repository, you should create a new directory.

Once done, just ssh into your VM:

```
$ vagrant ssh
```


## Setting up Vagrant box from scratch

These are the steps to set up the vagrant box from scratch.

We need to run two provision scripts.

First script installs `ansible` and some other packages, and reboots the machine:

```
vagrant up --provision-with bootstrap
```

`ansible` RPMs are overlayed so we can build all demo images:

```
vagrant reload --provision-with populate
```

You can ssh into your VM now:

```
$ vagrant ssh
```
