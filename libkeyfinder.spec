Name: libkeyfinder
Version: 2.2.4
Release: 1%{?dist}

Summary: Musical key detection for digital audio
License: GPL-3.0+
Url: https://mixxxdj.github.io/libkeyfinder

Source: https://github.com/mixxxdj/libkeyfinder/archive/refs/tags/v%{version}.tar.gz

# BuildPreReq: rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake
BuildRequires: fftw-devel
BuildRequires: catch-devel

%description
libkeyfinder is a small C++11 library for estimating the musical key of digital audio.


%package devel
Summary: Development files for libkeyfinder

%description devel
libkeyfinder is a small C++11 library for estimating the musical key of digital audio.


%prep
%autosetup -n %{name}-%{version}
sed -i 's|lib/cmake/KeyFinder|%_lib/cmake/KeyFinder|' CMakeLists.txt

%build
mkdir -p build
%cmake -B build 


%install
%make_install -C build

%files devel
%doc CHANGELOG.md LICENSE README.md
%{_includedir}/keyfinder/
%{_libdir}/libkeyfinder.so
%{_libdir}/pkgconfig/libkeyfinder.pc
%{_libdir}/cmake/KeyFinder/

%changelog

* Mon Jul 05 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.2.4-1
- Initial build 
