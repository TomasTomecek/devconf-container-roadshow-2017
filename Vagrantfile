Vagrant.configure(2) do |config|
  config.vm.provider "libvirt" do |libvirt, override|
    libvirt.driver = "kvm"
    libvirt.memory = 2048
    libvirt.cpus = 1
    libvirt.cpu_mode = 'host-passthrough'  # Host CPU does not provide required features: svm
  end

  config.vm.define :w do |vagrant_host|
    # Box name
    # fedora/25-atomic-host
    # rpm-ostree install strace and reboot
    # vagrant_host.vm.box = "projectatomic/adb"
    vagrant_host.vm.box = "fedora/25-atomic-host"
    vagrant_host.vm.hostname = "w"

    config.vm.synced_folder "./", "/home/vagrant/sync/", type: "rsync",
                            rsync__exclude: [ ".git/", ".#*", "*~" ]
  end

end

