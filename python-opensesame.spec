%global modname opensesame

Name:		python-%{modname}
Version:	2.8.1
Release:	1%{?dist}
Summary:	Graphical experiment builder
License:	GPLv2
URL:		http://www.cogsci.nl/software/opensesame
Source0:	http://files.cogsci.nl/software/opensesame/opensesame_2.8.1-1.tar.gz
Patch0:		opensesame-0.25.patch
BuildArch:	noarch
BuildRequires:	pygame 
BuildRequires:	pygame-devel 
BuildRequires:	python-qt4-devel 
BuildRequires:	python-numpy-devel
BuildRequires:	python-qt4-qscintilla
Requires:	pygame 
Requires:	python-qt4 
Requires:	python-numpy


%description
OpenSesame is a graphical experiment builder. OpenSesame provides an easy
to use, point-and-click interface for creating psychological experiments.
In addition to a powerful sketchpad for creating visual stimuli, OpenSesame
features a sampler and synthesizer for sound playback. For more complex tasks,
OpenSesame supports Python scripting using the built-in editor with syntax
highlighting.

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1
sed -i -e '1i#!/usr/bin/python' libopensesame/misc.py 


%build
%py2_build

%install
%py2_install
chmod 755 %{buildroot}%{py_puresitedir}/libopensesame/misc.py
chmod -x %{buildroot}%{_datadir}/opensesame/resources/theme/default/os-custom-icons/index.theme
chmod -x %{buildroot}%{_datadir}/opensesame/resources/theme/gnome/os-custom-icons/index.theme



%files
%{_bindir}/*
%{_datadir}/opensesame
%{_datadir}/applications/opensesame.desktop
%{py_puresitedir}/opensesame-*.egg-info
%{py_puresitedir}/openexp
%{py_puresitedir}/libopensesame
%{py_puresitedir}/libqtopensesame
%{_datadir}/mime/packages/*.xml
%doc COPYING 

%changelog
* Fri Nov 6 2015 Adrian Alves <alvesadrian@fedoraproject.org> 2.8.1-1
- Initial build
