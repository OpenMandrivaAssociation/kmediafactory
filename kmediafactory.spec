Summary:	DVD menu generator
Name:		kmediafactory
Version:	0.8.1
Release:	8
License:	GPLv2+
Group:		Publishing
Url:		http://code.google.com/p/kmediafactory/
Source0:	http://kmediafactory.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch0:		kmediafactory-0.8.1-ffmpeg0.11.patch
Patch1:		kmediafactory-0.8.1-gcc47.patch
Patch2:		kmediafactory-0.8.1-link.patch
Patch3:		kmediafactory-0.8.1-ffmpeg-2.0.patch
Patch4:		kmediafactory-0.8.1-fdr-desktop_validate.patch
Patch5:		kmediafactory-0.8.1-i18n-ru.patch
Patch6:		kmediafactory-0.8.1-ffmpeg2.4.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libkexiv2)
BuildRequires:	pkgconfig(phonon)
BuildRequires:	gettext
BuildRequires:	zip
BuildRequires:	dvdauthor
BuildRequires:	ffmpeg >= 2.5.4
BuildRequires:	mjpegtools
BuildRequires:	ffmpeg-devel >= 2.5.4
BuildRequires:	dvd-slideshow
BuildRequires:	k3b
#BuildRequires:	xine-ui
BuildRequires:	ghostscript
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
Requires:	zip
Requires:	dvdauthor
Requires:	ffmpeg
Requires:	mjpegtools
Requires:	dvd-slideshow
Requires:	k3b
Requires:	xine-ui

%description
KMediaFactory is an easy to use template based dvd authoring tool.
You can quickly create DVD menus for home videos and TV recordings
in three simple steps.

%files -f %{name}.lang
%{_kde_bindir}/*
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_datadir}/config/*
%{_kde_datadir}/config.kcfg/*
%{_kde_datadir}/apps/kmediafactory*
%{_kde_datadir}/apps/kmfwidgets
%{_kde_datadir}/icons/*/*/*/*
%{_kde_datadir}/kde4/services/*
%{_kde_datadir}/kde4/servicetypes/*
%{_kde_datadir}/mime/packages/kmediafactory.xml
%{_kde_libdir}/kde4/*

#--------------------------------------------------------------------

%define kmediafactorykstore_major 0
%define libkmediafactorykstore %mklibname kmediafactorykstore %{kmediafactorykstore_major}

%package -n %{libkmediafactorykstore}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libkmediafactorykstore}
%{name} library.

%files -n %{libkmediafactorykstore}
%{_kde_libdir}/libkmediafactorykstore.so.%{kmediafactorykstore_major}*

#--------------------------------------------------------------------

%define kmf_major 0
%define libkmf %mklibname kmf %{kmf_major}

%package -n %{libkmf}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libkmf}
%{name} library.

%files -n %{libkmf}
%{_kde_libdir}/libkmf.so.%{kmf_major}*

#--------------------------------------------------------------------

%define kmediafactoryinterfaces_major 0
%define libkmediafactoryinterfaces %mklibname kmediafactoryinterfaces %{kmediafactoryinterfaces_major}

%package -n %{libkmediafactoryinterfaces}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libkmediafactoryinterfaces}
%{name} library.

%files -n %{libkmediafactoryinterfaces}
%{_kde_libdir}/libkmediafactoryinterfaces.so.%{kmediafactoryinterfaces_major}*

#--------------------------------------------------------------------
%define devname %mklibname %{name} -d

%package -n	%{devname}
Summary:	Development headers and libraries for %{name}
Group:		Development/C++
Requires:	%{libkmediafactoryinterfaces} = %{version}-%{release}
Requires:	%{libkmf} = %{version}-%{release}
Requires:	%{libkmediafactorykstore} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Development libraries and headers for %{name}.

%files -n %{devname}
%{_kde_includedir}/%{name}
%{_kde_libdir}/lib*.so

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .ffmpeg
%patch1 -p0 -b .gcc
%patch2 -p0 -b .link
%patch3 -p1 -b .ffmpeg2.0~
%patch4 -p1
%patch5 -p1
%patch6 -p1 -b .ffmpeg2.4~

%build
%cmake_kde4
# Really dirty hack to avoid field 'st_atim' has incomplete type (etc) errors
sed -i s,-I/usr/include/libavutil,,g lib/CMakeFiles/kmf.dir/flags.make
%make

%install
%makeinstall_std -C build

desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_kde_datadir}/applications/kde4 \
	--remove-key='Encoding' \
	--remove-category='Application' \
	--add-category='Qt;AudioVideoEditing' \
	%{buildroot}%{_kde_datadir}/applications/kde4/*.desktop

%find_lang %{name} --all-name --with-html

