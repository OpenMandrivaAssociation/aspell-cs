%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 20040614-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Czech
%define languagecode cs
%define lc_ctype cs_CZ

Summary:       %{languageenglazy} files for aspell
Summary(cs):   Český slovník pro korektor překlepů aspell
Name:          aspell-%{languagecode}
Version:       20040614.1
Release:       %mkrel 9
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.sourceforge.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}
Provides:      spell-%{languagecode}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.%{languagecode} Copyright doc/notes.txt doc/README.orig
%{_libdir}/aspell-%{aspell_ver}/*


