%define hgver beta1.20090110hg

Name:           snowballz
Version:        1.0
Release:        0.5.%{hgver}%{?dist}
Summary:        A Fun Real Time Strategy Game Featuring Snowball Fights with Penguins
Group:          Amusements/Games
License:        MIT
URL:            http://joey101.net/snowballz/
Source0:        %{name}-%{version}-%{hgver}.tar.bz2
# setup.py borrowed from snowballz-0.9.5.1
Source1:        %{name}-setup.py
# pixmap derived from the logo from the project website
Source2:        %{name}.xpm
Source3:        %{name}.desktop
Source4:        %{name}.6
# The wrapper script
Source5:        %{name}

# The hg-fetch script
Source99:       %{name}-snapshot.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  python-setuptools-devel
BuildRequires:  desktop-file-utils

Requires:       python-iniparse
Requires:       pygame
Requires:       pyglet
Requires:       python-rabbyt


%description
Take command of your army of penguins as you blaze your path to victory! March
through snow laden forests to conqueror new frontears and grow your small army.
Ambush enemy lines with blasts of freezing snowballs. But don't neglect your 
home, invaders are just over the next snow drift! Gather fish for your cold 
penguins to munch on as they warm up in your cozy igloo. It's a snowy world you
don't want to miss!

This promising project is in need of developers, for both code and content. 
Interested folks should refer to the project website.


%prep
%setup -q -n %{name}
cp %{SOURCE1} setup.py

# Change the hardcoded path with a macro:
sed 's|/usr/share|%{_datadir}|' %{SOURCE5} > %{name}-wrapper
touch -r %{SOURCE5} %{name}-wrapper

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}

%{__python} setup.py install --skip-build --root %{buildroot} --install-lib %{_datadir}/%{name}

# Kill the egg since the eggs are only needed in python
# libraries that go to site-packages.
rm -rf %{buildroot}/%{_datadir}/%{name}/*egg-info

# Install the files omitted by the setuptools script
cp -a data *.py %{buildroot}/%{_datadir}/%{name}

install -p -m 0644 -D %{SOURCE4} %{buildroot}%{_mandir}/man6/%{name}.6

desktop-file-install --vendor="" \
        --dir=%{buildroot}%{_datadir}/applications \
        %{SOURCE3}

install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

install -p -D -m 0755 %{name}-wrapper %{buildroot}%{_bindir}/%{name}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.*

%changelog
* Wed Feb 04 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.0-0.5.beta1.20090110hg
- Updated description

* Mon Jan 12 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.0-0.4.beta1.20090110hg
- Wrapper script supplied separately once again

* Sun Jan 11 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.0-0.3.beta1.20090110hg
- More changes in the .desktop file (Comment and GenericName)
- Game files are installed in %%{datadir}/%%{name} instead of %%{datadir}/games/%%{name}
- Remove the egg
- Wrapper script supplied internally once again

* Sat Jan 10 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.0-0.2.beta1.20090110hg
- Changes in summary and in the .desktop file
- License is MIT
- Remove the font during the snapshot creation process
- Wrapper script supplied separately

* Mon Dec 22 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.0-0.1.beta1.20081222hg
- Update to 1.0-beta1

* Sun Aug 17 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.9.5.1-1
- Initial Release
