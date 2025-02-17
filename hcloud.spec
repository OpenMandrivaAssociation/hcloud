# Weird go buildsystem not supported by debuginfo
%undefine _debugsource_packages

Name:		hcloud
Version:	1.50.0
Release:	1
Source0:	https://github.com/hetznercloud/cli/archive/refs/tags/v1.50.0.tar.gz
# go mod vendor
Source1:	vendor.tar.xz
Summary:	Command line interface for interacting with Hetzner Cloud
URL:		https://github.com/hetznercloud/cli
License:	MIT
Group:		Servers
BuildRequires:	golang

%description
Command line interface for interacting with Hetzner Cloud

%prep
%autosetup -p1 -a1 -n cli-%{version}

%build
for cmd in cmd/*; do
	go build -o bin/$(basename $cmd) $(pwd)/$cmd
done

%install
mkdir -p %{buildroot}%{_bindir}
mv bin/* %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions \
	%{buildroot}%{_datadir}/zsh/site-functions \
	%{buildroot}%{_datadir}/fish/vendor_completions.d

%{buildroot}%{_bindir}/hcloud completion bash >%{buildroot}%{_datadir}/bash-completion/completions/%{name}
%{buildroot}%{_bindir}/hcloud completion zsh >%{buildroot}%{_datadir}/zsh/site-functions/_%{name}
%{buildroot}%{_bindir}/hcloud completion fish >%{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files
%{_bindir}/hcloud
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
