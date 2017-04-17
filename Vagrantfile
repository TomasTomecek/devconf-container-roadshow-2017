
$provision_bootstrap_script = <<SCRIPT
rpm-ostree install ansible mc tmux
printf "alias docker=\"sudo docker\"" >/home/vagrant/.bashrc
printf "alias d=\"sudo docker\"" >/home/vagrant/.bashrc
systemctl reboot
SCRIPT

$provision_populate_script = <<SCRIPT
ansible-playbook sync/playbook.yaml
SCRIPT

Vagrant.configure(2) do |config|
  config.vm.provider "libvirt" do |libvirt, override|
    libvirt.driver = "kvm"
    libvirt.memory = 2048
    libvirt.cpus = 1
    # libvirt.cpu_mode = 'host-passthrough'  # Host CPU does not provide required features: svm
  end

  config.vm.provision "bootstrap", type: "shell" do |s|
    s.inline = $provision_bootstrap_script
  end

  config.vm.provision "populate", type: "shell" do |s2|
    s2.inline = $provision_populate_script
  end

  config.vm.define :box do |v|
    # rpm-ostree install strace and reboot
    # vagrant_host.vm.box = "projectatomic/adb"
    v.vm.box = "fedora/25-atomic-host"
    v.vm.hostname = "box"
    v.vm.synced_folder ".", "/vagrant", disabled: true
    v.vm.synced_folder ".", "/home/vagrant/sync", type: "rsync", rsync__exclude: [ ".git/", ".#*", "*~" ]
  end

end
