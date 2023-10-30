Name:       ansible-role-dci-quay
Version:    0.1.0
Release:    1.VERS%{?dist}
Summary:    Ansible role to setup Quay on a system
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-dci-quay
Source0:    ansible-role-dci-quay-%{version}.tar.gz
BuildArch:  noarch

%description
Ansible role to setup Quay on a system. 

%prep
%setup -qc

%build

%install
find defaults -type f -name '*.yml' -exec install -D -v -p -m 644 "{}" "%{buildroot}%{_datadir}/dci/roles/ansible-role-dci-quay/{}" \;
find handlers -type f -name '*.yml' -exec install -D -v -p -m 644 "{}" "%{buildroot}%{_datadir}/dci/roles/ansible-role-dci-quay/{}" \;
find tasks -type f -name '*.yml' -exec install -D -v -p -m 644 "{}" "%{buildroot}%{_datadir}/dci/roles/ansible-role-dci-quay/{}" \;
find vars -type f -name '*.yml' -exec install -D -v -p -m 644 "{}" "%{buildroot}%{_datadir}/dci/roles/ansible-role-dci-quay/{}" \;

%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/ansible-role-dci-quay


%changelog
* Mon Oct 30 2023 Guillaume Vincent <gvincent@redhat.com> - 0.1.0-1
- Fix rpm name
* Thu Apr  1 2021 Haïkel Guémar <hguemar@fedoraproject.org> - 0.0.1-1
- Initial release
